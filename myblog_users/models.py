from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #**OneToOneField is the similar to ForeignKey unique=True
    image = models.ImageField(default='default.jpg', upload_to='profile',
                              validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return self.user.username