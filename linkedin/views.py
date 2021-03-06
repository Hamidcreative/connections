

from django.shortcuts  import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import requests
from .models import User
from django.conf import settings
from posts.models import Post
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required





class Login(TemplateView):
    template_name = 'login.html'

def login(request):
        return render(request, 'login.html')

def call_back(request):
    codes = request.GET.get('code')
    # live
    redirect_utl ="http://ec2-18-191-150-229.us-east-2.compute.amazonaws.com:8000"
    client_id    =   "81640v7palq8pd"
    client_secret  = "NrEP6PzssbMogU7t"
    # local
    # redirect_utl = "http://127.0.0.1:8000"  # local
    # client_id    =  "81q98zzq4ysq9p"
    # client_secret = "9KxQQ9qpPQlQ6Lj2"

    res = requests.post("https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&client_id="+client_id+"&redirect_uri="+redirect_utl+"/call_back/&client_secret="+client_secret+"&code="+codes)
    token = res.json()
    ac_token = token['access_token']
    users_datas = requests.get("https://api.linkedin.com/v2/me/?oauth2_access_token="+ac_token+"&projection=(id,firstName, useremail,lastName,profilePicture(displayImage~:playableStreams))")
    users_details  =  users_datas.json()
    linkedin_id    = users_details['id']
    firstName    = users_details['firstName']['localized']['en_US']
    lastName     = users_details['lastName']['localized']['en_US']
    avatar       = users_details['profilePicture']['displayImage~']['elements'][1]['identifiers'][0]['identifier']
    users_emails = requests.get("https://api.linkedin.com/v2/emailAddress?oauth2_access_token="+ac_token+"&q=members&projection=(elements*(handle~))")
    email        = users_emails.json();
    usere_mail   = email['elements'][0]['handle~']['emailAddress'];

    if User.objects.filter(email=usere_mail).exists():
        user = User.objects.get(email=usere_mail)
        user.first_name = firstName
        user.last_name  = lastName
        user.avatar     = avatar
        user.ac_token   = ac_token
        user.linkedin_id   = linkedin_id
        user.save()
        auth_login(request, user)
        request.session['user_id'] = user.id
        return HttpResponseRedirect("/dashboard")
    else:
        user = User.objects.create_user(usere_mail, usere_mail, 'johnpassword')
        user.first_name = firstName
        user.last_name  = lastName
        user.avatar     = avatar
        user.ac_token   = ac_token
        user.linkedin_id   = linkedin_id
        user.save()
        auth_login(request, user)
        request.session['user_id'] = user.id
        return HttpResponseRedirect("/plans")

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def addpost(request):
    return render(request, 'addpost.html')

@login_required
def savepost(request):
    if request.method == 'POST':
        title   = request.POST.get("title", "")
        #message = request.POST.get("message", "")
        message = request.POST.get("message", "")
        if request.user.id:
            users_id = request.user.id
            user = User.objects.get(id=users_id)
            ac_token = user.ac_token
            linkedin_id = user.linkedin_id
            if request.POST.get('sent_on'):
                post_obj = Post()
                sent_on = request.POST.get('sent_on')
                user = User.objects.get(id=users_id)
                post_obj.content = message
                post_obj.title = title
                post_obj.author = user
                post_obj.sent_on = sent_on
                post_obj.type = 0  # personal profile =0 = page = 2 group = 3
                post_obj.status = 0  # pending 0 sent 1
                post_obj.save()
                return render(request, 'dashboard.html')
            else:
                api_url = "https://api.linkedin.com/v2/ugcPosts"
                #"author": "urn:li:person:" + linkedin_id,
                #"author": "urn:li:organization:" + linkedin_id,

                post_data = {
                    "author": "urn:li:person:"+linkedin_id,
                    "lifecycleState": "PUBLISHED",
                    "specificContent": {
                        "com.linkedin.ugc.ShareContent": {
                            "shareCommentary": {
                                "text": message
                            },
                            "shareMediaCategory": "NONE"
                        },
                    },
                    "visibility": {
                        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                    },
                }
                headers = {'X-Restli-Protocol-Version': '2.0.0',
                           'Content-Type': 'application/json',
                           'Authorization': f'Bearer {ac_token}'}
                response = requests.post(api_url, headers=headers, json=post_data)
                if response.status_code == 201:
                    print("Success")
                    post_obj = Post()
                    user = User.objects.get(id=users_id)
                    post_obj.content = message
                    post_obj.title = title
                    post_obj.author = user
                    post_obj.type = 0  # personal profile =0 = page = 2 group = 3
                    post_obj.status = 1  # sent
                    post_obj.save()
                    return render(request, 'dashboard.html')
                else:
                    print(response.content)
                    return render(request, 'addpost.html')
        else:
            return render(request, 'login.html')
    return render(request, 'addpost.html')

@login_required
def plans(request):
    return render(request, 'plans.html')

@login_required
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
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'logout.html')
