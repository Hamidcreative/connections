


from django.shortcuts  import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import requests
from linkedin.models import User
from django.conf import settings
from posts.models import Post
from tablib import Dataset
from datetime import datetime
from accounts.resources import UpdateResource
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from linkedin.templatetags import custom_tags


@login_required
def updates(request):
    user_id = request.user.id
    posts = Post.objects.filter(author=user_id)
    return render(request, 'updates/updates.html', {'lists': posts})


@login_required
def import_posts(request):
    if request.method == 'POST':
        # data = {
        #     'key' : request.user
        # }
        try:
            person_resource = UpdateResource(request=request)
            dataset = Dataset()
            new_persons = request.FILES['myfile']
            imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')
            result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        except Exception as e:
            print(type(e))
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
            return redirect('updates')
        else:
            return render(request, 'updates/import.html')
    else:
        return render(request, 'updates/import.html')