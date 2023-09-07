from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from django_money_form import settings
from webapp.views import index

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
