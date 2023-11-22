from tortoise import models, fields


class Issue(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=30)
    deadline = fields.DateField()

    def __str__(self) -> str:
        return self.name
