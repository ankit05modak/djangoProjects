## I have created this - Ankit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    # Get Text
    rectext = request.POST.get('text', 'None')

    # Get triggers
    removepunc = request.POST.get('removepunc', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc, charcount)
    try:
        if removepunc=="on":
            analysed = ""
            puncs = '''!()-_{}[]@#$%^&*=+><'''
            for char in rectext:
                if char not in puncs:
                    analysed = analysed + char
            rectext = analysed
        
        if charcount=="on" :
            analysed = ""
            count = 0
            for char in rectext:
                if char != " ":
                    count += 1
            rectext = count
        params = {
                "purpose": "Remove Punctuations",
                "analysed_text": rectext
            }
        return render(request, 'analyse.html', params)
    except Exception as e:
        return HttpResponse("No tool selected...")
    
def contact(request):
    return render(request, 'contact.html')

def contactsubmit(request):
    if request:
        useremail = request.POST.get('useremail', 'none')
        userphonenumber = request.POST.get('userphonenumber', 'none')
        userresponse = request.POST.get('userresponse', 'none')
        return HttpResponse(f'''{useremail}<br><h1>Thanks for contacting us, we will get back to you shortly.</h1>''')