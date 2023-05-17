from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup', 'markup-templating', 'mongodb', 'powershell', 'python', 'sass', 'scss', 'sql', 'typescript']

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        #check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey you forgot to pick a Programming Language")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang':lang})
        return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang':lang})    

    return render(request, 'home.html', {'lang_list': lang_list})