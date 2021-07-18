from django.shortcuts import render
from .models import Message

TEMPLATE = 'foaas/message.html'

def get_message_body(message_name):
    # Get body of message from db
    message = Message.objects.get(name=message_name)
    body = message.body
    return body

def index(request):
    template = 'foaas/index.html'
    messages = Message.objects.all()
    message_list = []

    # Format message body and add to a message_list
    for message in messages:
        message_name = message.name
        message_body = get_message_body(message_name)
        message_list.append((message_name, message_body.format(":name", ":pronoun")))

    content = {
        'message_list': message_list,
    }
    return render(request, template, content)

def fuck_you(request, name, sender):
    template = TEMPLATE
    message = get_message_body('fuck_you')
    content = {
        'name': name, 
        'sender': sender, 
        'message': message.format(name)
    }

    return render(request, template, content)

def awesome(request, name, sender):
    template = TEMPLATE
    message = get_message_body('awesome')
    content = {
        'name': name, 
        'sender': sender, 
        'message': message.format(name)
    }
    return render(request, template, content)

def sfu(request, name, sender):
    template = TEMPLATE
    message = get_message_body('sfu')
    content = {
        'name': name,
        'sender': sender,
        'message': message.format(name),
    }
    return render(request, template, content)

def ballmer(request, name, pronoun, sender):
    template = TEMPLATE
    message = get_message_body('ballmer')
    content = {
        'name': name,
        'sender': sender,
        'message': message.format(name, pronoun),
    }
    return render(request, template, content)

def dalton(request, name, sender):
    template = TEMPLATE
    message = get_message_body('dalton')
    content = {
        'name': name,
        'sender': sender,
        'message': message.format(name),
    }
    return render(request, template, content)

