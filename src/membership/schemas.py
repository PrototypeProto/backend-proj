from pydantic import BaseModel, Field
import uuid
from datetime import date, datetime
from sqlmodel import SQLModel
from enum import Enum

# Prevent the addition of extra fields
class StrictModel(BaseModel):
    model_config = {
        "extra": "forbid"
    }



class MemberRole(str, Enum):
    ADMIN = "admin"
    COACH = "coach"
    OFFICER = "officer"
    MEMBER = "member"
    INACTIVE = "inactive"

class Semester(str, Enum):
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"

class Coxwain():
    '''
        Member can be a coxwain
    '''
    nid: str = Field(min_length=8, max_length=8)

class CoxwainEvaluation():
    '''
        Feedback on a coxwain's abilities and suggestions
    '''
    nid: str = Field(min_length=8, max_length=8)
    semester: Semester
    year: int = Field(ge=1900)
    feedback: str

class Rower():
    '''
        Member can row
    '''
    nid: str = Field(min_length=8, max_length=8)




class MembershipRolePermissions(StrictModel):
    role: MemberRole
    access_site: bool
    create_announcements: bool
    manage_dates: bool
    manage_members: bool
    manage_roles: bool
    view_funds: bool
    view_roster: bool


class MemberStatus(StrictModel):
    nid: str = Field(min_length=8, max_length=8)
    role: MembershipRole = MembershipRole.INACTIVE

class MemberEnrollment(StrictModel):
    '''
        Tracks membership status on a per-semester basis
    '''
    nid: str = Field(min_length=8, max_length=8)
    year: int = Field(ge=1900)
    semester: Semester
    role: MemberRole = MemberRole.MEMBER
    are_dues_paid: bool

