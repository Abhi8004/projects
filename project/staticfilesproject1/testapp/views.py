from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg='morning'
    elif h<16:
        msg='afternoon'
    elif h<21:
        msg='evening'
    else:
        msg='Hello Guest !!!! Very Good night'
    my_dict={'date':date,'msg':msg}
    return render(request,'testapp/results.html',my_dict)
