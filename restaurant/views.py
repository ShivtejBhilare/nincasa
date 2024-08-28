
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import MenuItem, Reservation, CarouselImage

from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    menu_items = MenuItem.objects.all()
    carousel_images = CarouselImage.objects.all()
    return render(request, 'restaurant/home.html', {
        'menu_items': menu_items,
        'carousel_images': carousel_images,
    })

def booking(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        guests = request.POST['guests']
        reservation = Reservation(name=name, email=email, date=date, time=time, guests=guests)
        reservation.save()
        return redirect('home')  # Redirect after successful booking
    return render(request, 'restaurant/booking.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {
        'menu_items': menu_items,
    })

def contact(request):
    if request.method == 'POST':
        # Handle form submission (you can add your logic here)
        return redirect('home')  # Redirect after successful submission
    return render(request, 'restaurant/contact.html')

@login_required
@user_passes_test(lambda user: user.is_staff)
def dashboard(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            # Handle menu item addition
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            image = request.FILES['image']
            menu_item = MenuItem(name=name, description=description, price=price, image=image)
            menu_item.save()
        elif 'video_url' in request.POST or 'image' in request.FILES:
            # Handle carousel image or video addition
            image = request.FILES.get('image')
            video_url = request.POST.get('video_url')
            caption = request.POST['caption']
            carousel_image = CarouselImage(image=image, video_url=video_url, caption=caption)
            carousel_image.save()
        return redirect('dashboard')

    bookings = Reservation.objects.all()
    carousel_images = CarouselImage.objects.all()
    menu_items = MenuItem.objects.all()
    context = {
        'bookings': bookings,
        'carousel_images': carousel_images,
        'menu_items': menu_items,
    }
    return render(request, 'restaurant/dashboard.html', context)

@login_required
@user_passes_test(lambda user: user.is_staff)
def edit_menu_item(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES.get('image')

        menu_item.name = name
        menu_item.description = description
        menu_item.price = price
        if image:
            menu_item.image = image
        menu_item.save()

        return redirect('dashboard')

    return render(request, 'restaurant/edit_menu_item.html', {'menu_item': menu_item})