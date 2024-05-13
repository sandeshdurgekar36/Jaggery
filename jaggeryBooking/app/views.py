from django.shortcuts import render
import calendar
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from calendar import HTMLCalendar

def Cart(request):
    return render(request, 'cart.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

def bookslots(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        slot_id = request.POST.get('slot_id')

        obj = UsersBookedSlots.objects.create(
            user_id = user_id,
            slots_id = slot_id
        )

        AvailableSlots.objects.filter(
            id = slot_id
        ).update(display=False)

        return JsonResponse({'message': "slot booked successfully"})


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': "Email already taken"})
        else:
            user = CustomUser.objects.create(
                email= email,
                full_name = full_name,
                password= password,
                mobile_number = phone_number,
                address = address,
                username = full_name
            )
            return JsonResponse({'message': 'You have registered successfully.', 'user_id': user.id})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def Home(request):
    available_slots = AvailableSlots.objects.filter(display=True).values()
    context = {
        'available_slots': available_slots
    }
    return render(request, 'home.html', context=context)
