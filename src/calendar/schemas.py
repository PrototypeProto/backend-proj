from pydantic import BaseModel, Field, Union
import uuid
from datetime import date, datetime, time
from sqlmodel import SQLModel
from enum import Enum

# Prevent the addition of extra fields
class StrictModel(BaseModel):
    model_config = {
        "extra": "forbid"
    }



class AttendanceTypes(str, Enum):
    '''
        "Present" is omitted intentionally to reduce noise
    '''
    ABSENT = "absent"
    ABSENT_EXC = "excused_absence"
    TARDY = "tardy"
    TARDY_EXC = "excused_tardy"

# TODO: break this apart for DB into 2 tables
class DateType(Enum):
    WATER = ("On the water practice", "#1f77b4")
    LAND = ("On the land practice", "#ff7f0e")
    WEEKEND_PRACTICE = ("Special weekend practice for upcoming matches", "#2ca02c")
    OYO = ("On your own workout", "#d62728")
    SETUP = ("Light practice / Load up gear on trailer", "#9467bd")
    AWAY_SCRIMMAGE = ("Away for scrimmage at another team's place", "#8c564b")
    HOME_SCRIMMAGE = ("Hosting scrimmage against another team", "#e377c2")
    REGATTA = ("Away for official regatta competition", "#7f7f7f")
    VOLUNTEER = ("Volunteering manpower at university event for club funding", "#bcbd22")
    FUNDRAISING = ("Raising funds for the team", "#17becf")

    # Enables to call DateType.{ENUM}.{description/color}
    def __init__(self, description: str, color: str):
        self.description = description
        self.color = color


class Attendance(StrictModel):
    '''
        By default, omit the "present" type a
    '''
    nid: str
    date: date
    presence_status: AttendanceType

class ScheduledMeetings(StrictModel):
    '''
        Used to display information on active club dates
    '''
    date: date
    date_type: DateType
    # "HR:MN {AM/PM}"
    time: str = Field(min_length=8, max_length=8)
    ext_description: Union[str, None]

class ScheduledAttendance(StrictModel):
    '''
        Data here is subject to change as availability changes from week-to-week
        false = absent that day
        true = present that day
    '''
    nid: str = Field(min_length=8, max_length=8)
    mon: bool
    tue: bool
    wed: bool
    thu: bool
    fri: bool
    sat: bool
    sun: bool