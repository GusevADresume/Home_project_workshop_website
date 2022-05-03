from django.forms import ModelForm, TextInput, CharField
from feedback.models import Feedback
from phonenumber_field.modelfields import PhoneNumberField
import re


class FeedbackForm(ModelForm):
    phone = CharField(label='Телефон', widget=TextInput(attrs={'value': '+7'}))
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'text', 'consent']
        labels = {'name': ('Имя'), 'phone': ('Телефон'), 'text': ('Сообщение'), 'consent': ('Согласен на обработку'), }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['consent'].required = True
        self.fields['name'].required = True

    def validate_phone(self):
        number = self.data.get('phone')
        result = re.match(r"^((\+7|8)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
                          number)
        return bool(result)

