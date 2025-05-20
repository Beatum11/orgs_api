from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Activity, Building, Organization
from sqlalchemy import select
from .utils import get_all_children

class OrgService:

    @staticmethod
    async def get_orgs_from_building(session: AsyncSession,
                                     building_id: int):
        
        
        statement = select(Building).where(Building.id == building_id)
        res = await session.execute(statement)
        if res is not None:
            building: Building = res.scalars.first()
            return building.organizations
        return None

    # искать организации по виду деятельности. Например, поиск по виду деятельности «Еда», 
    # которая находится на первом уровне дерева, и чтобы нашлись все организации, 
    # которые относятся к видам деятельности, лежащим внутри. 
    # Т.е. в результатах поиска должны отобразиться организации с видом деятельности 
    # Еда, Мясная продукция, Молочная продукция.

    @staticmethod
    async def find_orgs_based_on_activity(activity_name: str,
                                          session: AsyncSession):
        
        statement = select(Activity).where(Activity.name == activity_name)
        res = await session.execute(statement)

        if res is not None:
            activity: Activity = res.scalars.first()
            await session.refresh(activity, attribute_names=["children"])
            ids = get_all_children(activity)
            
            statement_2 = (
                select(Organization)
                .join(Organization.activities)
                .where(Activity.id.in_(ids))
                .distinct()
            )
            res = await session.execute(statement_2)
            return res.scalars().all()
        
        return None



    # все организации в рамках одного вида деятельности                                         
    @staticmethod
    async def get_orgs_based_on_activity(session: AsyncSession,
                                         activity_id: int):
        
        statement = select(Activity).where(Activity.id == activity_id)
        res = await session.execute(statement)

        if res is not None:
            activity: Activity = res.scalars.first()
            return activity.organizations
        return None
    

    
    @staticmethod
    async def get_organization_by_id(session: AsyncSession, org_id: int):

        statement = select(Organization).where(Organization.id == org_id)
        res = await session.execute(statement)

        if res is not None:
            organization: Organization = res.scalars.first()
            return organization
        return None



    @staticmethod
    async def get_organization_by_name(session: AsyncSession, name: str):

        statement = select(Organization).where(Organization.name == name)
        res = await session.execute(statement)

        if res is not None:
            organization: Organization = res.scalars.first()
            return organization
        return None



    # список организаций, которые находятся в заданном 
    # радиусе/прямоугольной области относительно указанной 
    # точки на карте. список зданий

    # @staticmethod
    # async def orgs_by_location(lat: float, long: float, radius: float, session: AsyncSession):
    #     statement = select(Building).where(Building.latitude == lat and Building.long == long)
    #     res = await session.execute(statement)
    #     if res:
    #         buildings = res.scalars.all()



def get_org_services():
    return OrgService()