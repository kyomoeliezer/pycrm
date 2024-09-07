from django.db import models

# Create your models here.
class BaseDB(models.Model):
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey("auths.User", on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Company(BaseDB):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Category(BaseDB):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name


class SubCategory(BaseDB):
    name = models.CharField(max_length=300)
    category=models.ForeignKey("core.Category", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Location(BaseDB):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name