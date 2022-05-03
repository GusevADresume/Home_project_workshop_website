from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from feedback.models import AGREEMENT, Feedback
from feedback.forms import FeedbackForm
import telebot
from contacts_info.models import Contacts_info, Phone


def feedback(request):
    template = 'feedback/feedback.html'
    form = FeedbackForm()
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.validate_phone():
            f.save()
            notice_send(f)
            return render(request, 'answer.html', {'form': 'form'})
        else:
            return render(request, template, {'form': form, 'error': 'Проверьте правильность ввода номера'})
    return render(request, template, {'form': form})


def agrementview(request):
    template = 'feedback/AGREEMENT.html'
    obj = AGREEMENT.objects.get()
    context = {'title': obj.title,
               'text': obj.text}
    return render(request, template, context)


def notice_send(form):
    message = f"You have new feedback \nname: {form.data.get('name')}\nphone:{form.data.get('phone')}\ntext:{form.data.get('text')})"
    send_mail('Feedback from website!', message,
              'motovar.site@gmail.com', ['motovar.site@gmail.com'])
    try:
        token = Contacts_info.objects.get(id=1)
        bot = telebot.TeleBot(token.tg_token)
        tg_id = Phone.objects.get(id=1)
        bot.send_message(tg_id.tg_id, message, )
    except:
        pass
