from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.database import get_db

from repositories.temple_repository_impl import TempleRepositoryImpl

from services.temple_service_impl import TempleServiceImpl

from schemas.api_response import ApiResponse
from schemas.temple_schema import TempleResponse

router = APIRouter()


@router.get(
    "/temples",
    response_model=ApiResponse[list[TempleResponse]]
)
def get_temples(db: Session = Depends(get_db)):

    repository = TempleRepositoryImpl(db)

    service = TempleServiceImpl(repository)

    temples = service.get_all_temples()

    return ApiResponse(

        responseCode=200,

        responseMessage="Temple details fetched successfully",

        responseBody=temples
    )