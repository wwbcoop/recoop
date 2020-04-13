# django
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
# project
from apps.initiative.views import InitiativeCreate
from apps.contact.views import ContactView

urlpatterns = [
    # Admin
    path(
        'admin',
        admin.site.urls
    ),
    # i18n
    path(
        'i18n',
        include('django.conf.urls.i18n')
    ),
    # ckeditor urls
    path(
        r'ckeditor/',
        include('ckeditor_uploader.urls')
    ),
    # registration
    path(
        'accede',
        auth_views.LoginView.as_view(
            template_name='pages/page-login.html'
        ),
        name='login'
    ),
    path(
        'logout',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    # Robots
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        ),
        name="robots"
    ),
]

urlpatterns += i18n_patterns(
    # Frontpage
    path(
        '',
        TemplateView.as_view(
            template_name='pages/page-front.html'
        ),
        name="front"
    ),
    # Contact
    path(
        'contacta',
        ContactView.as_view(
            template_name='pages/page-contact.html'
        ),
        name="contact"
    ),
    # Apply
    path(
        'solicita',
        InitiativeCreate.as_view(
            template_name='pages/page-apply.html'
        ),
        name="apply"
    ),
)

if settings.DEBUG == True:
  urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
  urlpatterns += static( settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT )
