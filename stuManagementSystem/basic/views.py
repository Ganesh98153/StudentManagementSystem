from django.shortcuts import render, redirect
from basic import models
# Create your views here.
def index(request):
    return render(request, "basic/index.html")

def admin(request):
    return render(request, "basic/admin.html")

def admission(request):
    return render(request, "basic/admission.html")
    
def contact(request):
    return render(request, "basic/contact.html")

def admission_backend(request):
    if request.method == "POST":
        fname =  request.POST['firstName']
        lname = request.POST['lastName']
        fa_name = request.POST['fathersName']
        mo_name = request.POST['mothersName']
        grade_values = request.POST['gradeValue']
        reviews_ = request.POST['subject']

        adm = models.Admission_Student(first_name=fname, last_name=lname, father_name=fa_name, mothers_name=mo_name, grade_value=grade_values, review = reviews_)
        adm.save()
        print("data is save")
    return redirect(index)

