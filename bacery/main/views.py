from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from products.models import Cake,CupCake,Desert,EastSweets
from main.forms import SubscriberForm,ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from main.models import AboutProject,Contact,ContactInfo


class MainPageView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cakes'] = Cake.objects.all()[:6]
        context['cupCakes'] = CupCake.objects.all()[:6]
        context['deserts'] = Desert.objects.all()[:3]
        context['eastSweets'] = EastSweets.objects.all()[:3]
        return context

class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    template_name = None
    http_method_names = ('post',)
    success_url = reverse_lazy('main:home')

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect_url

    def form_valid(self, form):
        messages.success(self.request,'Subscribe oldunuz')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,form.errors)
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect(redirect_url)
    
    
    
    
class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutUs = AboutProject.objects.get()
        cupcakeCount= CupCake.objects.all().count()
        sweetCount = EastSweets.objects.all().count()
        cakeCount = Cake.objects.all().count()
        desertCount = Desert.objects.all().count()
        context={
            'sweetCount':sweetCount,
            'cupcakeCount':cupcakeCount,
            'cakeCount':cakeCount,
            'desertCount':desertCount,
            'aboutUs':aboutUs,
        }
        return context

class ContactSubjectView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    # http_method_names = ('post',)
    success_url = reverse_lazy('main:contact')

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect_url

    def form_valid(self, form):
        messages.success(self.request,'Ваше письмо доставлено.')
        return super().form_valid(form)


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contactInfo = ContactInfo.objects.get()
        context['contactInfo'] = contactInfo
        context['form'] = ContactForm()
        if self.request.GET.get('objectName'):
            print('asdasdasdsadasd',self.request.GET.get('objectName'))
            context['objName'] = self.request.GET.get('objectName')
        return context