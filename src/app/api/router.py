from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any


router = APIRouter(prefix='/api')


issues = [
    {'id': 1, 'name': 'do something 1', 'deadline': '01.01.2024'},
    {'id': 2, 'name': 'do something 2', 'deadline': '02.02.2024'},
    {'id': 3, 'name': 'do something 3', 'deadline': '03.03.2024'},
]


@router.get('/issues')
def get_issues() -> list[dict]:
    return issues


@router.get('/issues/{id_}')
def get_issue(issue_id: int) -> list[dict]:
    return [issue for issue in issues if issue.get('id') == issue_id]


class Issue(BaseModel):
    id: int
    name: str
    deadline: str


@router.post('/issues')
def add_issue(issues_list: list[Issue]) -> list[Any]:
    issues.extend(issues_list)
    return issues


@router.post('/issues/{id_}')
def edit_issue(issue_id: int, new_name: str) -> dict[str, Any]:
    issue = [issue for issue in issues if issue.get('id') == issue_id][0]
    issue['name'] = new_name
    return issue
