from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Issue(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30)
    deadline = fields.DateField()

    def __str__(self) -> str:
        return self.name
    

Issue_Pydantic = pydantic_model_creator(Issue, name='Issue')
IssueIn_Pydantic = pydantic_model_creator(Issue, name="IssueIn", exclude_readonly=True)
