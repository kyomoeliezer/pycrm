from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse,reverse_lazy
from datetime import datetime
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import *
from django.contrib import messages
class CategoryCreate(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Category
    fields = ['name']
    template_name = 'core/setting/new_category.html'
    context_object_name = 'form'
    header = 'New Category'
    success_url = reverse_lazy('category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context


class CategoryUpdate(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Category
    fields = ['name']
    template_name = 'core/setting/new_category.html'
    context_object_name = 'form'
    header = 'Update Category'
    success_url = reverse_lazy('category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class CategoryLists(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Category
    template_name = 'core/setting/category_lists.html'
    context_object_name = 'lists'
    header = 'Categories'
    success_url = reverse_lazy('category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class CategoryDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Category
    success_message = "Success!  umefuta."
    def post(self, request, *args, **kwargs):
        url=reverse('category_lists')
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta aina user huyu, kuna data zinategemea data za user hii')
            return redirect(url)

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('category_lists')


########SUBCATEGORIES
class SubcategoryCreate(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = SubCategory
    fields = ['name','category']
    template_name = 'core/setting/new_subcategory.html'
    context_object_name = 'form'
    header = 'New Sub Category'
    success_url = reverse_lazy('sub_category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context


class SubCategoryUpdate(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = SubCategory
    fields = ['name','category']
    template_name = 'core/setting/new_subcategory.html'
    context_object_name = 'form'
    header = 'Update Sub Category'
    success_url = reverse_lazy('sub_category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class SubCategoryLists(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = SubCategory
    template_name = 'core/setting/sub_category_lists.html'
    context_object_name = 'lists'
    header = 'Sub categories '
    success_url = reverse_lazy('sub_category_lists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class SubCategoryDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = SubCategory
    success_message = "Success!  umefuta."
    def post(self, request, *args, **kwargs):
        url=reverse('sub_category_lists')
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta aina user huyu, kuna data zinategemea data za user hii')
            return redirect(url)

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('sub_category_lists')

########LOCATION
class LocationCreate(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Location
    fields = ['name']
    template_name = 'core/setting/new_location.html'
    context_object_name = 'form'
    header = 'New Location'
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context


class LocationUpdate(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Location
    fields = ['name']
    template_name = 'core/setting/new_location.html'
    context_object_name = 'form'
    header = 'Update Location'
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class LocationsLists(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Location
    template_name = 'core/setting/locations.html'
    context_object_name = 'lists'
    header = 'Locations '
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        return context

class LocationsDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Location
    success_message = "Success!  umefuta."
    def post(self, request, *args, **kwargs):
        url=reverse('locations')
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta aina user huyu, kuna data zinategemea data za user hii')
            return redirect(url)

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('locations')

