from django.db import models
from django.core.validators import EmailValidator
import random
import string
import re
from django.core.exceptions import ValidationError
from django.utils import timezone



def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed.') 
    
def validate_pan(value):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid PAN number format')

def validate_mobile_number(value):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, value) and len(str(value))!=10:
        raise ValidationError('Invalid mobile number format')

def validate_aadhar_number(value):
    pattern = r'^\d{12}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid Aadhar number format')

def validate_pincode(value):
    pattern = r'^\d{6}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid pincode format')
    

def validate_accountnumber(value):
    pattern = r'^\d{12}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid account nymber format')
    
    
    

def validate_pincodes(value):
    if len(str(value)) != 6:
        raise ValidationError('Pincode must be 6 digits.')

def validate_amount(value):
    if len(str(value)) > 10:
        raise ValidationError('Amount must be 10 digits.')
    
def clean_aadhar_card_front(self):
        file = self.cleaned_data.get('aadhar_card_front', False)
        if file:
            if not file.name.endswith('.jpg') and not file.name.endswith('.jpeg'):
                raise ValidationError(('Only JPG/JPEG files are allowed.'), code='invalid')
        return file
def clean_business_proof_1(self):
        file = self.cleaned_data.get('business_proof_1', False)
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError(('Only PDF files are allowed.'), code='invalid')
        return file
def validate_image_file(value):
    if not (value.name.endswith('.jpg') or value.name.endswith('.png') or value.name.endswith('.jpeg')):
        raise ValidationError('Only JPG/JPEG files are allowed.')


def validate_pdf_file(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')
def validate_date(value):
    if value > timezone.now().date():
        raise ValidationError('Date cannot be in the future.')

class CreditCardApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-Employed', 'Self-Employed'),
        ('Unemployed', 'Unemployed'),
        ('Student', 'Student'),
        ('Retired', 'Retired'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('Current', 'Current'),
        ('Savings', 'Savings'),
    ]

    CARD_TYPE_CHOICES = [
        ('Standard', 'Standard'),
        ('Rewards', 'Rewards'),
        ('Travel', 'Travel'),
        ('Cashback', 'Cashback'),
        ('Business', 'Business'),
    ]

    PURPOSE_CHOICES = [
        ('Travel', 'Travel'),
        ('Business', 'Business'),
        ('Everyday Use', 'Everyday Use'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField(max_length=100, null=True,validators=[validate_only_letters])
    date_of_birth = models.DateField(validators=[validate_date])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='Single')
    nationality = models.CharField(max_length=50, null=True,validators=[validate_only_letters])

    # Address Details
    current_street_address = models.CharField(max_length=255, null=True)
    current_city = models.CharField(max_length=100,validators=[validate_only_letters],default='enter')
    current_state_province = models.CharField(max_length=100, default='Default Value',validators=[validate_only_letters])
    current_postal_code = models.CharField(max_length=6,null=True, blank=True,validators=[validate_pincode])  # Changed to CharField
    
    current_country = models.CharField(max_length=50, null=True, blank=True,validators=[validate_only_letters])

    permanent_street_address = models.CharField(max_length=255, null=True, blank=True)
    permanent_city = models.CharField(max_length=100, null=True, blank=True,validators=[validate_only_letters])
    permanent_state_province = models.CharField(max_length=100, null=True, blank=True,validators=[validate_only_letters])
    permanent_postal_code = models.CharField(max_length=6,null=True, blank=True,validators=[validate_pincode]) 
    
     
    permanent_country = models.CharField(max_length=50,null=True, blank=True,validators=[validate_only_letters])

    phone_number = models.CharField(max_length=10,null=True,validators=[validate_mobile_number])
    email_address = models.EmailField(validators=[EmailValidator()])



    # Employment Information
    employment_status = models.CharField(max_length=15, choices=EMPLOYMENT_STATUS_CHOICES, null=True,)
    occupation = models.CharField(max_length=100, blank=True,validators=[validate_only_letters])
    employer_name = models.CharField(max_length=100, blank=True,validators=[validate_only_letters])
    employer_address = models.CharField(max_length=255, blank=True)
    work_phone_number = models.CharField(max_length=10,null=True,validators=[validate_mobile_number])  # Changed to CharField
    years_at_current_job = models.PositiveIntegerField(blank=True, null=True)
    monthly_annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,validators=[validate_amount])

    # Financial Information
    bank_name = models.CharField(max_length=100, blank=True,validators=[validate_only_letters])
    account_number = models.CharField(null=True, blank=True,validators=[validate_accountnumber],max_length=12) # Changed to CharField
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, blank=True)
    monthly_housing_payment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,validators=[validate_amount])
    other_monthly_obligations = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,validators=[validate_amount])
    total_monthly_expenses = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,validators=[validate_amount])

    # Credit Information
    existing_credit_cards = models.IntegerField(blank=True, null=True)  # You may consider JSONField if structured data is needed
    other_debts_loans = models.IntegerField(blank=True)

    # Additional Information
    preferred_credit_card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES, blank=True,validators=[validate_only_letters])
    purpose_of_credit_card = models.CharField(max_length=20, choices=PURPOSE_CHOICES, blank=True,validators=[validate_only_letters])
    referral_code = models.CharField(max_length=50, blank=True)

    # Legal Agreements
    terms_and_conditions_agreed = models.BooleanField(default=False)
    privacy_policy_agreed = models.BooleanField(default=False)
    electronic_signature = models.CharField(max_length=25)
    # application_id=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return f"{self.full_name} - {self.email_address}"
    



