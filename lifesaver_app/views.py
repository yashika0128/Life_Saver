from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor, Receiver
from .forms import DonorForm, ReceiverForm

# 🏠 Home Page
def index(request):
    return render(request, 'lifesaver_app/index.html')

# 🩸 Donor Views
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'lifesaver_app/donor_list.html', {'donors': donors})

def donor_create(request):
    form = DonorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('donor_list')
    return render(request, 'lifesaver_app/donor_form.html', {'form': form})

def donor_edit(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    form = DonorForm(request.POST or None, instance=donor)
    if form.is_valid():
        form.save()
        return redirect('donor_list')
    return render(request, 'lifesaver_app/donor_form.html', {'form': form})

def donor_delete(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    if request.method == 'POST':
        donor.delete()
        return redirect('donor_list')
    return render(request, 'lifesaver_app/donor_confirm_delete.html', {'donor': donor})

# ❤️ Receiver Views
def receiver_list(request):
    receivers = Receiver.objects.all()
    return render(request, 'lifesaver_app/receiver_list.html', {'receivers': receivers})

def receiver_create(request):
    form = ReceiverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('receiver_list')
    return render(request, 'lifesaver_app/receiver_form.html', {'form': form})

# 🌐 Static/Informational Pages
def community(request):
    return render(request, 'lifesaver_app/community.html')

def mobile_friendly(request):
    return render(request, 'lifesaver_app/mobile_friendly.html')

def trusted_network(request):
    return render(request, 'lifesaver_app/trusted_network.html')

def track_impact(request):
    return render(request, 'lifesaver_app/track_impact.html')

def safe_easy_donation(request):
    return render(request, 'lifesaver_app/safe_easy_donation.html')
