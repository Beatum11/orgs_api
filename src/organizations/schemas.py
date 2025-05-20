from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from uuid import UUID
from typing import Optional


class Building(BaseModel):
    address: str
    longitude: str
    latitude: str

class Activity(BaseModel):
    name: str
    parent: Optional["Activity"]
    children: Optional[list["Activity"]]

class Organization(BaseModel):
    name: str
    tel: str
    building: Building
    activities: list[Activity]

class OrganizationOut(BaseModel):
    id: UUID
    name: str
    tel: str
    activities: list[Activity]
    
    model_config = ConfigDict(from_attributes=True)


Activity.model_rebuild()



