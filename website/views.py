from django.shortcuts import render
from django.core.mail import send_mail
from .models import Price
from blog.models import Blog




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


def sendMessage(request):
    mod1 = Blog.objects.all()[:2]
    mod2 = Price.objects.all()[:2]
    model1 = ''
    model2 = ''
    for i in mod1:
        model1 += f"Blog:\n{i.title}  {i.text} \n"
    for j in mod2:
        model2 += f"Offer:\n{j.title}  {j.stage}  {j.price} \n"
    if request.method == 'POST':
        mail_s = request.POST['nl-email']
        send_mail(
         'Newest article and some great offers',
         f'{model2}, \n {model1}',
         'asln.zurabov@gmail.com',
         [f'{mail_s}'],
         fail_silently=False
     )
        return render(request, 'website/sendMessage.html', {"mail_s": mail_s})
    else:

        return render(request, 'website/sendMessage.html')
