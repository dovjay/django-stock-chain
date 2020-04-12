from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PermissionWarehouse, Warehouse, Contact
from .forms import ContactForm

# Create your views here.
def contacts(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'account/contacts.html', context)

class CreateContact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-contacts')

    def form_valid(self, form, *args, **kwargs):
        if self.request.user.is_superuser:
            form.instance.owner = self.request.user
        else:
            permission = get_object_or_404(PermissionWarehouse, user=self.request.user)
        return super(CreateContact, self).form_valid(form)

class UpdateContact(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-contacts')

class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('account-contacts')

def manage_accounts(request):
    return render(request, 'account/accounts.html')