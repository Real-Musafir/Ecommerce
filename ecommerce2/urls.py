"""ecommerce2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from products import views
from carts import views as cart_views
from orders import views as order_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('s/',views.search, name='search'),
    path('products/',views.all, name='products'),
    path('cart/',cart_views.view, name='cart'),
    path('checkout/',order_views.checkout, name='checkout'),
    path('orders/',order_views.orders, name='user_orders'),
    #path('^products/(?P<slug>.*)/$',views.single, name='single_product'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', views.single, name='single_product'),
    re_path(r'^cart/(?P<id>\d+)/$', cart_views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^cart/(?P<slug>[\w-]+)/$', cart_views.add_to_cart, name='add_to_cart'),

    
    path('accounts/logout/', account_views.logout_view , name='auth_logout' ),
    path('accounts/login/', account_views.login_view , name='auth_login' ),
    path('accounts/register/', account_views.registration_view , name='auth_register' ),

    re_path(r'^accounts/activate/(?P<activation_key>\w+)/$', account_views.activation_view , name='activation_view'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)