# def save(self, *args, **kwargs):
#         if not self.random_number:
#             last_entry = CreditCardApplication.objects.filter(random_number__startswith='king').order_by('-random_number').first()
#             if last_entry:
#                 last_number = int(last_entry.random_number[4:])  
#                 new_number = last_number + 1
#             else:
#                 new_number = 1001
#             self.random_number = f"king{new_number:04d}" 

#         print(f"Saving PersonalDetail with random_number: {self.random_number}")
#         super(CreditCardApplication, self).save(*args,**kwargs)








class CreditDocumentUpload(models.Model):
    personal_details = models.ForeignKey(CreditCardApplication, on_delete=models.CASCADE)

    proof_of_identity = models.FileField(upload_to='proof_of_identity/', blank=True, null=True,
                                         help_text='Upload proof of identity such as a passport or driver’s license.',validators=[validate_pdf_file])
    proof_of_address = models.FileField(upload_to='proof_of_address/', blank=True, null=True,
                                        help_text='Upload proof of address such as a utility bill or lease agreement.',validators=[validate_pdf_file])
    proof_of_income = models.FileField(upload_to='proof_of_income/', blank=True, null=True,
                                       help_text='Upload proof of income such as payslips or tax returns.',validators=[validate_pdf_file])

    def __str__(self):
        return f"Documents for {self.proof_of_address}-{self.proof_of_income}"

def validate_only_letters(value):
    if not value.isalpha() and r'^\s{100}$':
        raise ValidationError('Only letters are allowed.')
    
def validate_pan(value):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid PAN number format')

def validate_mobile_number(value):
    
    if len(value)!=10 or not value.isdigit():
        raise ValidationError('Invalid mobile number format')

def validate_aadhar_number(value):
      # Convert the value to a string
    if len(value) != 12 or not value.isdigit():
        raise ValidationError('Invalid Aadhar number format. It should be exactly 12 digits and contain only numbers.')

def validate_pincode(value):
    pattern = r'^\d{6}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid pincode format')



def validate_amount(value):
    if len(str(value)) > 10:
        raise ValidationError('Amount must be lessthan 10 digits.')
    
def validate_date(value):
    if value  > timezone.now().date():
        raise ValidationError('Date should be in past or present')
    
def validate_gst_number(value):
    gst_regex = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')
    
    value_str = str(value)  # Convert the value to a string
    if not gst_regex.match(value_str):
        raise ValidationError('Invalid GST number format.')

def validate_age(value):
    # Ensure value is an integer and within the expected range
    if not (18 <= value <= 70):
        raise ValidationError('Apply between 18 and 70')

class crebasicdetailform(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    MARITAL_STATUS_CHOICES = [('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')]

    full_name = models.CharField(max_length=25,validators=[validate_only_letters])
    pan_number = models.CharField(max_length=10, validators=[validate_pan])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(validators=[EmailValidator()])
    date_of_birth = models.DateField(validators=[validate_date])
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='Single')
    required_loan_amount = models.DecimalField(max_digits=50, decimal_places=2,validators=[validate_amount])
    terms_accepted = models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    random_number = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    
   




