from django.shortcuts import render

# Create your views here.
def Storefront(request):
    return render(request, 'storefront.html')
