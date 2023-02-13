from django.shortcuts import render
import socket
from website.meuapp.forms import IpAddressForm


# Create your views here.
def index(request):
    return render(request, 'index/index.html', status=200)


def ip_address_v4(request):
    time_seconds = 1
    if request.method == 'POST':
        form = IpAddressForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data.get('ip_address')
            port = form.cleaned_data.get('port')
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(time_seconds)
                result = sock.connect_ex((ip_address, port))

                if result == 0:
                    return ('Porta aberta!')
                else:
                    print('Porta fechada!')
            except NameError:
                print('Não foi possivél resolver esse host')

                context = {
                    'form': form,
                    'ip_address': ip_address,
                    'port': port,
                    'result': result,
                }
                return render(request, 'forms/form.html', context=context)
    else:
        form = IpAddressForm()
    return render(request, 'forms/form.html', {'form': form})



