from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


# Create your views here.
class PollList(ListView):
    model = Poll


class PollCreate(CreateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Poll Subject'
        context['backpath'] = '/poll/'
        return context


class PollUpdate(UpdateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Poll Subject'
        context['backpath'] = '/poll/'
        return context


class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'
    template_name = 'confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Poll Subject'
        context['backpath'] = '/poll/'
        return context


class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context


class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1
        option.save()
        return "/poll/" + str(option.poll_id) + "/"


class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    template_name = 'form.html'

    def get_success_url(self):
        return '/poll/' + str(self.kwargs['pid']) + '/'

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Poll Option'
        context['backpath'] = reverse('poll_view',
                                      kwargs={'pk': self.kwargs['pid']})
        return context


class OptionUpdate(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'form.html'

    def get_success_url(self):
        return '/poll/' + str(self.object.poll_id) + '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Poll Option'
        context['backpath'] = reverse('poll_view',
                                      kwargs={'pk': self.object.poll_id})
        return context


class OptionDelete(DeleteView):
    model = Option
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Poll Option'
        context['backpath'] = reverse('poll_view',
                                      kwargs={'pk': self.object.poll_id})
        return context