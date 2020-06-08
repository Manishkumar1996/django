from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
def home_view(request, *args, **kwargs):
    #     return HttpResponse("<h1>Hello World!</h1")
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    #     return HttpResponse("<h1>Contact page</h1")
    my_content = {
        'text': 'This is about us',
        'number': 1234567890,
        'name': 'Manish Kumar Prajapat',
        'list': [7877, 8302, 1234, 9874]
    }
    return render(request, 'about.html', my_content)


def contact_view(request, *args, **kwargs):
    #     return HttpResponse("<h1>Contact page</h1")
    return render(request, 'contact.html', {})


# Class base

class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class AboutView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        my_content = {
            'text': 'This is about us',
            'number': 1234567890,
            'name': 'Manish Kumar Prajapat',
            'list': [7877, 8302, 1234, 9874]
        }
        return render(request, self.template_name, my_content)


class ContactView(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
