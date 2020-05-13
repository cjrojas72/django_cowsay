from cowsay.models import UserInput
from cowsay.forms import CowsayAddForm
from django.shortcuts import render, reverse, HttpResponseRedirect
import subprocess

# Create your views here.
def index(request):

  if request.method == "POST":
      form = CowsayAddForm(request.POST)
      if form.is_valid():
          dat = form.cleaned_data
          UserInput.objects.create(
            user_input = dat['user_input']
          )
          cow = subprocess.run(['cowsay', dat['user_input']], stdout = subprocess.PIPE)
          cow = cow.stdout.decode('utf-8')
          form = CowsayAddForm()
          return render(request, 'index.html', {'form': form, 'cowsays': cow })

  form = CowsayAddForm()
  

  return render(request, 'index.html', {'form': form})


def history(request):
  data = UserInput.objects.all()
  cowsay_list = []

  for i in data:
      cow = subprocess.run(['cowsay', i.user_input], stdout = subprocess.PIPE)
      cow = cow.stdout.decode('utf-8')
      cowsay_list.append(cow)

  cowsay_last10 = cowsay_list[-10:]

  return render(request, 'history.html', {'cowsay': cowsay_last10})