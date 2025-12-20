"""
URL configuration for katakara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from productApp.views import home, getProducts, addProduct, getProductById, editProduct, deleteProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("products/", getProducts, name='products'),
    path('add-product/', addProduct, name='add-product'),
    path('get-product/<int:id>/', getProductById, name='get-product'),
    path('edit-product/<int:id>/', editProduct, name='edit-product'),
    path('delete-product/<int:id>/', deleteProduct, name='delete-product'),
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)