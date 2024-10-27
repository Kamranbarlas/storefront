from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, BadHeaderError, mail_admins
from templated_mail.mail import BaseEmailMessage
# Create your views here.

def hello(request):
    try:
        ##1
        # send_mail('subject','message','info@kamibuy.com',['kamran_barlas@hotmail.com'])
        ##2
        # mail_admins('subject','message',html_message='message')
        ##3
        # mesage = EmailMessage('subject','message','info@kamibuy.com',['kamran_barlas@hotmail.com'])
        # mesage.attach_file('playground/static/images/wanted.jpg')
        # mesage.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={
                'name':'Kamran'
            }
        )
        message.send(['kamran@kamibuy.com'])
    except BadHeaderError:
        pass
    return render(request,'hello.html',{'name':'Kamran'})

