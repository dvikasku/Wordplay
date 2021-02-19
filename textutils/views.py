from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    wordcount = request.POST.get('wordcount', 'off')
    if removepunc == "on":   
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed }
        djtext = analyzed
    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Upper Case','analyzed_text': analyzed }
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Line','analyzed_text': analyzed }
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index + 1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra space Remover','analyzed_text': analyzed }
        djtext = analyzed
    if wordcount == "on":
        analyzed = analyzed + str(len(djtext))
        params = {'purpose':'Total number of Words are','analyzed_text': analyzed }
        djtext = analyzed
    if (removepunc != "on" and fullcap != "on" and newlineremover != "on" and extraspaceremover != "on" and wordcount != "on"):
        return render(request, 'error.html')
    return render(request, 'analyze.html',params)

