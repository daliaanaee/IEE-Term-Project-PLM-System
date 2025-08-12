from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Team(SQLModel, table=True):
    TeamName: str = Field(primary_key=True)

class Design(SQLModel, table=True):
    DesignID: int = Field(primary_key=True)
    CodeName: str
    ChassisType: str
    UnitCost: float
    UnitRevenue: float

class TeamDesign(SQLModel, table=True):
    TeamName: str = Field(foreign_key="team.TeamName", primary_key=True)
    DesignID: int = Field(foreign_key="design.DesignID")

class Chassis(SQLModel, table=True):
    Serial: str = Field(primary_key=True)
    TeamName: str = Field(foreign_key="team.TeamName")
    PurchaseTimestamp: datetime
    SaleTimestamp: Optional[datetime] = None
    Status: str
