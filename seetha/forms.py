from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.db.models import Q




class CarLoanApplicationForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = CarLoan
        fields = '__all__'
        #exclude=['application_id']
        
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'job_joining_date': forms.DateInput(attrs={'type': 'date'}),
            'business_establishment_date': forms.DateInput(attrs={'type': 'date'}),
            'pan_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control'}),
            'aadhar_address': forms.Textarea(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'net_salary_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'net_income_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
            'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
            'existing_loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'ref1_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref1_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ref2_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    
    def clean_aadhaar_card_number(self):
        aadhaar_number = self.cleaned_data.get('aadhaar_card_number')
        if len(aadhaar_number) != 12 or not aadhaar_number.isdigit():
            raise forms.ValidationError("Aadhaar number must be 12 digits.")
        return aadhaar_number

    # def clean_mobile_number(self):
    #     mobile_number = self.cleaned_data.get('mobile_number')
    #     if len(mobile_number) != 10 or not mobile_number.isdigit():
    #         raise forms.ValidationError("Mobile number must be 10 digits.")
    #     return mobile_number

    # def clean_email_id(self):
    #     email_id = self.cleaned_data.get('email_id')
    #     if not forms.EmailField().clean(email_id):
    #         raise forms.ValidationError("Invalid email format.")
    #     return email_id

    # def clean_model_year(self):
    #     model_year = self.cleaned_data.get('model_year')
    #     if model_year and (model_year < 1900 or model_year > 9999):
    #         raise forms.ValidationError("Model year must be a 4-digit year.")
    #     return model_year

    # def clean_current_address_pincode(self):
    #     pincode = self.cleaned_data.get('current_address_pincode')
    #     if len(pincode) != 6 or not pincode.isdigit():
    #         raise forms.ValidationError("Pincode must be 6 digits.")
    #     return pincode

    # def clean_aadhaar_pincode(self):
    #     pincode = self.cleaned_data.get('aadhaar_pincode')
    #     if len(pincode) != 6 or not pincode.isdigit():
    #         raise forms.ValidationError("Aadhaar pincode must be 6 digits.")
    #     return pincode

    # def clean_required_loan_amount(self):
    #     return self.clean_decimal_field('required_loan_amount')

    # def clean_car_purchase_value(self):
    #     return self.clean_decimal_field('car_purchase_value')

    # def clean_downpayment_amount(self):
    #     return self.clean_decimal_field('downpayment_amount')

    # def clean_existing_loan_amount(self):
    #     return self.clean_decimal_field('existing_loan_amount')

    # def clean_quotation_value_on_ex_showroom(self):
    #     return self.clean_decimal_field('quotation_value_on_ex_showroom')

    # def clean_showroom_quotation(self):
    #     return self.clean_file_field('showroom_quotation')

    # def clean_turnover_in_lakhs_per_year(self):
    #     return self.clean_decimal_field('turnover_in_lakhs_per_year')

    # def clean_net_salary_per_month(self):
    #     return self.clean_decimal_field('net_salary_per_month')

    # def clean_net_income_per_month(self):
    #     return self.clean_decimal_field('net_income_per_month')

    # def clean_running_emis_amount_per_month(self):
    #     return self.clean_decimal_field('running_emis_amount_per_month')

    # def clean_car_vehicle_no(self):
    #     vehicle_no = self.cleaned_data.get('vehicle_no')
    #     if vehicle_no and not re.match(r'^[A-Z0-9]{1,15}$', vehicle_no):
    #         raise forms.ValidationError("Car vehicle number must be in the correct format (e.g., ABC1234).")
    #     return vehicle_no

    # def clean_decimal_field(self, field_name):
    #     value = self.cleaned_data.get(field_name)
    #     if value and (value < 0 or len(str(value)) > 10):
    #         raise forms.ValidationError(f"{field_name.replace('_', ' ').title()} must be a valid number with up to 10 digits.")
    #     return value

    # def clean_file_field(self, field_name):
    #     file = self.cleaned_data.get(field_name)
    #     if file and file.size > 10 * 1024 * 1024:  # 10 MB limit
    #         raise forms.ValidationError(f"{field_name.replace('_', ' ').title()} file size must be under 10 MB.")
    #     return file


from django.utils.translation import gettext_lazy as _

class CarDocumentUploadForm(forms.ModelForm):
    class Meta:
        model = CarLoanDocument
        fields = '__all__'
        exclude = ['loan_type']
        labels = {
            'car_rc_front': 'Car Rc Front(JPEG)',
            'car_rc_back': 'Car Rc Back (JPEG)',
            'aadhar_card_front': 'Aadhar Card Front (JPEG)',
            'aadhar_card_back': 'Aadhar Card Back (JPEG)',
            'pan_card': 'PAN Card (JPEG)',
            'customer_photo': 'Customer Photo (JPEG)',
            'payslip1': 'Payslip 1 (PDF)',
            'payslip2': 'Payslip 2 (PDF)',
            'payslip3': 'Payslip 3 (PDF)',
            'bank_statement': 'Bank Statement (PDF)',
            'employee_id_card': 'Employee ID Card (JPEG)',
            'business_proof_1': 'Business Proof 1 (PDF)',
            'business_proof_2': 'Business Proof 2 (PDF)',
            'latest_12_months_bank_statement': 'Latest 12 Months Bank Statement (PDF)',
            'business_office_photo': 'Business Office Photo (JPEG)',
            'latest_3_yrs_itr_1': 'Latest 3 Years ITR 1 (PDF)',
            'latest_3_yrs_itr_2': 'Latest 3 Years ITR 2 (PDF)',
            'latest_3_yrs_itr_3': 'Latest 3 Years ITR 3 (PDF)',
            'current_address_proof': 'Current Address Proof (PDF)',
            'existing_loan_statement': 'Existing Loan Statement (PDF)',
            'other_document_1': 'Other Document 1 (PDF)',
            'other_document_2': 'Other Document 2 (PDF)',
            'other_document_3': 'Other Document 1 (PDF)',
            'other_document_4': 'Other Document 2 (PDF)',
            'showroom_quotation': 'Showroom Quotation (PDF)',
            # 'downpayment_amount': 'Downpayment Amount',
            # 'quotation_value_on_ex_showroom': 'Quotation Value on Ex-showroom',
        }

    def clean_aadhar_card_front(self):
        file = self.cleaned_data.get('aadhar_card_front', False)
        if file:
            if not file.name.endswith('.jpg') and not file.name.endswith('.jpeg') and not file.name.endswith('.png') :
                raise ValidationError(_('Only JPG/JPEG files are allowed.'), code='invalid')
        return file
class carBasicDetailForm(forms.ModelForm):
    random_number = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = carbasicdetailform
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

        # Check for previous applications within the last three months
        three_months_ago = timezone.now() - timedelta(days=90)
        recent_applications = carbasicdetailform.objects.filter(
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
       

