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



class Workout(StrictModel):
    '''
        Because workouts are spaced out and vary, can now track individual performance per iteration
        Front end will clean up interactions a lot more, allowing users to manually enter information to the correct workout
    '''
    workout_id: uuid.UUID
    workout_iteration: int = Field(ge=1)
    date: date
    workout_description: str


class MemberWorkoutPerformance(StrictModel):
    '''
        Stores specific data on users performance
        Edit, delete and create follow same parameters, except delete doesnt require performance_comment
    '''
    workout_id: uuid.UUID
    workout_iteration: int = Field(ge=1)
    uid: uuid.UUID
    performance_comment: str
