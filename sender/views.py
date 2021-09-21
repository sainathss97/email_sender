from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message = message+'\n'+f'from: {name} '
        data ={
        'name':name,
        'email':email,
        'subject':subject,
        'message':message
    }

        send_mail(data['subject'], data['message'], 'sainath.ss97@gmail.com',
              [data['email']], fail_silently=False,)
        return HttpResponse('Well done!!!')
    return render(request,'index.html')
