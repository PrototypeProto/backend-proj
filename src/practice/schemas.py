from pydantic import BaseModel, Field
from pydantic import model_validator
from uuid import UUID
from datetime import date, datetime
from enum import Enum
from src.db.db_enum_models import SemesterEnum

# Prevent the addition of extra fields
class StrictModel(BaseModel):
    model_config = {
        "extra": "forbid"
    }


'''

    ATTENDANCE-RELATED MODELS

'''


class SemesterAttendance(StrictModel):
    '''
        Tracks each students's absences that semster, if not absent on that day then they were present
        sort by (year, semester) for current stats
    '''
    member_id = UUID
    semester: SemesterEnum
    year: int = Field(ge=1900)
    day: date
    arrival_time: datetime.time
    is_tardy: bool = False

    

'''

    PRACTICE-RELATED MODELS

'''


class Workout(StrictModel):
    '''
        Because workouts are spaced out and vary, can now track individual performance per iteration
        Front end will clean up interactions a lot more, allowing users to manually enter information to the correct workout
    '''
    workout_id: UUID
    workout: str 
    desc: str 
    date: date

class WorkoutCreateModel(StrictModel):
    workout: str 
    desc: str 
    date: date

class MemberWorkoutPerformance(StrictModel):
    '''
        Stores specific data on users performance
        Edit, delete and create follow same parameters, except delete doesnt require performance_comment
    '''
    workout_id: UUID
    member_id: UUID
    sequence_num: int 
    performance: datetime.time





