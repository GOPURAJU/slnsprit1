from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import *

def demo(request):
    return HttpResponse("hi Your Project Working Fine")
def carbasicdetails(request):
    form = carBasicDetailForm()

    if request.method == 'POST':
        form = carBasicDetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('car-laon-application') 
        
    return render(request, 'carbasicdetail.html',{'form':form})

def apply_for_car_loan(request):
    # print("View function called")
    if request.method == 'POST':
        form = CarLoanApplicationForm(request.POST)
        if form.is_valid():
            # print("Form is valid")  # Debugging statement
            # form.save()
            carObj=form.save()
            request.session['car_id']=carObj.id
            return redirect('upload-documents')
        else:
            print(form.errors)
            return render(request,'apply_for_car_loan.html',{'form': form})
       
    else:
        form = CarLoanApplicationForm()
    
    return render(request, 'apply_for_car_loan.html', {'form': form})


def upload_documents(request):
    if request.method == 'POST':
        if request.session.get('car_id'):
            loanid = request.session.get('car_id')
            print(loanid)
            loanObj = get_object_or_404(CarLoan, id=loanid)

            form = CarDocumentUploadForm(request.POST, request.FILES)

            if form.is_valid():
                docObj = form.save(commit=False)
                docObj.loan = loanObj
                docObj.save()
                return HttpResponse('Created Document with Application Id of - {}'.format(loanObj.application_id))
            else:
                # If the form is not valid, re-render the form with errors
                print(form.errors)
                return HttpResponse("invalid")
    else:
        form = CarDocumentUploadForm()
    
    return render(request, 'Car_upload_documents.html', {'form': form})



def car_loan_list(request):
    car_loans = CarLoan.objects.all()
    return render(request, 'car_loan_list.html', {'car_loans': car_loans})

def car_loan_update(request,application_id):
    loan = get_object_or_404(CarLoan, application_id=application_id)
    print(loan)
    if request.method == 'POST':
        form = CarLoanApplicationForm(request.POST, instance=loan,instance_id=loan.id)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated')
        else:
            print(form.errors)
            return render(request, 'car_loan_update.html', {'form': form})

    else:
        form = CarLoanApplicationForm(instance=loan)
    return render(request, 'car_loan_update.html', {'form': form})
