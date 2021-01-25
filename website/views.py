from django.shortcuts import render
from django.core.mail import send_mail
from website.models import Price


def home(request):
    Model = Price.objects.all()[:6]
    return render(request, 'website/home.html',{'prices': Model})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            f'{message} \n My email to  communicate with me {message_email}',
            message_email,
            ['asl.zurabov@gmail.com'],
        )
        # send_mail(' test message ',
        #           'I send this message just for testing django send_mail model',
        #           'asln.zurabov@gmail.com',  # send
        #           ['asl.zurabov@gmail.com'],  # get
        #           fail_silently=False)
        # return render(request, 'website/contact.html')
        return render(request, 'website/contact.html', {'message_name': message_name})
    else:
        return render(request, 'website/contact.html')


def about(request):
    return render(request, 'website/about.html')


def price(request):
    Model = Price.objects.all()
    return render(request, 'website/price.html', {'prices': Model})
