# Generated by Django 5.0.7 on 2024-08-02 12:28

import django.core.validators
import django.db.models.deletion
import seetha.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[seetha.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[seetha.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField(validators=[seetha.models.validate_date])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.DecimalField(decimal_places=2, max_digits=50, validators=[seetha.models.validate_amount])),
                ('terms_accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CarLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('car_loan_type', models.CharField(blank=True, choices=[('NEW', 'New'), ('USED', 'Used')], max_length=4, null=True)),
                ('car_vehicle_no', models.CharField(blank=True, max_length=15, null=True)),
                ('car_company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('variant', models.CharField(blank=True, max_length=50, null=True)),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('car_purchase_value_in_RS', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quotation_valaue_on_ex_showroom', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('downpayment_amount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('pan_card_number', models.CharField(max_length=10, unique=True)),
                ('aadhar_card_number', models.CharField(max_length=12, unique=True)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], max_length=1)),
                ('email_id', models.EmailField(max_length=254)),
                ('current_address', models.TextField()),
                ('current_address_pincode', models.IntegerField()),
                ('aadhar_address', models.TextField()),
                ('aadhar_pincode', models.IntegerField()),
                ('running_emis_amount_per_month', models.DecimalField(decimal_places=2, max_digits=15)),
                ('income_source', models.CharField(blank=True, choices=[('Job', 'Job'), ('Business', 'Business')], max_length=10, null=True)),
                ('net_salary_per_month', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('job_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('job_joining_date', models.DateField(blank=True, null=True)),
                ('business_name', models.CharField(max_length=200)),
                ('business_type', models.CharField(choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Partnership', 'Partnership'), ('Private Limited Company', 'Private Limited Company'), ('Public Limited Company', 'Public Limited Company'), ('LLP', 'Limited Liability Partnership'), ('Others', 'Others')], max_length=50)),
                ('net_income_per_month', models.DecimalField(decimal_places=2, max_digits=15)),
                ('business_establishment_date', models.DateField()),
                ('gst_certificate', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('nature_of_business', models.CharField(max_length=200)),
                ('turnover_in_lakhs_per_year', models.DecimalField(decimal_places=2, max_digits=15)),
                ('business_address', models.TextField()),
                ('business_address_pincode', models.IntegerField()),
                ('required_loan_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ref_1_person_name', models.CharField(max_length=100)),
                ('ref_1_person_mobile_number', models.CharField(max_length=15)),
                ('ref_2_person_name', models.CharField(max_length=100)),
                ('ref_2_person_mobile_number', models.CharField(max_length=15)),
                ('own_house', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('remarks', models.TextField()),
                ('application_id', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarLoanDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_rc_front', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('car_rc_back', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('aadhaar_card_front', models.ImageField(upload_to='documents/')),
                ('aadhaar_card_back', models.ImageField(upload_to='documents/')),
                ('pan_card', models.ImageField(upload_to='documents/')),
                ('customer_photo', models.ImageField(upload_to='documents/')),
                ('payslip1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('payslip2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('payslip3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('bank_statement', models.FileField(upload_to='documents/')),
                ('employee_id_card', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('business_proof_1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('business_proof_2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('latest_12_months_bank_statement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('business_office_photo', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('latest_3_yrs_itr_1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('latest_3_yrs_itr_2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('latest_3_yrs_itr_3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('current_address_proof', models.FileField(upload_to='documents/')),
                ('existing_loan_statement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document_1', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document_2', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document_3', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('other_document_4', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('showroom_quotation', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('downpayment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('quotation_value_on_ex_showroom', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('loan_type', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='CarLoandocuments', to='seetha.carloan')),
            ],
        ),
    ]
