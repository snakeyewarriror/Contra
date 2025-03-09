from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _t


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email: str, password: str, **other_fields):
        if not email.strip():
            raise ValueError(_t("Empty email. The email must be set."))
        
        user = self.model(
            email = self.normalize_email(email),
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user
    
    
    
    def create_superuser(self, email: str, password: str, **other_fields):
        
        must_be_true_field = {'is_staff', 'is_superuser', 'is_active'}

        for field in must_be_true_field:
            if field in other_fields and not other_fields[field]:
                raise ValueError(_t(f'Field {field} must be True or left alone'))
            other_fields[field] = True


        user = self.create_user(email, password, **other_fields)
        user.is_admin = True
        user.save()
        return user


