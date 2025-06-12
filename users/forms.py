from django.contrib.auth.forms import UserChangeForm as DefaultChangeForm
from django.contrib.auth.forms import \
    UserCreationForm as DefaultUserCreationForm

from .models import User


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

class UserChangeForm(DefaultChangeForm):
    class Meta:
        model = User
        fields = '__all__'
