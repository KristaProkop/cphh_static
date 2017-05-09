# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import Inquiry, Message



def index(request):
    return render(request, 'cphh/index.html')

def contact(request):
    if request.method == 'POST':
        try:
            inquiry_id = Inquiry.objects.create_inquiry(request.POST)
            message = Message.objects.create_message(request.POST)
            contact_success = Inquiry.objects.send_email(request.POST)
            if contact_success:
                messages.success(request, "Successfully sent! We will respond within 1 business day.")
        except: 
            messages.error(request, "Something went wrong. Please try again or call us during normal business hours.")
    return redirect(reverse('cphh:index'))
   