from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor, Receiver
from .forms import DonorForm, ReceiverForm

# Show all donors
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'lifesaver_app/donor_list.html', {'donors': donors})

# Add new donor
def donor_create(request):
    form = DonorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('donor_list')
    return render(request, 'lifesaver_app/donor_form.html', {'form': form})

# Show all receivers
def receiver_list(request):
    receivers = Receiver.objects.all()
    return render(request, 'lifesaver_app/receiver_list.html', {'receivers': receivers})

# Add new receiver
def receiver_create(request):
    form = ReceiverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('receiver_list')
    return render(request, 'lifesaver_app/receiver_form.html', {'form': form})
