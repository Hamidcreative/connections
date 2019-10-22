

from django.shortcuts  import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import requests
from .models import User
from django.conf import settings





class Login(TemplateView):
    template_name = 'login.html'

def login(request):
        return render(request, 'login.html')

def call_back(request):
    codes = request.GET.get('code')
    res = requests.post("https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&client_id=77022qk4cbxhhw&redirect_uri=http://127.0.0.1:8000/call_back/&client_secret=0xxQLFbzRNqFboAS&code="+codes)
    token = res.json()
    ac_token = token['access_token']
    users_datas = requests.get("https://api.linkedin.com/v2/me/?oauth2_access_token="+ac_token+"&projection=(id,firstName, useremail,lastName,profilePicture(displayImage~:playableStreams))")
    users_details  =  users_datas.json()
    firstName  = users_details['firstName']['localized']['en_US']
    lastName   = users_details['lastName']['localized']['en_US']
    avatar     = users_details['profilePicture']['displayImage~']['elements'][1]['identifiers'][0]['identifier']
    users_emails = requests.get("https://api.linkedin.com/v2/clientAwareMemberHandles?oauth2_access_token="+ac_token+"&q=members&projection=(elements*(handle~))")
    email = users_emails.json();
    usere_mail = email['elements'][0]['handle~']['emailAddress'];
    if User.objects.filter(email=usere_mail).exists():
        return HttpResponseRedirect("/dashboard")
    else:
        user = User.objects.create_user(usere_mail, usere_mail, 'johnpassword')
        user.first_name = firstName
        user.last_name  = lastName
        user.avatar = avatar
        user.save()
        return HttpResponseRedirect("/plans")
def dashboard(request):
    return render(request, 'dashboard.html')

def plans(request):
    return render(request, 'plans.html')

def payment(request):
    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    return render(request, 'payment.html')

def connections(request):
    return render(request, 'connections.html')

def campaigns(request):
    return render(request, 'campaigns.html')

def messages(request):
    return render(request, 'messages.html')

def logout(request):
    return render(request, 'logout.html')
