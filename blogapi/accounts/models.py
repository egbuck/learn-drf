from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Custom user model that extends the default Django user model. """
    pass
    # Add any additional fields here

    def __str__(self):
        return self.username