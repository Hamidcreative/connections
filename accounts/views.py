

from django.shortcuts  import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import requests

from django.conf import settings
from accounts.models import Account





def accounts(request):
    return render(request, 'accounts/accounts.html')

