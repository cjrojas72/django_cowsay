from django.shortcuts import render
from cowsay.models import UserInput

# Create your views here.
def index(request):
  data = UserInput.objects.all()
  return render(request, 'index.html', {'data' : data})