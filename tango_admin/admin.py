"""
Overrides Django contrib groups and sites for more control.

Note that model-level changes to these django.contrib apps
are made in tango_admin.models.
"""
from django import forms
from django.contrib import admin
#from django.contrib.auth.admin import GroupAdmin
#from django.contrib.auth.models import Group
#from django.contrib.sites.admin import SiteAdmin
#from django.contrib.sites.models import Site

from .models import Blacklist

"""
class CustomGroupAdmin(GroupAdmin):
    # Custom Groups admin: Adds "description" field to list display
    list_display = GroupAdmin.list_display + ('description',)


class CustomSiteAdmin(SiteAdmin):
    # Custom Site admiN: Adds fields to list display.
    list_display = SiteAdmin.list_display + ('description',)
"""


class BlackListAdmin(admin.ModelAdmin):
    list_display = ['user', 'blacklister', 'reason', 'date']


class TextCounterWidget(forms.Textarea):
    """
    Used for textAreas that need to count their characters
    """

    def render(self, name, value, attrs=None):
        if attrs:
            attrs['data-counter'] = 'needs_counter'
        else:
            attrs = {'data-counter': 'needs_counter'}
        return super(TextCounterWidget, self).render(name, value, attrs)


#admin.site.unregister(Site)
#admin.site.unregister(Group)
#admin.site.register(Site, CustomSiteAdmin)
#admin.site.register(Group, CustomGroupAdmin)

admin.site.register(Blacklist, BlackListAdmin)
