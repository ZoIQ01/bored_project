from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView
from django.contrib import messages
from django.conf import settings
from log_in.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'  
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        # Save user but set as inactive until email is verified
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        # Send verification email
        self.send_verification_email(user)
        
        messages.success(
            self.request,
            'Account created! Please check your email to verify your account.'
        )
        return redirect(self.success_url)
    
    def send_verification_email(self, user):
        """Send email verification link to user"""
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        verification_link = self.request.build_absolute_uri(
            f"/verify-email/{uid}/{token}/"
        )
        
        subject = 'Verify your email address'
        message = f"""
Hi {user.username},

Thanks for signing up! Please click the link below to verify your email address:

{verification_link}

This link will expire in 24 hours.

If you didn't create an account, please ignore this email.

Best regards,
Auth Demo Team
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        ) 

@login_required
def home_view(request):
    """
    Simple home page shown after login/registration.
    """
    return render(request, 'home.html')


def verify_email(request, uidb64, token):
    """
    Verify user's email address using token from email link.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email verified successfully! You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'Verification link is invalid or has expired.')
        return redirect('login')