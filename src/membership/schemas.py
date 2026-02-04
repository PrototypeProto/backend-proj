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
    '''
        May deprecate ADMIN role in favor of president+VP role, TBD
    '''
    ADMIN = "admin"
    COACH = "coach"
    OFFICER = "officer"
    MEMBER = "member"
    INACTIVE = "inactive"

class Semester(str, Enum):
    '''
        NO practice during the summer, but placeholder in case situation changes
    '''
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"

class Coxwain():
    '''
        Marks members that are coxwains
    '''
    nid: str = Field(min_length=8, max_length=8)

class CoxwainEvaluation():
    '''
        Anonymous feedback on a coxwain's abilities and suggestions from rowers
    '''
    nid: str = Field(min_length=8, max_length=8)
    semester: Semester
    year: int = Field(ge=1900)
    feedback: str

class Rower():
    '''
        A member that rows
    '''
    nid: str = Field(min_length=8, max_length=8)




class MembershipRolePermissions(StrictModel):
    '''
        Restricts certain APIs based on these permissions
    '''
    role: MemberRole
    access_site: bool
    create_announcements: bool
    manage_dates: bool
    manage_members: bool
    manage_roles: bool
    view_funds: bool
    view_roster: bool


class MemberStatus(StrictModel):
    '''
        A member's current membership status
        NOTE: may just be stuch into the User table instead
        
    '''
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

