from tortoise import models, fields


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True)
    
    class Meta:
        abstract = True
        
        
class TimeStampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
        
class BaseModel(IdMixin, TimeStampMixin):
    
    class Meta:
        abstract = True
        
        
class Category(BaseModel):
    name = fields.CharField(max_length=100)
    issues = fields.ManyToManyField('models.Issue', related_name='categories')
    
    class Meta:
        table = 'category'
    

class Issue(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=30)
    deadline = fields.DateField()
    author = fields.ForeignKeyField('models.User', related_name='issues')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        table = 'issue'


class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)
    
    class Meta:
        table = 'user'
        