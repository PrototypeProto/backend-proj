from typing import Optional, Union, Annotated, List
'''
    Optional[type(s)]
    Union() or (type | None)
    Annotated[type, "annotation textr"]
'''
from fastapi import FastAPI, Header, APIRouter, Depends
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from .schemas import UserUpdateModel, UserCreateModel, User, UserLoginModel
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import UserService
from src.db.main import get_session
from .utils import create_access_token, decode_token, verify_passwd
from datetime import datetime, timedelta

REFRESH_TOKEN_EXPIRY = 2


'''
    A custom route to access users
    simple CRUD routes
    calls service() methods to perform business logic
'''

router_at_users = APIRouter()
user_service = UserService()



@router_at_users.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    email = user_data.email

    user_exists = await user_service.get_user_by_email(email, session)
    
    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with email already exists")

    new_user = await user_service.create_user(user_data, session)
    return new_user

@router_at_users.post("/login", status_code=status.HTTP_200_OK)
async def login_user(login_data: UserLoginModel, session: AsyncSession = Depends(get_session)):
    email = login_data.email
    passwd = login_data.passwd

    user = await user_service.get_user_by_email(email, session)

    if user is not None:
        passwd_valid = verify_passwd(passwd, user.passwd_hash)

        if passwd_valid:
            access_token = create_access_token(
                user_data={
                    "email": user.email,
                    "uid": str(user.uid),
                },
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
            )

            refresh_token = create_access_token(
                user_data={
                    "email": user.email,
                    "uid": str(user.uid),
                },
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY),
            )

            return JSONResponse(
                content={
                    "message": "login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user":{
                        "email": user.email,
                        "uid": str(user.uid)
                    },
                }
            )

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email and/or password")

    

@router_at_users.get("/all", response_model=List[User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await user_service.get_all_users(session)
    return users

# @router_at_users.get("/{user_uid}", response_model=User)
# async def get_user(user_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
#     user = await user_service.get_user(user_uid, session)

#     if user:
#         return user
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")



# @router_at_users.patch("/{user_uid}", response_model=User)
# async def update_user(user_uid: str, user_update_data: UserUpdateModel, session: AsyncSession = Depends(get_session)) -> dict:
#     updated_user = await user_service.update_user(user_uid, user_update_data, session)
        
#     if updated_user:
#         return updated_user
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")


# @router_at_users.delete("/{user_uid}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(user_uid:str, session: AsyncSession = Depends(get_session)):
#     user_to_delete = await user_service.delete_user(user_uid, session)

#     if not user_to_delete:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

