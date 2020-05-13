from django.shortcuts import render
from cowsay.models import UserInput
from cowsay.forms import CowsayAddForm
from django.shortcuts import render, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
  data = UserInput.objects.all()

  if request.method == "POST":
      form = CowsayAddForm(request.POST)
      if form.is_valid():
          dat = form.cleaned_data
          UserInput.objects.create(
            user_input = dat['user_input']
          )

  form = CowsayAddForm()
  

  return render(request, 'index.html', {'data' : data, 'form': form})