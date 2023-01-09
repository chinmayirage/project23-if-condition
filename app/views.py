from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':4344,'b':1234,'c':12355}
    return render(request,'operations.html',d)
