
from random import randrange
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.core.mail import send_mail
from django.core.files.storage import default_storage
from datetime import datetime
from zoneinfo import ZoneInfo
from django.views.decorators.csrf import csrf_exempt
from trashapp.models import trashData
from twilio.rest import Client



# Create your views here.
def home(request):
        try:
                dustbin_lst = trashData.objects.all()
                context = {
                        "dustbin_lst":dustbin_lst,
                }
                return render(request,'index.html',context=context)
        except:
                return render(request,'index.html',context={})


def recent_data(request):
        try:
                dustbin_lst = trashData.objects.all()
                return JsonResponse({'trash_data':list(dustbin_lst.values())})
        except:
                return HttpResponse('0')
        
def send_sms():
        print("SMS Sent")
        # Your Twilio Account SID and Auth Token
        # account_sid = 'ACd98e70c1c11752a6ffa042dd64d8ffc7'
        # auth_token = '0be3ac67f14be11e5b173cf31f66d07d'

        # # Create a Twilio client
        # client = Client(account_sid, auth_token)

        # # Send an SMS
        # from_number = '+12565677974'
        # to_number = '+919326081694'  # Replace with the recipient's phone number
        # message_body = 'Hello, this is a test message from Soham!'

        # message = client.messages.create(
        # body=message_body,
        # from_=from_number,
        # to=to_number
        # )

        # print(f"Message sent with SID: {message.sid}")

def show_data(request):
        try:
                dustbin_lst = trashData.objects.all()
                return JsonResponse({'trash_data':list(dustbin_lst.values("dustbin_id","perc"))})
        except:
                return HttpResponse('0')

def update_data(request):
        dustbin_id=request.GET.get("dustbin_id")
        perc=request.GET.get("perc")
        if(trashData.objects.filter(dustbin_id=dustbin_id).exists()):
                if(int(perc)>80):
                        send_sms()
                current_time=str(datetime.now(tz=ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S"))
                trashData.objects.filter(dustbin_id=dustbin_id).update(perc=int(perc),last_time=current_time)
                print(current_time)
                return HttpResponse(f"{dustbin_id} Percentage Updated Succesfully...")
        else:
                
                return HttpResponse(f"{dustbin_id} ID does not exists")



