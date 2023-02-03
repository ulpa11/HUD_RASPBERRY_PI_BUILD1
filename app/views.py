from django.shortcuts import render,redirect

# Create your views here.
import subprocess
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        if 'ssid' in request.POST and 'password' in request.POST:
            ssid = request.POST['ssid']
            password = request.POST['password']
            try:
                output = subprocess.check_output(['sudo', 'nmcli', 'device', 'wifi', 'connect', ssid, 'password', password])
                return HttpResponse("Wifi Connected")
            except subprocess.CalledProcessError as e:
                return HttpResponse("Failed to connect to wifi")
        else:
            return HttpResponse("Missing ssid or password")
    return render(request, 'login.html')