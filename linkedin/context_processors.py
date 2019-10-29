
import requests
from .models import User


def add_variable_to_context(request):

    return {
        'testme': 'Hello world!'
    }