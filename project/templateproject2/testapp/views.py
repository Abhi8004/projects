from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hello guest good '
    if h<12:
        msg=msg+'morning'
    elif h<16:
        msg=msg+'afternoon'
    elif h<21:
        msg=msg+'evening'
    else:
        msg=msg+'night'
    return render(request,'testapp/results.html',{'m':msg,'date':date})
    return response
