from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)#**OneToOneField is the similar to ForeignKey unique=True
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='default.jpg', upload_to='Profile_images', validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return f'{self.staff.username}-Profile'
    class Meta:
        verbose_name_plural = 'Profile'