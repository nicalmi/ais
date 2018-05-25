from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.companies_customers_list, name = 'companies_customers_list'),
	url(r'^mine$', views.companies_customers_list_mine, name = 'companies_customers_list_mine'),
	url(r'^slack_call$', views.companies_slack_call, name = 'companies_slack_call'),
	url(r'^statistics$', views.companies_customers_statistics, name = 'companies_customers_statistics'),
	url(r'^link$', views.companies_customers_link, name = 'companies_customers_link'),
	url(r'^groups$', views.companies_customers_groups, name = 'companies_customers_groups'),
	url(r'^groups/new$', views.companies_customers_groups, name = 'companies_customers_groups_new'),
	url(r'^groups/(?P<pk>\d+)$', views.companies_customers_groups, name = 'companies_customers_groups_edit'),
	url(r'^(?P<pk>\d+)$', views.companies_customers_view, name = 'companies_customers_view'),
	url(r'^(?P<pk>\d+)/edit$', views.companies_customers_edit, name = 'companies_customers_edit'),
	url(r'^(?P<pk>\d+)/edit/group/(?P<group_pk>\d+)$', views.companies_customers_edit, name = 'companies_customers_edit_toggle_group'),
	url(r'^(?P<pk>\d+)/edit/responsible/(?P<responsible_group_pk>\d+)$', views.companies_customers_edit, name = 'companies_customers_edit_toggle_responsible'),
	url(r'^(?P<pk>\d+)/edit/responsible/(?P<responsible_group_pk>\d+)/remove$', views.companies_customers_remove, name = 'companies_customers_edit_remove_responsible'),
	url(r'^(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/edit$', views.companies_customers_comment_edit, name = 'companies_customers_comment_edit'),
	url(r'^(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/remove$', views.companies_customers_comment_remove, name = 'companies_customers_comment_remove'),
]
