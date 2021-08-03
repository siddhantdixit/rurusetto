from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rulesets/', views.listing, name='listing'),
    path('new/', views.create_ruleset, name='create_ruleset'),
    path('changelog/', views.changelog, name='changelog'),
    path('rulesets/<slug:slug>', views.wiki_page, name='wiki'),
    path('rulesets/<slug:slug>/edit', views.edit_ruleset_wiki, name='edit_wiki'),
]