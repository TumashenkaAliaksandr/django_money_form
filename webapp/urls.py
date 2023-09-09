from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from django_money_form import settings
from webapp import views
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('process_payment/', views.process_payment, name='process_payment'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
