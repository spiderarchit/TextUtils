# this file has beeen created by me.....

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    check = request.POST.get('removepunc','Off')
    capitalize = request.POST.get('capitalize','off')
    charcount = request.POST.get('charcount','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')

    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if check == "on":
        analyzed_text = ""
        for char in djtext:
            if char not in punc:
                analyzed_text += char


        djtext = analyzed_text
        params = {'purpose': 'removepunc', 'analyzed_text': analyzed_text}
        # return render(request,'analyze.html',params)

    if capitalize == "on":
        analyzed_text = ""
        for char in djtext:
            analyzed_text += char.upper()
        djtext = analyzed_text
        # params = {'purpose':'capitalized Successfull' , 'analyzed_text': analyzed_text}
        # return render(request,'analyze.html',params)
    if charcount == "on":
         count = 0
         for char in djtext:
             if(char!=" "):
                 count+=1
         return render(request,'analyze.html',{'purpose':'Total number of characters are' , 'analyzed_text' : count})

    if extraspaceremove == "on":
        analyzed_text = ""
        for idx,char in enumerate(djtext):
            if(not(djtext[idx]==" " and djtext[idx+1]==" ")):
                analyzed_text += char
        djtext = analyzed_text
        # return render(request,'analyze.html',{'purpose': 'Extra Spaces Removed' , 'analyzed_text':analyzed_text})
    if newlineremove=="on":
        analyzed_text  = ""
        for char in djtext:
            if char != '\n':
                analyzed_text += char
        djtext = analyzed_text
        # return render(request,'analyze.html',{'purpose':'New lines Removed','analyzed_text' : analyzed_text})
    return render(request,'analyze.html',{'purpose': 'Analyzed Text' , 'analyzed_text':djtext})

    #
    # else:
    #     return HttpResponse("Error")

# def charcount(request):
#     return HttpResponse("this is charcount page")
#
# def removepunc(request):
#     return HttpResponse("this is remove punc page")
#
# def capitalize(request):
#     return HttpResponse("first letter capitalize")