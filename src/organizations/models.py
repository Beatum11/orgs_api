from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Table
from typing import Optional

class Base(DeclarativeBase):
    pass

class Organization(Base):
    __tablename__ = 'organizations'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    tel: Mapped[str] = MappedColumn(String, unique=True)
    name: Mapped[str] = MappedColumn(String, unique=True)

    building_id: Mapped[int] = MappedColumn(ForeignKey('buildings.id'))
    building: Mapped["Building"] = relationship(back_populates='organizations')

    activities: Mapped[list["Activity"]] = relationship(
        secondary='organization_activity',
        back_populates='organizations'
    )



class Building(Base):
    
    __tablename__ = 'buildings'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)

    address: Mapped[str] = MappedColumn(String, unique=True)

    longitude: Mapped[float] = MappedColumn(Float)
    latitude: Mapped[float] = MappedColumn(Float)

    organizations: Mapped[list['Organization']] = relationship(back_populates='building')



class Activity(Base):
    
    __tablename__ = 'activities'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    name: Mapped[str] = MappedColumn(String, unique=True)

    parent_id: Mapped[Optional[int]] = MappedColumn(ForeignKey('activities.id'))

    parent: Mapped[Optional['Activity']] = relationship(
        back_populates='children',
        remote_side='Activity.id'
    )

    children: Mapped[Optional[list['Activity']]] = relationship(
        back_populates='parent',
        cascade='all, delete-orphan'
    )

    organizations: Mapped[list['Organization']] = relationship(
        secondary='organization_activity',
        back_populates='activities'
    )


organization_activity = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)

