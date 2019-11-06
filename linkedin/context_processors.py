
import requests
from .models import User


def add_variable_to_context(request):
    if 'user_id' in request.session:
        users_id = request.session['user_id']
        user = User.objects.get(id=users_id)
        return {
            'avatar': user.avatar
        }
    else:
        return {
            'avatar': ""
        }


