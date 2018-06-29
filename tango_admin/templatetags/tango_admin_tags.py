from django import template
from django.contrib.staticfiles.finders import AppDirectoriesFinder
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import resolve, reverse

register = template.Library()


@register.simple_tag
def tango_admin_css():
    """
    Inserts tango_admin css links.
    """
    appdirs = AppDirectoriesFinder()
    targets = []
    csslink = '<link rel="stylesheet" type="text/css" href="%s">'

    for app_name in appdirs.apps:
        app = app_name
        if '.' in app_name:
            oldpath, app = app_name.rsplit('.', 1)
        target = '%s/css/tango_admin.css' % app
        if appdirs.find_in_app(app_name, target):
            targets.append(target)

    return "\n".join(csslink % staticfiles_storage.url(x) for x in targets)


@register.inclusion_tag('admin/includes/app_list.html', takes_context=True)
def tango_admin_app_list(context):
    request = context['request']
    current_view = resolve(request.path)
    namespace = getattr(current_view, 'app_name', 'admin')

    # Ensure response has context data and apps.
    # Redirects don't, and neither do pages outside
    # an app context (lacking namespace), such as documentation pages
    try:
        index_url = reverse('%s:index' % namespace)
        index_view = resolve(index_url)
        template_response = index_view.func(request)
        app_list = template_response.context_data['app_list']
        current_app = template_response._current_app
    except Exception: # yeah, this is suppressing any error. We're living dangerously.
        app_list = []
        current_app = None

    return {
        'apps': app_list,
        'current_app': current_app,
        'path': request.path,
    }
