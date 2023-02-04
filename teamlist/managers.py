from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, first_name, last_name, phone, admin):
        """
        Create and save a user with the given email and password.
        """ 
        if not email or not first_name or not last_name or not phone or not admin:
            raise ValueError(_("All values are required"))
        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, admin=admin)
        user.save()
        return user

    
    def create_superuser(self, email, first_name, last_name, phone, admin):
        # create superuser here
        if not email or not first_name or not last_name or not phone or not admin:
            raise ValueError(_("All values are required"))
        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, admin=admin)
        user.save()
        return user