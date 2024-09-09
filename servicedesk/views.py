from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse,reverse_lazy
from datetime import datetime
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from servicedesk.models import *
from servicedesk.forms import *
from auths.common_roles import *
from django.contrib import messages
from django.db.models import  *
from core.common import create_ticket

class PopupView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    template_name = 'servicedesk/popup/popupx.html'
    model = CustomerQuery
    form_class =AttendForm
    context_object_name = 'form'

    def get(self,request,*args,**kwargs):
        context={}
        context['tab']=request.GET.get('tab')
        context['form']=self.form_class
        context['contact']=contact=Contact.objects.filter(mobile__iexact=request.GET.get('caller')).first()
        context['queries'] = CustomerQuery.objects.filter(contact=contact).order_by('-id')
        return render(request,self.template_name,context)

    def post(self,request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact = Contact.objects.filter(id=request.POST.get('contact')).first()

            form=form.save(commit=False)
            form.created_by=request.user
            no=0
            if CustomerQuery.objects.filter(orderno__gt=0).exists():
                no=CustomerQuery.objects.filter(orderno__gt=0).aggregate(max_id=Max('orderno'))['max_id']

            form.ticketNo=create_ticket(no+1)
            form.orderno=no+1
            form.desc = request.POST.get('desc')

            form.save()
            urel=reverse('popup_distribute')+str('?caller='+contact.mobile)+'&tab=recent'
            return redirect(urel)

            #return HttpResponse(request.POST.get('mobile')+str(request.GET.get('caller')))
        caller = request.GET.get('caller')
        return render(request, self.template_name, {'caller': caller, 'form': self.form_class})




class PopupNewView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    template_name = 'servicedesk/popup/popup_newx.html'
    model = CustomerQuery
    form_class = ContactForm
    context_object_name = 'form'

    def get(self,request,*args,**kwargs):
        caller=request.GET.get('caller')

        return render(request,self.template_name,{'caller':caller,'form':self.form_class})

    def post(self,request,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.created_by=request.user
            form.save()
            urel=reverse('popup_distribute')+str('?caller='+request.POST.get('mobile'))+'&tab=attend'
            return redirect(urel)

            #return HttpResponse(request.POST.get('mobile')+str(request.GET.get('caller')))
        caller = request.GET.get('caller')
        return render(request, self.template_name, {'caller': caller, 'form': self.form_class})


class ContactLists(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Contact
    template_name = 'servicedesk/data/contact_lists.html'
    context_object_name = 'lists'
    header = 'Contacts '
    form_class=SeachData
    success_url = reverse_lazy('contact_lists')


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        context['form']=self.form_class
        if is_superagent(self.request.user) or  is_admin(self.request.user):
            context['lists']=Contact.objects.all().order_by('-id')[:110]
        elif is_agent(self.request.user):
            context['lists']=Contact.objects.filter(created_by=self.request.user).order_by('-id')[:110]
        else:
            context['lists']=[]#Contact.objects.filter(created_by=self.request.user).order_by('-id')[:110]

        return context

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        if is_superagent(self.request.user) or is_admin(self.request.user):
            lists = Contact.objects.filter(id__isnull=False)
        elif is_agent(self.request.user):
            lists = Contact.objects.filter(created_by=self.request.user)
        else:
            lists = None  # Contact.objects.filter(created_by=self.request.user).order_by('-id')[:110]

        if form.is_valid():

            context = {}
            data=None
            if lists:
                context['lists'] = lists.filter(created_on__gte=request.POST.get('fromdate'),created_on__date__lte=request.POST.get('todate')).order_by('-created_on')
            context['header'] = 'Contacts from ' + request.POST.get('fromdate')+' '+request.POST.get('todate')
            context['form'] = form
            return render(request, self.template_name, context)
        else:
            if lists:
                context['lists'] = lists.order_by('-created_on')[:150]
            context['header'] = self.header
            context['form'] = self.form_class
            return render(request, self.template_name, context)




class QueryLists(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustomerQuery
    template_name = 'servicedesk/data/queries_lists.html'
    context_object_name = 'lists'
    header = 'Service Lists '
    form_class=SeachData
    success_url = reverse_lazy('query_lists')


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        context['form']=self.form_class
        if is_superagent(self.request.user) or  is_admin(self.request.user):
            context['lists']=CustomerQuery.objects.all().order_by('-id')[:110]
        elif is_agent(self.request.user):
            context['lists']=CustomerQuery.objects.filter(created_by=self.request.user).order_by('-id')[:110]
        else:
            context['lists']=[]#Contact.objects.filter(created_by=self.request.user).order_by('-id')[:110]

        return context

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        if is_superagent(self.request.user) or is_admin(self.request.user):
            lists = CustomerQuery.objects.filter(id__isnull=False)
        elif is_agent(self.request.user):
            lists = CustomerQuery.objects.filter(created_by=self.request.user)
        else:
            lists = None  # Contact.objects.filter(created_by=self.request.user).order_by('-id')[:110]

        if form.is_valid():
            context = {}
            data=None
            if lists:

                context['lists'] = lists.filter(created_on__gte=request.POST.get('fromdate'),created_on__date__lte=request.POST.get('todate')).order_by('-created_on')
            context['header'] = 'Contacts from ' + request.POST.get('fromdate')+' '+request.POST.get('todate')
            context['form'] = form
            return render(request, self.template_name, context)
        else:
            if lists:

                context['lists'] = lists.order_by('-created_on')[:150]
            context['header'] = self.header
            context['form'] = self.form_class
            return render(request, self.template_name, context)


class UpdateQuery(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustomerQuery
    fields = ['desc','category','subcategory','status']
    template_name = 'servicedesk/data/update_query.html'
    context_object_name = 'form'
    header = 'Update Query'
    success_url = reverse_lazy('queries')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['caller']=CustomerQuery.objects.filter(id=self.kwargs['pk']).first()
        context['header'] = self.header
        return context

class AttendQuery(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustomerQuery
    fields = ['status','response']
    template_name = 'servicedesk/popup/modal/modal_attend_general_ticket.html'
    context_object_name = 'form'
    header = 'Update Query'
    success_url = reverse_lazy('queries')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['req']=CustomerQuery.objects.filter(id=self.kwargs['pk']).first()
        context['header'] = self.header
        return context



class PopUpIntroView(LoginRequiredMixin,View):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    def get(self,request,*args,**kwargs):
        contact=Contact.objects.filter(Q(mobile__iexact=request.GET.get('caller'))|Q(mobile2__iexact=request.GET.get('caller'))).first()
        if contact:
            if request.GET.get('tab'):
                return redirect(reverse('popup')+'?caller='+request.GET.get('caller')+'&tab='+request.GET.get('tab'))
            else:
                return redirect(
                    reverse('popup') + '?caller=' + request.GET.get('caller') + '&tab=recent')

        else:
            if request.GET.get('tab'):
                return redirect(reverse('new_popup') +'?caller='+request.GET.get('caller')+'&tab='+request.GET.get('tab'))
            else:
                return redirect(reverse('new_popup') + '?caller=' + request.GET.get('caller') + '&tab=home')

        return render(request,self.template_name,context)




