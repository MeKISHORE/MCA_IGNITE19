from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse


from.import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('regstudent', views.regstudent, name='regstudent'),
    path('login', views.login, name='login'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('team_ignite', views.team_ignite, name='team_ignite'),
    path('teams', views.team, name='team'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('gallery', views.gallery, name='gallery'),
    path('event', views.event, name='event'),
    path('event/<slug:slug>', views.event_detail, name='event_data'),
    path('team_nitk/<slug:slug>', views.team_image, name='team_image'),
    path('contact', views.contact, name='contact'),
    path('contact_reg', views.contact_reg, name='contact_reg'),
    # path('basic', views.basic, name='basic'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('media_cover', views.media_cover, name='media_cover'),
    path('headndmentors', views.headndmentors, name='headndmentors'),
    path('score/<str:user_name>/<str:score_pass>/<str:score_mail>/<str:colleg>', views.reg_game, name='reg_game'),
    path('log/<str:user_mail>/<str:score_pass>', views.log, name='log'),
    path('updte/<str:user_mail>/<str:score_pass>/<str:score_update>', views.updte, name='updte'),
    path('show/', views.show, name='show'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
