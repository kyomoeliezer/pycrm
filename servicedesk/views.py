from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse,reverse_lazy
from datetime import datetime
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from servicedesk.models import *
from django.contrib import messages


class PopupView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    template_name = 'servicedesk/popup/new.html'
    model = CustomerQuery
    context_object_name = 'form'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{})




