

from django.shortcuts  import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import requests

from django.conf import settings
from accounts.models import Account
from tablib import Dataset
from import_export import resources
from .resources import AccountResource
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required




@login_required
def accounts(request):
    user_id = request.user.id
    accounts = Account.objects.filter(user_ac=user_id)
    return render(request, 'accounts/accounts.html', {'lists': accounts})


@login_required
def import_data(request):
    if request.method == 'POST':
        # data = {
        #     'key' : request.user
        # }
        try:
            # print(request.user.id)
            person_resource = AccountResource(request=request)
            dataset = Dataset()
            new_persons = request.FILES['myfile']
            imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')

            result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
            # print('dddddddddddddddddddddddddddddddddddddddddddddd')
            # print(result)
            # print('dddddddddddddddddddddddddddddddddddddddddddddd')
        except Exception as e:
            print(type(e))

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
            return redirect('accounts')
        else:
            return render(request, 'import/import.html')



    else:
        return render(request, 'import/import.html')

