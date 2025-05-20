from fastapi import APIRouter, Depends, HTTPException, status
from ..db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.organizations.services import get_org_services, OrgService
from logger import logger
from src.organizations.schemas import OrganizationOut
from dependencies import get_api_key

router = APIRouter(dependencies=[get_api_key])


@router.get('/', response_model=OrganizationOut, summary="Получить организацию по ее названию")
async def get_org_by_id(name: str, 
                        session: AsyncSession = Depends(get_session),
                        organization_services: OrgService = Depends(get_org_services)):
    try:
        organization = await organization_services.get_organization_by_name(session, name)
        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Организация не найдена"
            )
        return OrganizationOut.model_validate(organization)

    except Exception as e:
        logger.error(f'Ошибкаааа: {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при получении данных из базы"
        )
    

@router.get('/{org_id}', response_model=OrganizationOut, summary="Получить организацию по ID")
async def get_org_by_id(org_id: int, 
                        session: AsyncSession = Depends(get_session),
                        organization_services: OrgService = Depends(get_org_services)):
    try:
        organization = await organization_services.get_organization_by_id(session, org_id)
        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Организация не найдена"
            )
        
        return OrganizationOut.model_validate(organization)
        

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при получении данных из базы"
        )


@router.get("/by-building/{building_id}", response_model=list[OrganizationOut], summary="Список организаций в конкретном здании")
async def get_orgs_from_building(building_id: int, 
                                 session: AsyncSession = Depends(get_session),
                                 organization_services: OrgService = Depends(get_org_services)):
    try:
        orgs = await organization_services.get_orgs_from_building(session, building_id)
        if not orgs:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Организации в здании не найдены"
            )
        
        serialized_orgs = [OrganizationOut.model_validate(org) for org in orgs]
        return serialized_orgs
    
    except Exception as e:
        logger.error(f'Ошибкаааа: {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при получении данных из базы"
        )
    
 

@router.get('/by-activity/', response_model=list[OrganizationOut], summary='Список организаций по деятельности и её подкатегориям')
async def find_orgs_on_activity(activity_name: str, 
                               session: AsyncSession = Depends(get_session),
                               organization_services: OrgService = Depends(get_org_services)):
    try:
        organizations = await organization_services.find_orgs_based_on_activity(session, activity_name)
        if not organizations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Организации не найдены"
            )
        
        serialized_organizations = [OrganizationOut.model_validate(org) for org in organizations]
        return serialized_organizations

    except Exception as e:
        logger.error(f'Ошибкаааа: {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при получении данных из базы"
        )
    

@router.get('/by-activity/{activity_id}', response_model=list[OrganizationOut], summary="Список организаций по конкретной деятельности.")
async def get_orgs_on_activity(activity_id: int, 
                               session: AsyncSession = Depends(get_session),
                               organization_services: OrgService = Depends(get_org_services)):
    try:
        organizations = await organization_services.get_orgs_based_on_activity(session, activity_id)
        if not organizations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Организации не найдены"
            )
        
        serialized_organizations = [OrganizationOut.model_validate(org) for org in organizations]
        return serialized_organizations

    except Exception as e:
        logger.error(f'Ошибкаааа: {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при получении данных из базы"
        )


