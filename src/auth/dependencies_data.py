from .dependencies import RoleChecker
from fastapi.exceptions import HTTPException
from fastapi import Depends
from enum import Enum

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


role_checker = Depends(RoleChecker(['member']))
admin_rolechecker = Depends(RoleChecker([MemberRole.ADMIN]))
coach_rolechecker = Depends(RoleChecker([MemberRole.ADMIN, MemberRole.COACH]))
officer_rolechecker = Depends(RoleChecker([MemberRole.ADMIN, MemberRole.OFFICER]))
member_rolechecker = Depends(RoleChecker([MemberRole.ADMIN, MemberRole.COACH, MemberRole.OFFICER]))
public_rolechecker = Depends(RoleChecker([role for role in MemberRole]))