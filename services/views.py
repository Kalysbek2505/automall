from django.shortcuts import render, redirect
from .models import Service, Review, GalleryImage, Contact
from .forms import AppointmentForm, ContactForm
from django.http import HttpResponse

def home(request):
    return render(request, 'services/home.html')

def services(request):
    all_services = Service.objects.all()
    return render(request, 'services/services.html', {'services': all_services})


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'services/book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'services/appointment_success.html')


def reviews(request):
    all_reviews = Review.objects.all()
    return render(request, 'services/reviews.html', {'reviews': all_reviews})



# def gallery(request):
#     images = GalleryImage.objects.all()
#     return render(request, 'index.html', {'portfolio_items': images})


# def index(request):
#     return render(request, 'index.html')
def contact_view(request):
    images = GalleryImage.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в базу данных
            Contact.objects.create(
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number']
            )
            return HttpResponse("Данные сохранены.")
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'portfolio_items': images,
    }

    return render(request, 'index.html', context)
        
            
