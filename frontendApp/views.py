from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')
def contact(request):
    return render(request, 'contact.html')
def packages(request):
    return render(request, 'package.html')
def team(request):
    return render(request, 'team.html')
def testimonials(request):
    return render(request, 'testimonial.html')
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

