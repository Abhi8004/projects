from django.shortcuts import render
from.import forms
# Create your views here.
def student_input_view(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'testapp/input.html',context=my_dict)
