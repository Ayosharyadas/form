from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import forms

#DataFlair #Form #View Functions
def index(request):
    form = forms.EmployeeForm()
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'index.html', {'html': html, 'form': form})