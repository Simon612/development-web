from django.shortcuts import render
from django.http import HttpResponse
from .models import Text, MainText, lists, Emails
from django.core.mail import send_mail
# Create your views here.

def homepage(response):
    m_t = MainText.objects.get(id=1)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("signup"):
            pass
        elif response.POST.get("Read"):
            pass


    return render(response,"main/homepage.html",{"maintext":m_t.text})

def aboutme(response):
    t = Text.objects.get(id=2)
    t1 = Text.objects.get(id=1)
    return render(response,"main/aboutme.html",{"text2":t.text2, "text1":t1.text2})

def signed(response):
    ls = lists.objects.get(id=1)
    t = Text.objects.get(id=3)
    t2 = Text.objects.get(id=4)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("signup"):
            e = response.POST.get("email")
            ls.emails_set.create(txt=e)
            send_mail('New Client',
                      e,
                      'marossy.webprogramming@gmail.com',
                      ['maros.papan126@gmail.com'],
                      fail_silently=False,
                      )
            return render(response,"main/signedup.html",{"name":e})
    return render(response,"main/signed.html",{"ts":t.text2, "expect":t2.text2})

def list(response):
    ls = lists.objects.get(id=1)
    if response.method == "POST":
        if response.POST.get("update"):
            for emails in ls.emails_set.all():
                if response.POST.get("c" + str(emails.id)) == "clicked":
                    emails.complete = True
                else:
                    emails.complete = False

                emails.save()

    return render(response,"main/list.html",{"list":ls.list,"ls":ls})

def homepage2(response):
    ls = lists.objects.get(id=1)
    t = Text.objects.get(id=3)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("signup"):
            e = response.POST.get("email")
            ls.emails_set.create(txt=e)
            return render(response, "main/signedup.html", {"name": e})
    return render(response, "main/homepage2.html", {"ts": t.text2})



