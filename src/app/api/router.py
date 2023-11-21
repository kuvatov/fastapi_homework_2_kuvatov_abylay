from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any
from db.models import Issue, Issue_Pydantic, IssueIn_Pydantic


router = APIRouter(prefix='/api', tags=['issue'])


class Status(BaseModel):
    message: str


@router.get('/issues', response_model=list[Issue_Pydantic])
async def get_issues() -> list[dict]:
    return await Issue_Pydantic.from_queryset(Issue.all())


@router.post('/issues', response_model=Issue_Pydantic)
async def create_issue(issue: IssueIn_Pydantic) -> Issue:
    issue_obj = await Issue.create(**issue.model_dump(exclude_unset=True))
    return await Issue_Pydantic.from_tortoise_orm(issue_obj)


@router.get('/issue/{id_}', response_model=Issue_Pydantic)
async def get_issue(issue_id: int) -> Issue:
    return await Issue_Pydantic.from_queryset_single(Issue.get(id=issue_id))


@router.put('/issue/{id_}', response_model=Issue_Pydantic)
async def update_issue(issue_id: int, issue: IssueIn_Pydantic) -> Issue:
    await Issue.filter(id=issue_id).update(**issue.model_dump(exclude_unset=True))
    return await Issue_Pydantic.from_queryset_single(Issue.get(id=issue_id))


@router.delete('/issue/{id_}', response_model=Status)
async def delete_issue(issue_id: int) -> str:
    await Issue.filter(id=issue_id).delete()
    return Status(message=f"Deleted issue {issue_id}")
