from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406394396',
        'name' : 'Guruprasanth Meyyarasu',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)