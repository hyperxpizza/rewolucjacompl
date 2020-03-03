from django.shortcuts import render

def handler404(request):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=404)

def handler400(request):
    return render(request, 'errors/400.html', status=404)

def handler403(request):
    return render(request, 'errors/403.html', status=404)