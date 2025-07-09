from django.shortcuts import render

# Create your views here.

def index(request):
    content = {'user': request.user}
    return render(request, 'common/home.html', content)