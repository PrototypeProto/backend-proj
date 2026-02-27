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
from src.auth.schemas import User
from .schemas import Workout, WorkoutCreateModel, MemberWorkoutPerformance
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.service import UserService
from src.db.main import get_session
from datetime import datetime, timedelta
from src.auth.dependencies import RefreshTokenBearer, access_token_bearer, get_current_user_by_username, get_current_user_uuid
from src.auth.dependencies_data import admin_rolechecker, coach_rolechecker, officer_rolechecker, member_rolechecker, public_rolechecker
from .service import MemberService
from uuid import UUID

REFRESH_TOKEN_EXPIRY_DAYS = 2


practice_router = APIRouter()
user_service = UserService()
member_service = MemberService()
SessionDependency = Annotated[AsyncSession, Depends(get_session)]


@practice_router.post("/create_workout", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED, response_model=UUID)
async def create_new_workout(workout_data: WorkoutCreateModel, session: SessionDependency) -> UUID:
    pass

@practice_router.patch("/update_workout", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
async def update_workout():
    pass


# @practice_router.delete("/remove_workout", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def a():
#     pass


# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass


# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass

# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass

# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass


# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass


# @practice_router.post("/", dependencies=[public_rolechecker], status_code=status.HTTP_201_CREATED)
# async def ():
#     pass
