from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey("users.Register", on_delete=models.CASCADE,blank=True, null=True,related_name='products')

    def __str__(self):
        return self.name
    

    