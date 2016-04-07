from django.conf.urls import url
from . import views
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns = [
    url(r'^$', views.recruitment, name='recruitment'),
    url(r'^new$', views.recruitment_period_new, name='recruitment_period_new'),
    url(r'^(?P<pk>\d+)/delete$', views.recruitment_period_delete, name='recruitment_period_delete'),
    url(r'^(?P<pk>\d+)/application/new$', views.recruitment_application_new, name='recruitment_application_new'),

    url(r'^application/(?P<pk>\d+)$', views.recruitment_application_delete, name='recruitment_application_delete'),
    url(r'^application/(?P<pk>\d+)/interview$', views.recruitment_application_interview,
        name='recruitment_application_interview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
