from pydantic import BaseModel, Field
from pydantic import model_validator
import uuid
from datetime import date, datetime
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
    uid: uuid.UUID

class CoxwainEvaluation():
    '''
        Anonymous feedback on a coxwain's abilities and suggestions from rowers
    '''
    uid: uuid.UUID
    semester: Semester
    year: int = Field(ge=1900)
    feedback: str

class Rower():
    '''
        A member that rows
    '''
    uid: uuid.UUID


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

class MembershipRolePermissionsUpdateModel(StrictModel):
    '''
        Flips bool value in database where bool is true
    '''
    role: MemberRole
    access_site: bool = False
    create_announcements: bool = False
    manage_dates: bool = False
    manage_members: bool = False
    manage_roles: bool = False
    view_funds: bool = False
    view_roster: bool = False

    @model_validator(mode="after")
    def require_one(self):
        permissions = [
            self.access_site,
            self.create_announcements,
            self.manage_dates,
            self.manage_members,
            self.manage_roles,
            self.view_funds,
            self.view_roster,
        ]

        if not any(permissions):
            raise ValueError("At least one permission must be set to True")

        return self


class MemberStatus(StrictModel):
    '''
        A member's current membership status
        NOTE: may just be stuch into the User table instead
        
    '''
    uid: uuid.UUID
    role: MembershipRole = MembershipRole.INACTIVE

class MemberEnrollment(StrictModel):
    '''
        Tracks membership status on a per-semester basis
    '''
    uid: uuid.UUID
    year: int = Field(ge=1900)
    semester: Semester
    role: MemberRole = MemberRole.MEMBER
    are_dues_paid: bool

