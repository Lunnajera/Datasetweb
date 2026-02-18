from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


def main(request):
    return render(request, "web/main.html")

