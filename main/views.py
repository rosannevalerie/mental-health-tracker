from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306222986',
        'name': 'Rosanne Valerie',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.