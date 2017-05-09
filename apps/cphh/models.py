from __future__ import unicode_literals
from django.db import models
from django.core.mail import EmailMessage


class InquiryManager(models.Manager):
    def create_inquiry(self, postData):
        inquiry = Inquiry.objects.create(email=postData['email'], first_name=postData['first_name'], last_name=postData['last_name'], phone=postData['phone'])
        return inquiry.id

    def send_email(self, postData):
        try: 
            body = "From: {0} {1} / Email: {2} / Phone: {3} / Appointment Prefs: {4} / Message: {5}".format(
                    str(postData['first_name']),
                    str(postData['last_name']),
                    str(postData['email']),
                    str(postData['phone']),
                    str(postData['appt']),
                    str(postData['message'])
                    )
            print 'body', body

            email = EmailMessage(
                    'CPHH Website Inquiry', 
                    body,
                    to=['meganacarolan@gmail.com']
                )
            email.send()
            return True
        except:
            print "email didn't send"
            return False

    

class MessageManager(models.Manager):
    def create_message(self, postData):
        inquiry = Inquiry.objects.filter(email=postData['email'])
        message = Message.objects.create(inquiry=inquiry[0], message=postData['message'], appt=postData['appt'])
        return inquiry[0].id


# Prospective clients who requested information
class Inquiry(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = InquiryManager()

class Message(models.Model):
    inquiry = models.ForeignKey(Inquiry, null=True, blank=True)
    message = models.TextField()
    appt = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False);
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MessageManager()
