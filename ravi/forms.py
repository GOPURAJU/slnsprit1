from .models import *
from django.utils import timezone
from datetime import timedelta
from django import forms

class plBasicDetailForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = plbasicdetailform
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'loantype': forms.Select(attrs={'class': 'form-control'}),
            'pan_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'random_number': forms.HiddenInput(),
        }
        error_messages = {
            'full_name': {'required': 'Full name is required.'},
            'loantype':{'required':'this field is required'},
            'pan_number': {'required': 'Pan number is required.'},
            'gender': {'required': 'Gender is required.'},
            'email': {'required': 'Email is required.'},
            'date_of_birth': {'required': 'Date of birth is required.'},
            'marital_status': {'required': 'Marital status is required.'},
            'required_loan_amount': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }

    def clean(self):
        cleaned_data = super().clean()
        pan_number = cleaned_data.get('pan_number')

     
        three_months_ago = timezone.now() - timedelta(days=90)
        recent_applications = plbasicdetailform.objects.filter(
            pan_number=pan_number,
            created_at__gte=three_months_ago
        ).order_by('-created_at')

        if recent_applications.exists():
            most_recent_application = recent_applications.first()
            reapply_date = most_recent_application.created_at + timedelta(days=90)
            error_message = f"You have already applied within the last three months. Please reapply after {reapply_date.strftime('%Y-%m-%d')}."
            raise forms.ValidationError(error_message)

        return cleaned_data
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
    

class hlBasicDetailForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = hlbasicdetailform
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'required_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'terms_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'random_number': forms.HiddenInput(),
        }
        error_messages = {
            'full_name': {'required': 'Full name is required.'},
            'pan_number': {'required': 'Pan number is required.'},
            'gender': {'required': 'Gender is required.'},
            'email': {'required': 'Email is required.'},
            'date_of_birth': {'required': 'Date of birth is required.'},
            'marital_status': {'required': 'Marital status is required.'},
            'required_loan_amount': {'required': 'Required loan amount is required.'},
            'terms_accepted': {'required': 'You must accept the terms and conditions to proceed.'},
        }

    def clean(self):
        cleaned_data = super().clean()
        pan_number = cleaned_data.get('pan_number')

     
        three_months_ago = timezone.now() - timedelta(days=90)
        recent_applications = plbasicdetailform.objects.filter(
            pan_number=pan_number,
            created_at__gte=three_months_ago
        ).order_by('-created_at')

        if recent_applications.exists():
            most_recent_application = recent_applications.first()
            reapply_date = most_recent_application.created_at + timedelta(days=90)
            error_message = f"You have already applied within the last three months. Please reapply after {reapply_date.strftime('%Y-%m-%d')}."
            raise forms.ValidationError(error_message)

        return cleaned_data
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
class PersonalDetailForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = PersonalDetail
        fields = '__all__'
        widgets = {
             'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
             'job_joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = ['aadhar_card_front','aadhar_card_back','pan_card','customer_photo','payslip_1',
                  'payslip_2','payslip_3','bank_statement','employee_id_card','current_address_proof',
                  'other_document_1','other_document_2']
<<<<<<< HEAD
        

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control'}),
            'current_address_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_address': forms.Textarea(attrs={'class': 'form-control'}),
            'aadhar_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'running_emis_per_month': forms.TextInput(attrs={'class': 'form-control'}),
            'income_source': forms.Select(attrs={'class': 'form-control'}),
            
            # Job-related fields
            'net_salary_per_month': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_type': forms.Select(attrs={'class': 'form-control'}),
            'job_joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'total_job_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'work_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'office_address_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Business-related fields
            'net_income_per_month': forms.TextInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_type': forms.Select(attrs={'class': 'form-control'}),
            'business_establishment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gst_certificate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nature_of_business': forms.TextInput(attrs={'class': 'form-control'}),
            'turnover_per_year': forms.TextInput(attrs={'class': 'form-control'}),
            'business_address_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'house_plot_purchase_value': forms.TextInput(attrs={'class': 'form-control'}),
            'required_loan_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'existing_loan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'existing_loan_bank_nbfc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'existing_loan_amount': forms.TextInput(attrs={'class': 'form-control'}),

            # Co-Applicant Details
            'coapplicant_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'coapplicant_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'coapplicant_gender': forms.Select(attrs={'class': 'form-control'}),
            'coapplicant_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'coapplicant_relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'coapplicant_mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'coapplicant_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'coapplicant_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'coapplicant_net_income_per_month': forms.TextInput(attrs={'class': 'form-control'}),
        }
=======


class CustomerProfileForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = CustomerProfile
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'business_establishment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        def _init_(self, *args, **kwargs):
           super()._init_(*args, **kwargs)
           self.fields['have_gst_certificate'].label = "Do you have GST certificate?"
           self.fields['gst_number'].label = "GST Number(if available)"

>>>>>>> origin/master




class ApplicantDocumentForm(forms.ModelForm):
    class Meta:
        model = ApplicantDocument
        fields = '__all__'
        exclude = ['applicant_profile']
        widgets = {
            'adhar_card_front': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'adhar_card_back': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'pan_card': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'customer_photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'home_plot_photo_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'home_plot_photo_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'home_plot_photo_3': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'home_plot_photo_4': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'latest_3_months_banked_statement': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'latest_3_months_payslips_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'latest_3_months_payslips_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'latest_3_months_payslips_3': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'employee_id_card': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'business_proof_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'business_proof_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'latest_12_months_banked_statement': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'business_office_photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'latest_3_yrs_itr_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'latest_3_yrs_itr_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'latest_3_yrs_itr_3': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'current_address_proof': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'existing_loan_statement': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'other_documents_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'other_documents_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'other_documents_3': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'other_documents_4': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'co_adhar_card_front': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'co_adhar_card_back': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'co_pan_card': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'co_selfie_photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'random_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ApplicationVerificationForm(forms.ModelForm):
   
    class Meta:
        model=ApplicationVerification
        fields='__all__'
        exclude=['personal_detail']

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
       
        for field in self.fields:
            if not getattr(instance, field):
                setattr(instance, field, 'Rejected')
        
        if commit:
            instance.save()
        return instance
    
class HomeapplicationForm(forms.ModelForm):
   
    class Meta:
        model= HomeApplication
        fields='__all__'
        exclude=['applicant_profile']

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
       
        for field in self.fields:
            if not getattr(instance, field):
                setattr(instance, field, 'Rejected')
        
        if commit:
            instance.save()
        return instance
