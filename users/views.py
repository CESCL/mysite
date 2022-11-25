from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, BookingForm #, UserUpdateForm, ProfileUpdateForm
from .models import Booking, User, License

def home(request):
    return render(request, "users/home.html")

def about(request):
    return render(request, "users/about.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your applicant account has been created!. Now you are able to login.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def booking(request):
    user_id = request.user.id
    if request.method == "POST":
        b_form = BookingForm(request.POST, instance=request.user.booking)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f"Your booking has been set")
            return redirect("profile")
    else:
        b_form = BookingForm(instance=request.user.booking)
    context = {
        'b_form': b_form,
        'booking': Booking.objects.get(id=user_id)
    }
    form = BookingForm()
    return render(request, "users/booking.html", context)

@login_required
def status(request):
    user_id = request.user.id
    context = {
        'booking': Booking.objects.get(id=user_id),
        'license': License.objects.get(id=user_id)
    }
    return render(request, "users/status.html", context)


#@login_required
#def updateprofile(request):
#    if request.method == "POST":
#        u_form = UserUpdateForm(request.POST, instance=request.user)
#        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
#        if u_form.is_valid() and p_form.is_valid():
#            u_form.save()
#            p_form.save()
#            messages.success(request, f"Your account has been updated")
#            return redirect("profile")
#    else:
#        u_form = UserUpdateForm(instance=request.user)
#        p_form = ProfileUpdateForm(instance=request.user.profile)
#    
#    context = {
#        'u_form': u_form,
#        'p_form': p_form
#    }
#    return render(request, "users/updateprofile.html", context)
