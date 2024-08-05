"""
URL configuration for dhproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
<<<<<<< HEAD

=======
from django.contrib import admin
>>>>>>> origin/master
from django.urls import path
from seetha.views import *

urlpatterns = [
<<<<<<< HEAD
=======
    # path("admin/", admin.site.urls),
>>>>>>> origin/master
    path('car-loan-application/',apply_for_car_loan,name='car-laon-application'),
    path('document/',upload_documents,name="upload-documents"),
    path('carbasicdetail/',carbasicdetails,name="carbasicdetail"),

    path('car-loans-lists/',car_loan_list, name='car_loan_list'),
]
