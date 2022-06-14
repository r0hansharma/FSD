from cProfile import label
from unittest.util import _MAX_LENGTH
from django import forms
from first_app.models import Degree
import datetime

class DegreeForm(forms.Form) :
    title = forms.CharField(label='Title', max_length=20, required=False)
    branch = forms.CharField(label='Branch', max_length=50, required=False)
    file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)', required=False)

class StudentsForm(forms.Form) :
    degree = forms.ModelChoiceField(queryset=Degree.objects.all(), required=False)
    roll_number = forms.CharField(label='Roll Number', max_length=16)
    name = forms.CharField(label='Name', max_length=30)
    year = forms.CharField(label='Year')
    dob = forms.DateField(label='DOB')
    file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)')

class SearchForm(forms.Form) :
    name = forms.CharField(label="Name", max_length=50, required=False)
    dateFrom = forms.DateField(
        label="From", required=False, initial=(datetime.date.min)
    )
    dateTo = forms.DateField(label="To", required=False, initial=datetime.date.today)
    sort = forms.BooleanField(label="Sort", required=False)