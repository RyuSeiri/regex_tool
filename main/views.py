import re
from django.shortcuts import render
from .models import Regex

def index(request):
    if request.method == 'POST':
        pattern = request.POST['pattern']
        text = request.POST['text']
        result = re.findall(pattern, text)
        Regex.objects.create(pattern=pattern, text=text, result=result)
    return render(request, 'index.html')
