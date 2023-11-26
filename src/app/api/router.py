import fastapi as fa

from api.issue.routes import router as issue_router
from adapters import MinIOClient
from starlette import status


router = fa.APIRouter(prefix='/api')
router.include_router(issue_router)


# @router.get('/issues')
# async def get_issues() -> list[dict]:
#     pass


@router.post('/upload')
async def upload_file(file: fa.UploadFile = fa.File(...)):
    client = MinIOClient()
    await client.upload_from_bytes(file)
    
    return fa.Response(status_code=status.HTTP_204_NO_CONTENT)
