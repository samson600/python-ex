from django.shortcuts import render

# Create your views here.
def demoapp(request):
    return render(request, 'demo-page.html')

def service(request):
    return render(request, 'service.html')
