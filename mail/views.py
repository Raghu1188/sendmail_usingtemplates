from django.shortcuts import render ,redirect
from .forms import Contactmail
from django.core.mail import send_mail 

# Create your views here.
def simple_mail(request):
  if request.method =="GET":
    fm = Contactmail()
  else:
    if request.method == "POST":
      fm = Contactmail(request.POST)
      if fm.is_valid():
        frommail = fm.cleaned_data['Sender_id']
        fromsub = fm.cleaned_data['Subject']
        sender_file = fm.cleaned_data['file']
        message = format(fromsub,
                                                                           frommail,
                                                                           fm.cleaned_data['Message'],
                                                                           sender_file,)
        send_mail(fromsub,message,frommail,['raghuveerdhayal98@gmail.com',frommail]) 
  return render(request,'mail/sendmail.html',{'form':fm})
