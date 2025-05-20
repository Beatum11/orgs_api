from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from config import settings


VALID_API_KEYS = settings.API_KEYS

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

class APIKeyValidator:
    def __init__(self, valid_keys: set[str]):
        self.valid_keys = valid_keys

    async def __call__(self, api_key: str = Depends(api_key_header)) -> str:
        if not api_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Нужен API ключ"
            )
        if api_key not in self.valid_keys:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Невалидный API ключ",
            )
        return api_key


get_api_key = APIKeyValidator(valid_keys=settings.API_KEYS)

