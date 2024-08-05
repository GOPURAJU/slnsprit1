<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path,include
>>>>>>> origin/master
from .views import *



urlpatterns = [
<<<<<<< HEAD
    path('demo',apply_for_business_loan,name="demo"),
=======
   
    path('',apply_for_business_loan,name="demo"),
>>>>>>> origin/master
    path('document',upload_documents,name="upload-documents"),
    path('insurance',insuranceForm,name="insurance"),
    path('business-loans-lists/', business_loan_list, name='business_loan_list'),
    path('business-loan-update/<str:application_id>',business_loan_update,name='business-loan-update'),
    path('business-loan-view/<str:id>',business_loan_view,name='business-loan-view'),
    path('document-upload/<str:application_id>',update_business_loan_document,name='update-documents'),
    path('application-flow/<str:application_id>',applicationVerification,name='applicationFlow'),
    path('view-document/<str:application_id>',documentsView,name='documents-view'),
    path('update-verification/<str:application_id>',update_verification,name="update-verification"),
    path('customerProfile/<str:application_id>',customerProfile,name="buscustomer-profile"),
<<<<<<< HEAD
    path('busbasicdetail/',busbasicdetails,name='busbasicdetail'),
=======
                path('busbasicdetail/',busbasicdetails,name='busbasicdetail'),
>>>>>>> origin/master

]
