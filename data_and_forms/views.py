from django.views import generic, View
from django.views.generic import CreateView, DeleteView, UpdateView, RedirectView
from .models import User
from django.urls import reverse_lazy

class Index(generic.ListView):
    template_name = 'users.html'

    def get_queryset(self):
        return User.objects.all()

class AddUser(CreateView):
    model = User
    fields = ['Name', 'Position', "Age", "Office"]
    template_name = 'user_form.html'

    def form_valid(self, form):
        return super(AddUser, self).form_valid(form)

class EditUser(UpdateView):
    model = User
    template_name = "user_edit.html"
    fields = ['Name', 'Position', "Age", "Office"]

    def form_valid(self, form):
        return super(EditUser, self).form_valid(form)

class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('crud:index')