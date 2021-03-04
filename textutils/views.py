# created this file - pavana
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'name':'pavana','place':'kakinada'}
    return render(request, 'index.html', context)


def analyse(request):
    #get the text
    textprint = request.POST.get('text','default')
   
    # check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in textprint:
            if char not in punctuations:
                analyzed = analyzed + char
        context = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        textprint = analyzed
        #return render(request, 'analyse.html', context)

    if(fullcaps=="on"):
        analyzed = ""
        for char in textprint:
            analyzed = analyzed + char.upper()

        context = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyse.html', context)
        textprint = analyzed



    if(newlineremover == 'on'):
        analyzed = ""
        for char in textprint:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char.upper()
                context = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyse.html', context)
        textprint = analyzed

    
    if(extraspaceremover == 'on'):
         analyzed = ""
         for index, char in enumerate(textprint):
             if not(textprint[index] == " " and textprint[index+1]==" "):
                 analyzed = analyzed + char

                 context = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyse.html', params)
    if(removepunc != "on" and extraspaceremover != 'on' and newlineremover != 'on' and fullcaps != 'on'):
        return render(request,'error.html')
    return render(request, 'analyse.html', context)
  
    
def capfirst(request):
    return HttpResponse('capt first')


def newlineremove(request):
    return HttpResponse('new line remove')


def spaceremove(request):
    return HttpResponse('space remove <a href ="/">back</a>')

def charcount(request):
    return HttpResponse('charcount')





