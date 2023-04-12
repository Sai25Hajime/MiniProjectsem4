from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'test.html')
def view(request):
    return render(request,'view.html')