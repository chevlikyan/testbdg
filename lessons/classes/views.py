from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Class
from .forms import ClassForm, CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.filter(category=self.object)
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('category-list')


class ClassListView(ListView):
    model = Class
    template_name = 'index.html'
    context_object_name = 'classes'


class ClassCreateView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'form.html'
    success_url = reverse_lazy('class-list')  # Redirect to the class list view after creation


class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'form.html'
    slug_field = 'slug'
    success_url = reverse_lazy('class-list')  # Redirect to the class list view after update


class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('class-list')  # Redirect to the class list view after deletion
    slug_field = 'slug'


class ClassDetailView(DetailView):
    model = Class
    template_name = 'class_detail.html'
    context_object_name = 'class'
    slug_field = 'slug'
