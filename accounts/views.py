from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):

    variables = {
        'form':CustomUserCreationForm
    }

    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            variables['mensaje'] = 'Usuario Registrado'
        else:
            variables['mensaje'] = 'No se ha podido registrar'
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)
