from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
import re
from datetime import datetime
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=75, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                            '@/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                              _('Enter a valid username.'), 'invalid')
                                ])
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.CharField(max_length=200, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=datetime.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = "user"

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email
