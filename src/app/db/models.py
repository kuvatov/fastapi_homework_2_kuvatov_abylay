from tortoise import models, fields


class Issue(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    deadline = fields.DateField()
    