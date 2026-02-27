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
from .schemas import *
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.service import UserService
from src.db.main import get_session
from datetime import datetime, timedelta
from src.auth.dependencies import RefreshTokenBearer, access_token_bearer, get_current_user_uuid, get_current_user_by_username
from src.auth.dependencies_data import admin_rolechecker, coach_rolechecker, officer_rolechecker, member_rolechecker, public_rolechecker
from .service import MemberService
from uuid import UUID

REFRESH_TOKEN_EXPIRY_DAYS = 2


'''
    A custom route to access users
    simple CRUD routes
    calls service() methods to perform business logic
'''

member_router = APIRouter(dependencies=[access_token_bearer])
user_service = UserService()
member_service = MemberService()
SessionDependency = Annotated[AsyncSession, Depends(get_session)]


@member_router.post("/add_coxain", response_model=CoxwainModel, dependencies=[officer_rolechecker], status_code=status.HTTP_201_CREATED)
async def add_coxain(cox: CoxwainModel, session: SessionDependency):
    user_exists = await user_service.get_user_by_uid(cox.cox_id, session)
    
    if user_exists is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Coxain is already a coxain")

    new_user = await member_service.create_coxain(cox, session)
    return new_user

@member_router.post("/submit_coxwain_evaluation", response_model=CoxwainEvaluationModel, dependencies=[public_rolechecker])
async def evaluate_coxwain( cox_eval: CoxwainEvaluationModel, session: SessionDependency) -> dict:
    # TODO: log who sent feedback
    coxwain_eval = await member_service.create_coxwain_evaluation(cox_eval, session)

    if coxwain_eval is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user provided / Failed to submit evaluation")

    return coxwain_eval

@member_router.delete("/remove_coxwain_evaluation", dependencies=[officer_rolechecker], status_code=status.HTTP_204_NO_CONTENT)
async def del_coxwain_evaluation(cox_eval: DeleteCoxwainEvaluationModel, session: SessionDependency):
    if not await member_service.remove_one_coxwain_evaluation(cox_eval, session):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Unable to remove selected coxwain evaluation"
        )

@member_router.get("/get_coxwain_evaluations", response_model=list[CoxwainEvaluationModel])
async def get_cox_evals(session: SessionDependency, eval_search_params: CoxwainModel):
    result = await member_service.get_all_coxwain_evaluations(eval_search_params, session)
    return result

# NOTE: New code from here, 

@member_router.post("/add_rower", status_code=status.HTTP_201_CREATED, response_model=RowerModel)
async def add_rower(session: SessionDependency, rower_data: RowerModel) -> RowerModel:
    rower = await member_service.create_rower(rower_data, session)
    if rower is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Failed to create rower / User already exists"
        )
    return rower

@member_router.patch("/update_role_permissions")
async def update_role_perms(session: SessionDependency, role_data: RolePermissionsUpdateModel) -> None:
    if not await member_service.update_role_permissions(role_data, session):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid paramas / No changes made"
        )
    

@member_router.post("/enroll_member", status_code=status.HTTP_201_CREATED)
async def enroll_member(member_data: CreateMemberEnrollmentHistoryModel, session: SessionDependency):
    if not await member_service.enroll_member(member_data, session):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid paramas / No changes made"
        )

# @member_router.put("/raise_privilege", status_code=status.HTTP_202_ACCEPTED)

# @member_router.put("/raise_privilege", status_code=status.HTTP_202_ACCEPTED)

# @member_router.put("/raise_privilege", status_code=status.HTTP_202_ACCEPTED)

