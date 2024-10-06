from django.shortcuts import render

def home(request):
    data = {
        'title': 'Home',
        'values': ['he','215','ghj']
    }
    return render(request, 'main/home.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')



