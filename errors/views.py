from django.shortcuts import render

# Create your views here.
def errors_index(request):
    division_by_zero = 1 / 0
    return render(request, 'index.html', {})