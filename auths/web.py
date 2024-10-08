from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse,reverse_lazy
from datetime import datetime
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views import View
from auths import models
from django.contrib.auth import login,logout # ,authenticate

from auths.custombackend import authenticate as authenticate_user
from auths.forms import PasswordForm, RoleEditForm,RoleForm, UserForm,PermissionForm,UserUpdateFormPass,CustomAuthenticationForm
from auths.models import DefaultPassword, LoginLog, Role, User,CustPermission
from auths.views import import_roles
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import  Q
from core.common import send_email_common

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

###class based view # second developer

class CreatePermission(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    form_class=PermissionForm

    template_name = 'auths/perm/create.html'
    context_object_name = 'form'
    header='New Permission'
    success_url = reverse_lazy('permissions')

    def get(self,request, **kwargs):
        import_roles()
        messages.success(self.request, 'Updated permission')
        return redirect(self.success_url)


    def post(self, request, **kwargs):
        form=self.form_class(request.POST)

        if form.is_valid:
            perm_name = request.POST.get('perm_name')
            perm_desc = request.POST.get('perm_desc')
            if CustPermission.objects.filter(perm_name__iexact=perm_name).exists():
                messages.warning(self.request, 'This Permission exists')
                return render(request,self.template_name,{'form':form,'error':'This Permission exists'})

            custperm=CustPermission.objects.create(perm_desc=perm_desc,perm_name=perm_name)
            messages.success(self.request,'Created permission')
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'error': 'This Permission exists'})




