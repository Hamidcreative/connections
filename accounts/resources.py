
from accounts.models import Account

from import_export.fields import Field
import requests
from linkedin.models import User
from import_export import resources, widgets, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


class AccountResource(resources.ModelResource):
    name = Field(attribute='name', column_name='First Name') # will add about column value into avatar
    about = Field(attribute='about', column_name='Position') # will add about column value into avatar
    user = {}

    def __init__(self, *args, **kwargs):

        if 'request' in kwargs:
            self.user = kwargs['request'].user
            kwargs.pop('request', None)
            super(AccountResource, self).__init__(*args, **kwargs)

    def before_import_row( self, row, **kwargs):

        print('userddddddddddddddddddddddddddddddddddd')
        print(self.user)
        print('userddddddddddddddddddddddddddddddddddd')
        if self.user:
            row['user_ac'] = self.user.id
        else:
            row['user_ac'] = kwargs['user'].id


    class Meta:
        model = Account
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','created_at','updated_at','status')
        import_id_fields = ('name',)
        fields  = ('user_ac','name','avatar','followers','type','about')

    def dehydrate_name(self, accout):
        return  accout.name + accout.about







