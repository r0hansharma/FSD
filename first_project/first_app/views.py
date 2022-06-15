# from typing_extensions import Self
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from first_app.models import Degree, Student
from django.db.models import Q
from django.template import loader

from .forms import DegreeForm, SearchForm, StudentsForm
import json

def index(request) :    # 'request' name is convention. It can be some other name too.
    degree_values = Degree.objects.all()
    students_values = Student.objects.all()
    my_dict = {'degree_rows' : degree_values, 'students_rows' : students_values,}
    # my_dict = { 'inject_var' : "This is an injected content"}
    return render(request,'index.html',context=my_dict)

def help(request) :
    return render(request,'help.html')

# def forms(request) :
#     return render(request,'forms.html')

def get_degree(request):
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = DegreeForm(request.POST, request.FILES)   # create a form instance and populate it with data from the request:
    if form.is_valid():                         # check whether it's valid:
      title = form.cleaned_data['title']        # process the data in form.cleaned_data as required
      branch = form.cleaned_data['branch']
      print(title, branch)

      d = Degree(title=title, branch=branch)    # write to the database
      d.save()

      # Retrieve the json file and process here
      f = request.FILES['file']          # open the json files - get file handle
      data = json.load(f)
      for deg in data['degree']:         # iterate through the degree list
        t = deg['title']                 # get the title of each item in the list
        b = deg['branch']                # get the branch of each item in the list
        dl = Degree(title=t, branch=b)   # Create a Degree model instance
        dl.save()                        # save

      return HttpResponseRedirect('/forms/')   # redirect to a new URL:
  else:                                   # if a GET (or any other method) we'll create a blank form
    form = DegreeForm()
    return render(request, 'forms.html', {'form': form })

def get_students(request):
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = StudentsForm(request.POST, request.FILES)   # create a form instance and populate it with data from the request:
    if form.is_valid():
      degree = form.cleaned_data['degree']
      roll_number = form.cleaned_data['roll_number']
      name = form.cleaned_data['name']
      year = form.cleaned_data['year']
      dob = form.cleaned_data['dob']
      print(degree, roll_number, name, year, dob)

      d = Student(degree=degree, roll_number=roll_number, name=name, year=year, dob=dob)    # write to the database
      d.save()

      
      f = request.FILES['file']        
      data = json.load(f)
      for deg in data['students']:        
        r = deg['roll_number']
        n = deg['name']
        y = deg['year']
        b = deg['dob']               
        dg = deg['degree']
        degree1 = Degree.objects.get(branch=dg[0]["branch"])
        print(degree1)
        dl = Student(degree=degree1, roll_number=r, name=n, year=y, dob=b)
        dl.save()

      return HttpResponseRedirect('/students/')
  else:                                   
    form = StudentsForm()
    return render(request, 'students.html', {'form': form })

degree_values = Degree.objects.all()
student_values = Student.objects.all()

def search(request) :
    
    global student_values
    form = SearchForm()
    my_dict = {
        "degree_rows": degree_values,
        "student_values": student_values,
        "search_form": form,
    }
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            fromdate = form.cleaned_data["dateFrom"]
            todate = form.cleaned_data["dateTo"]
            sort = form.cleaned_data["sort"]

            print(fromdate, todate, name, sort)
            if fromdate and todate:
                student_values = Student.objects.filter(
                    Q(name__icontains=name) & Q(dob__range=(fromdate, todate))
                )
            else:
                student_values = Student.objects.filter(Q(name__icontains=name))
            if sort:
                print("HI")
                student_values = student_values.order_by("name")

        my_dict["student_values"] = student_values
        return render(request, "search.html", context=my_dict)

    else:
        return render(request, "search.html", context=my_dict)


def profile(request):
    return render(request, "profile.html")

def wordle(request):
    return render(request, "wordle.html")

def tictactoe(request):
    return render(request, "tic_tac_toe.html")

def blog(request):
    return render(request, "blog.html")

def employee(request):
    return render(request, "employee.html")
      