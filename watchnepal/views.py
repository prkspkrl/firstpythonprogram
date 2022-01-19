from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request):
   return render(request,'index.html')

def removespecialchar(request):
   djtext = request.POST.get('text', 'default')
   specialchar = request.POST.get('specialchar', 'off')
   upperchar = request.POST.get('upperchar', 'off')
   countchar = request.POST.get('countchar', 'off')
   inputext = ""

   if specialchar == 'on'and upperchar == 'off':
      list_specialchar = '''¤¶§!"#$%&'()*+,-./:;<=>?@'''
      # inputext = ""
      for chars in djtext:
         if chars not in list_specialchar:
            inputext = inputext + chars
      params = {'result': 'is Ready', 'analyzed_text': inputext}
      return render(request, 'analyze.html', params)

   if specialchar == 'on' and upperchar == 'on' :
      list_specialchar = '''¤¶§!"#$%&'()*+,-./:;<=>?@'''
      inputext = ""
      for chars in djtext:
         if chars not in list_specialchar:
            # inputext = ""
            inputext = inputext + chars
            upperchar = inputext.upper()


      params = {'result': 'is Ready', 'analyzed_text': upperchar}
      return render(request, 'analyze.html', params)

   elif upperchar == 'on' and specialchar == 'off':
      # chars = ""
      for chars in djtext:
        chars = djtext.upper()
        # print(chars)
        params = {'result': 'is Ready', 'analyzed_text': chars}
        return render(request, 'analyze.html', params)


   elif (countchar == 'on'):
      for chars in djtext:
           countchar = len(djtext)
      print(countchar)
      params = {'result': ': The Total number of character is', 'analyzed_text': countchar}
      return render(request, 'analyze.html', params)


   params = {'result':'is Ready', 'analyzed_text': inputext}
   # return render(request, 'index.html')
   return render(request,'analyze.html', params)
