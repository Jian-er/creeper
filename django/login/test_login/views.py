from django.shortcuts import render



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get("password")

        if username == 'admin' and password == '123456':
            return render(request, 'index.html')
        return render(request, 'error.html')
