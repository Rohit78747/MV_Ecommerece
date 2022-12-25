from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base', views.BASE, name='base'),

                  path('', views.Home, name='home'),
                  path('product/<slug:slug>', views.Product_Details, name='product_detail'),
                  path('404', views.Error404, name='404'),

                  # Account
                  path('account/my_account', views.My_Account, name='my_account'),
                  path('account/register', views.Register, name='register'),
                  path('account/login', views.Login, name='login')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
