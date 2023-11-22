from uuid import UUID
import pydantic


class IssueSchema(pydantic.BaseModel):
    name: str
    deadline: str
    
    
class IssueGetSchema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
    deadline: str | None = pydantic.Field(None)
    
    
class IssueUpdateSchema(pydantic.BaseModel):
    name: str | None = pydantic.Field(None)
    deadline: str | None = pydantic.Field(None)
    