from django.shortcuts import render

def index(request):
    data = {
        'title': 'Glavnaya',
        'values': ['123', 'Shukaku', 'Itachi'],
        'obj': {
            'car': 'Lada Priora',
            'age': '18',
            'hobby': 'nasvay'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
