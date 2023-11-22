from uuid import UUID
import fastapi as fa

from starlette import status
from api import schemas
from db.repository import IssueRepo
from exceptions import common as common_exc, http as http_exc


router = fa.APIRouter(prefix='/issue', tags=['issue'])
repo = IssueRepo()


@router.get('')
async def get_issues(query: schemas.IssueGetSchema = fa.Depends()):
    return await repo.get_list(**query.model_dump(exclude_none=True))


@router.get('/{id}')
async def get_issue(id: UUID):
    try:
        return await repo.get(id)
    
    except common_exc.NotFoundExcepton as e:
        http_exc.HTTPNotFoundException(detail=str(e))
        
        
@router.post('')
async def create_issue(body: schemas.IssueSchema):
    try:
        return await repo.create(body.model_dump)
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    
@router.patch('/{id}')
async def update_issue(id: UUID, body: schemas.IssueUpdateSchema):
    try:
        return await repo.update(id, **body.model_dump(exclude_none=True))
    
    except common_exc.UpdateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
    
@router.delete('/{id}')
async def delete_issue(id: UUID):
    try:
        await repo.delete(id)
        
        return fa.responses.Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    