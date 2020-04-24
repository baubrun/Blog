from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
        }