from django.shortcuts import render
from contacts_info.models import Contacts_info

def ContactInfoView(request):
    print(request)
    template = 'contacts_info/contacts_info.html'
    obj = Contacts_info.objects.all()
    info = get_contacts(obj)
    context = {'contacts':obj,
               'info':info}
    return render(request,template,context)

def get_contacts(qset):
    for set in qset:
        return set.phone.all()