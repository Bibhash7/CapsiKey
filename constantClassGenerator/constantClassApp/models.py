import re
import logging
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinLengthValidator
logger = logging.getLogger(__name__)
from email_validator import validate_email, EmailNotValidError


# Create your models here.
def custom_email_validator(value):
    if not re.match(r'^[a-zA-Z][\w.-]+@gmail\.com$', value):
        logger.error("Enter a valid Gmail address that does not start with a digit.")
        print("Here")
        return False
    return True
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class LoggedUser(BaseModel):

    email = models.EmailField(
        unique=True,
        validators=[custom_email_validator],
        )
    password = models.CharField(max_length=250, validators=[MinLengthValidator(8)])
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def validate_password(self, entered_password):
        return check_password(entered_password, self.password)

    def __str__(self):
        return self.email