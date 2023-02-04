from .models import MyUser

class CustomBackend:
    """
    Custom authentication backend.
    Allows users to log in using their email address.
    """

    def authenticate(self, email):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = MyUser.objects.get(email=email)
            if user:
                print("authenticated!")
                return user
            print("failed!")
            return None
        except:
            print("error failed!")
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return MyUser.objects.get(pk=user_id)
        except:
            return None


