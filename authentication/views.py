from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from authentication.forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
            We use email instead of username in the login form,
        because our User model is designed to use
        email as the primary identifier for users.
        """
        email = form.cleaned_data.get('username')  # 'username' refers to the email field in the form
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            user.last_active_datetime = timezone.now()
            user.save(update_fields=['last_active_datetime'])

            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid email or password.')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CustomLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
