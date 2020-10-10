from django.shortcuts import render
from django.views.generic import ListView,DetailView
from products.models import Cake,CupCake,Desert,DesertFeatures,CupCakeFeatures,CakeFeatures,EastSweets, \
    EastSweetFeatures,CakeTypes
from django.core.paginator import Paginator

class CakessListView(ListView):
    model = Cake
    template_name = 'cakes.html'
    paginate_by = 6
    context_object_name = 'cakes'

    def get_context_data(self, **kwargs):
        context = super(CakessListView, self).get_context_data(**kwargs)
        context['cake_features'] = CakeFeatures.objects.all()
        context['cake_types'] = CakeTypes.objects.all()
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 6 if index >= 6 else 0
            end_index = index + 6 if index <= max_index - 6 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        return context

class DesertssListView(ListView):
    model = Desert
    template_name = 'deserts.html'
    paginate_by = 6
    context_object_name = 'deserts'

    def get_context_data(self, **kwargs):
        context = super(DesertssListView, self).get_context_data(**kwargs)
        context['desert_features'] = DesertFeatures.objects.all()
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 6 if index >= 6 else 0
            end_index = index + 6 if index <= max_index - 6 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        return context

class CupCakessListView(ListView):
    model = CupCake
    template_name = 'cupcakes.html'
    paginate_by = 6
    context_object_name = 'cupcakes'

    def get_context_data(self, **kwargs):
        context = super(CupCakessListView, self).get_context_data(**kwargs)
        context['cupcake_features'] = CupCakeFeatures.objects.all()
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 6 if index >= 6 else 0
            end_index = index + 6 if index <= max_index - 6 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        return context

class SweetssListView(ListView):
    model = EastSweets
    template_name = 'sweets.html'
    paginate_by = 6
    context_object_name = 'sweets'

    def get_context_data(self, **kwargs):
        context = super(SweetssListView, self).get_context_data(**kwargs)
        context['sweet_features'] = EastSweetFeatures.objects.all()
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 6 if index >= 6 else 0
            end_index = index + 6 if index <= max_index - 6 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        return context



class CakeDetailView(DetailView):
    model=Cake
    template_name = 'detail_page.html'
    context_object_name = 'object'

class DesertDetailView(DetailView):
    model=Desert
    template_name = 'detail_page.html'
    context_object_name = 'object'

class CupCakeDetailView(DetailView):
    model=CupCake
    template_name = 'detail_page.html'
    context_object_name = 'object'

class SweetDetailView(DetailView):
    model=EastSweets
    template_name = 'detail_page.html'
    context_object_name = 'object'