from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.smtp import EmailBackend
from dashboard.models import EmailSetting

def sendemail(full_name, email, content):
    try:
        config = EmailSetting.objects.get(pk = 1)
        backend = EmailBackend(host=config.email_host, port=config.email_port, username=config.email_host_user, 
                    password=config.email_host_password, use_tls=config.email_use_tls)

        subject = f"{full_name}, thanks for contacting"
        email_from = config.email_host_user
        message = render_to_string('home/email_templates/email.html',{
            "full_name":full_name,
            "email":email,
            "content":content
        })
        msg_email_confermation = EmailMultiAlternatives(subject, message, email_from, [email], connection=backend)
        msg_email_confermation.attach_alternative(message, "text/html")
        msg_email_confermation.send()
    except:
        pass