class UpdatePermission(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = CustPermission
    fields = ['perm_name','perm_desc']
    template_name ='auths/perm/create.html'
    context_object_name = 'form'
    header='Update Permission'
    success_url = reverse_lazy('permissions')

    def get(self,request, **kwargs):
        import_roles()
        messages.success(self.request, 'Updated permission')
        return redirect(self.success_url)

class PermissionDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    success_message = "Success!  deleted permissions."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta permission hii, kuna data zinategemea data  hii')
            return redirect('permissions')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('permissions')

class PermissionsList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    context_object_name = 'lists'
    template_name = 'auths/perm/perm_list.html'
    header='Permissions'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class PermissionRequired(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'auths/perm/permission_required.html')
class UpdateUserCvB(LoginRequiredMixin,UpdateView):
    redirect_next_name='next'
    login_url=reverse_lazy('login')
    model=User
    #form_class=UserForm
    fields = ["is_active", "is_staff", "is_superuser",'email','username','full_name','role','phone_number']
    template_name='auths/add_user.html'
    context_object_name='form'
    success_url=reverse_lazy('users')

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        full_name=request.POST.get('full_name')
        role = request.POST.get('role')
        phone_number = request.POST.get('phone_number')
        #Staffob.objects.filter(user_id=self.kwargs['pk']).update(phone_number=phone_number,role_id=role,full_name=full_name)
        #change password
        #password = Auths.get_default_password(request)
        #hash_password = bcrypt.hashpw(
        #   password.encode("utf-8"), bcrypt.gensalt()
        #)

        #hashed_password = hash_password.decode("utf8")
        #User.objects.filter(id=self.kwargs['pk']).update(password=hashed_password)
        return super(UpdateUserCvB, self).post(request, **kwargs)


class CreateRole(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = Role
    form_class=RoleForm
    #fields = ['role_name','perm']
    template_name = 'auths/add_role.html'
    context_object_name = 'form'
    header='New Role'
    success_url = reverse_lazy('roles')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context


class UpdateRole(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = Role
    #fields = ['role_name','perm']
    form_class = RoleEditForm
    template_name = 'auths/add_role.html'
    context_object_name = 'form'
    header='Update Role'
    success_message = 'Succesfully Updated'
    success_url = reverse_lazy('roles')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class Auths:
    def __init__(self):
        pass

    def login(request):
        """Authenticate the user to the system, by checking given credentials"""
        if request.user.is_authenticated:
            if User.objects.filter(id=request.user.id).exists():
                login_log = LoginLog.objects.create(created_by=request.user)
                login_log.save()
                if "next_page" in request.session:
                    path = request.session["next_page"]
                    return redirect(path)
                return redirect("/dashboard")
            if "next_page" in request.session:
                path = request.session["next_page"]
                return redirect(path)
            return redirect("index")


        elif request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth_user.get_user_by_username(request, username=username)
            if user:
                """
                is_valid = bcrypt.checkpw(
                    password.encode("utf-8"), user.password.encode("utf-8")
                )
                """
                #if is_valid:
                user=authenticate(username=username, password=password)
                if user.is_active:
                    if user.is_staff:
                        auth_login(request, user)
                        login_log = LoginLog.objects.create(created_by=request.user)
                        login_log.save()
                        if request.GET.get("path"):
                            return redirect(request.GET.get("path"))
                        return redirect("/")
                    message = "sorry your account is not an Admin Account, communicate with your Admin"
                    return render(request, "auths/login.html", {"message": message})

                message = ("sorry your account is inactive communicate with your Admin")
                return render(request, "auths/login.html", {"message": message})

                message = "Incorrect Username or Password"
                return render(request, "auths/login.html", {"message": message})

            message = "Incorrect Username or Password"
            return render(request, "auths/login.html", {"message": message})
        if request.GET.get("next") != None:
            request.session["next_page"] = request.GET.get("next")
            return render(
                request, "auths/login.html", {"path": request.GET.get("next")}
            )
        return render(request, "auths/login.html")

    def logout(request):
        """logout the user destroy user session"""
        if LoginLog.objects.filter(created_by=request.user).first():
            log = LoginLog.objects.filter(created_by=request.user).order_by("-created_on")[
                0
            ]
            logout_log = LoginLog.objects.filter(created_by=request.user, id=log.id).update(
                logout_time=datetime.now()
            )
            # builtin function for session destroy
        auth_logout(request)
        if "next_page" in request.session:
            del request.session["next_page"]
        return redirect("/")

    def set_default_password(request):
        """set default password to be used as default for all added staffs"""
        template_name = "auths/add_password.html"
        if request.method == "POST":
            password_form = PasswordForm(request.POST or None)
            if password_form.is_valid():
                password = DefaultPassword.objects.create(
                    password=password_form.cleaned_data["password"]
                )
                password.save()
                users = User.objects.filter(~Q(username__iexact='tobacco'))
                passD = DefaultPassword.objects.latest('created_on').password
                for usr in users:
                    usr.set_password(passD)
                    usr.is_active = True
                    usr.save()
                return redirect(reverse('core:dashboard'))

                return render(
                    request,
                    template_name,
                    {"password": Auths.get_default_password(request)},
                )
        return render(
            request, template_name, {"password": Auths.get_default_password(request)}
        )

    def get_default_password(request):
        """Get (default) password"""
        password = DefaultPassword.objects.filter(is_active=True).order_by(
            "-created_on"
        )
        if password:
            return password[0].password
        else:
            return "There was no Default Password"


class Staff:
    def __init__(self):
        pass

    def create_user(request):
        """Add user to the system"""
        template_name = "auths/add_user.html"
        header = 'Add Staff'
        if request.method == "POST":
            user_form = UserForm(request.POST or None)
            if user_form.is_valid():

                role_id=request.POST.get('role')
                is_staff = False
                is_active = False
                is_superuser = False
                if request.POST.get('is_staff'):
                    is_staff=True
                if request.POST.get('is_active'):
                    is_active=True
                if request.POST.get('is_superuser'):
                    is_superuser=True



                user = models.User.objects.create(
                    username=request.POST.get("username"),
                    is_staff=is_staff,
                    is_superuser=is_superuser,
                    is_active=is_active,
                    email=request.POST.get('email'),
                    full_name=user_form.cleaned_data["full_name"],
                    phone_number=user_form.cleaned_data["phone_number"],
                    role_id=request.POST.get('role'),
                )
                import random
                passexce=randomword(5)
                print(passexce)

                user.set_password(passexce)
                user.save()
                title='M-CRM Registrations'
                urldata=request.build_absolute_uri(reverse('login_user'))
                subject='Dear '+str(request.POST.get('full_name'))+'\n Welcome to the call center crm. \n Your username  '+str(request.POST.get('username'))+'\n Your Password: '+str(passexce)+'\n MCRM link:'+urldata+'  \n Thanks \n CRM Software'

                send_email_common(
                    title=title,
                    desc=subject,
                    emails=[request.POST.get('username')]
                )
                print(urldata)
                return redirect(reverse('users'))


        user_form = UserForm()
        return render(request, template_name, {"form": user_form,'header':header})


    def create_staff(request):
        """Add staff to the system"""
        template_name = "auths/add_staff.html"

        if request.method == "POST":
            staff_form = StaffForm(request.POST or None)
            if staff_form.is_valid():
                password = Auths.get_default_password(request)
                hash_password = bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt()
                )
                role = models.Role.objects.filter(
                    role_name=staff_form.cleaned_data["role"]
                )
                if role:
                    role = role[0]
                else:
                    role = None
                #is_staff = False
                if role.role_name in [
                    "Admin",
                    "admin",
                    "Administrator",
                    "administrator",
                ]:
                    is_staff = True
                hashed_password = hash_password.decode("utf8")
                existing_user = models.User.objects.filter(
                    username=staff_form.cleaned_data["phone_number"]
                )
                if existing_user:
                    roles = models.Role.objects.filter(is_active=True).order_by(
                        "role_name"
                    )
                    message = "User with Entered username Exists"
                    return render(
                        request, template_name, {"roles": roles, "message": message}
                    )
                user = models.User.objects.create(
                    password=hashed_password,
                    username=staff_form.cleaned_data["phone_number"],
                    is_staff=is_staff,
                )
                user.save()
                staff = models.Staff.objects.create(
                    user=user,
                    full_name=staff_form.cleaned_data["full_name"],
                    role=role,
                    phone_number=staff_form.cleaned_data["phone_number"],
                )
                staff.save()
                if staff:
                    return Staff.get_staffs(request)
        roles = models.Role.objects.filter(is_active=True).order_by("role_name")
        return render(request, template_name, {"roles": roles})

    def edit_staff(request, staff_id):
        """edit staff to the system"""
        template_name = "auths/add_staff.html"
        if request.method == "POST":
            staff_form = StaffForm(request.POST or None)
            if staff_form.is_valid():
                role = models.Role.objects.filter(
                    role_name=staff_form.cleaned_data["role"]
                )
                models.Staff.objects.filter(id=staff_id).update(
                    full_name=staff_form.cleaned_data["full_name"],
                    role=role[0],
                    phone_number=staff_form.cleaned_data["phone_number"],
                )

                return redirect("/staff-members")
        form = models.Staff.objects.get(id=staff_id)
        roles = models.Role.objects.filter(is_active=True).order_by("role_name")
        return render(request, template_name, {"roles": roles, "form": form})

    def get_staffs(request):
        """get (display) all staffs"""
        template_name = "auths/staffs.html"
        header = ' Staff/User'
        #try:
        staffs = models.User.objects.filter(is_active=True).order_by("-date_joined")
        paginated_staffs = Paginator(staffs, 10)
        page_number = request.GET.get("page")
        page_obj = paginated_staffs.get_page(page_number)
        return render(request, template_name, {"users": staffs,'header':header})
        #except:
        raise HttpError(500, "Internal Server Error")

    def get_staffs_inactive(request):
        """get (display) all staffs"""
        template_name = "auths/staffs.html"
        header='Inactive Staff'
        #try:
        staffs = models.Staff.objects.filter(is_active=False).order_by("-created_on")
        paginated_staffs = Paginator(staffs, 10)
        page_number = request.GET.get("page")
        page_obj = paginated_staffs.get_page(page_number)
        return render(request, template_name, {"users": staffs,'header':header})
        #except:
        raise HttpError(500, "Internal Server Error")



    def delete_staff(request, staff_id):
        """delete staff member by staff id"""
        template_name = "auths/staffs.html"
        staff = models.User.objects.filter(~Q(id=request.user.id)&Q(id=staff_id))
        if not staff.exists():
            staffs = models.User.objects.filter(is_active=True).order_by("-created_on")
            paginated_staffs = Paginator(staffs, 10)
            page_number = request.GET.get("page")
            page_obj = paginated_staffs.get_page(page_number)
            message = "Staff was already deleted"
            return render(
                request, template_name, {"page_obj": staffs, "message": message}
            )

        return redirect(reverse('users'))


class Role:
    def __init__(self):
        pass

    def add_role(request):
        """Add role to be assigned to staffs"""
        template_name = "auths/add_role.html"
        try:
            if request.method == "POST":
                role_form = RoleForm(request.POST or None)
                if role_form.is_valid():
                    if not  models.Role.objects.filter(role_name__iexact=request.POST.get('role_name')).exists():
                        role = models.Role.objects.create(
                            role_name=role_form.cleaned_data["role_name"]
                        )
                        role.save()
                    return redirect("/roles")

            return render(request, template_name)
        except:
            raise HttpError(500, "Internal Server Error")

    def get_roles(request):
        """get (display) all roles"""
        template_name = "auths/roles.html"
        header = 'Roles'

        roles = models.Role.objects.filter(is_active=True).order_by("role_name")
        paginated_roles = Paginator(roles, 10)
        page_number = request.GET.get("page")
        page_obj = paginated_roles.get_page(page_number)
        return render(request, template_name, {"page_obj": page_obj,'header':header})

    def get_roles_inactive(request):
        """get (display) all roles"""
        template_name = "auths/roles.html"
        header='Inactive Roles'
        try:
            roles = models.Role.objects.filter(is_active=False).order_by("role_name")
            paginated_roles = Paginator(roles, 10)
            page_number = request.GET.get("page")
            page_obj = paginated_roles.get_page(page_number)
            return render(request, template_name, {"page_obj": page_obj,'header':header})
        except:
            raise HttpError(500, "internal Server Error")

    def edit_role(request, role_id):
        template_name = "auths/add_role.html"
        try:
            if request.method == "POST":
                role_form = RoleForm(request.POST or None)
                if role_form.is_valid():
                    role = models.Role.objects.filter(id=role_id).update(
                        role_name=role_form.cleaned_data["role_name"]
                    )
                    return redirect("/roles")
            form = models.Role.objects.get(id=role_id)
            return render(request, template_name, {"form": form})
        except:
            raise HttpError(500, "Internal Server Error")

    def delete_role(request, role_id):
        """Delete Roles from the database"""
        template_name = "auths/roles.html"
        role = models.Role.objects.filter(id=role_id)
        if not role.exists():
            roles = models.Role.objects.filter(is_active=True).order_by("role_name")
            paginated_roles = Paginator(roles, 10)
            page_number = request.GET.get("page")
            page_obj = paginated_roles.get_page(page_number)
            message = "Role was already Deleted"
            return render(
                request, template_name, {"page_obj": page_obj, "message": message}
            )
        if role.first().is_active:
            role.update(is_active=False)
        else:
            role.update(is_active=True)

        return redirect("/roles")

class UpdateUserChangePassword(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy("login_user")
    redirect_field_name = 'next'
    model =User
    form_class = UserUpdateFormPass
    template_name = 'auths/change_user_pass.html'
    context_object_name = 'form'
    header='CHANGE PASSWORD'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['userob']=User.objects.filter(id=self.kwargs['pk']).first()
        context['header']=self.header

        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        from auths.auth_token import Auth
        if form.is_valid():

            #is_password_correct = Auth.check_username_password(request, dotdict({'username':request.user.username,'password':request.POST.get('password')}))
            user = authenticate(self, username=request.user.username, password=request.POST.get('password'))

            if not user.is_active:
                return render(request, self.template_name, {'form': form, 'header': self.header,'error':'Old password is Invalid'})
            else:
                if request.POST.get('new_password') == request.POST.get('cpassword'):

                    user=usr=User.objects.get(id= request.user.id)
                    usr.set_password(request.POST.get('new_password'))
                    usr.save()
                    messages.success(request,'Success! update changed password')
                    return redirect(reverse('core:dashboard'))
                else:
                    messages.success(request, 'Failed! Confirm password not same as new password')
                    return render(request, self.template_name, {'form': form, 'header': self.header,'error':'New password and confirm password are not same'})

        else:
            return render(request,self.template_name,{'form':form,'header':self.header})


class LoginView1(View):
    form_class = CustomAuthenticationForm
    template_name = 'auths/login.html'
    #template_name='wananchi/wananchi_home.html'
    # display blank form
    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process form data

    def post(self, request):
        form = self.form_class(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')

        if form.is_valid():
            user = authenticate_user(self,username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.role:
                        if user.role.perm:
                            if user.role.perm.filter(perm_name='manage_account').exists() and user.role.perm.filter(perm_name='manage_buying').exists():
                                return redirect(reverse('core:apps'))
                            if user.role.perm.filter(perm_name='manage_account').exists() and not user.role.perm.filter(perm_name='manage_buying').exists():
                                return redirect(reverse('voucher:voucher_list'))
                            if not user.role.perm.filter(perm_name='manage_account').exists() and  user.role.perm.filter(perm_name='manage_buying').exists():
                                return redirect(reverse('core:dashboard'))

                    return redirect(reverse('permissions'))
            else:
                return render(request, self.template_name, {'form': form,'error':'Your username and password are incorect, please enter it well or if not registered register '+username})

        return render(request, self.template_name, {'form': form})


class ChangePassword(View):
    template_name='base/base.html'
    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)



class NoPermission(View):
    template_name='auths/perm/nopermission.html'
    def get(self,request,*args,**kwargs):

        return render(request,self.template_name )
