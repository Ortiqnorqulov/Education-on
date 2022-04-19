from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from course.models import Courses
from creatoradmin.models import Client
from home.models import Informations
from order.forms import CoursecartForm, OrderForm
from order.models import ShopCart, CourseCarts, Order
from django.utils.crypto import get_random_string


@login_required(login_url='login_form')
def addtocart(request, pk):
    course = Courses.objects.get(id=pk)
    current_user = request.user
    user = Client.objects.get(user=request.user)
    shopcart = ShopCart.objects.filter(user=user)
    if request.method == 'POST':
        form = CoursecartForm(request.POST)
        if form.is_valid():
            data = CourseCarts()
            data.user = form.cleaned_data['user']
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.country = form.cleaned_data['country']
            data.city = form.cleaned_data['city']
            data.title = form.cleaned_data['title']
            data.price = form.cleaned_data['price']
            if request.FILES:
                data.image = request.FILES['image']
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = CoursecartForm
    course = Courses.objects.get(id=pk)
    current_user = request.user
    user = Client.objects.get(user=request.user)
    shopcart = ShopCart.objects.filter(user=user)
    context = {
        'course': course,
        'user': user,
        'current_user': current_user,
        'shopcart': shopcart,
        'form': form,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login_form')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Shop Cart!")
    return redirect('shopcart')


def orderproduct(request):

    current_user = request.user

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data.get('first_name', None)
            data.last_name = form.cleaned_data.get('last_name', None)
            data.address = form.cleaned_data.get('address', None)
            data.phone = form.cleaned_data.get('phone', None)
            data.country = form.cleaned_data.get('country', None)
            data.city = form.cleaned_data.get('city', None)
            data.email = form.cleaned_data.get('email', None)
            data.feedback = form.cleaned_data.get('feedback', None)
            data.user_id = request.user.id
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper()  # random code
            data.code = ordercode
            data.save()

            client = Client.objects.get(user=request.user)
            shopcart_ = CourseCarts.objects.filter(user=client)
            for rs in shopcart_:
                detail = CourseCarts()
                detail.order_id = data.id  # Order id
                detail.course_id = rs.course_id
                detail.user_id = current_user.id
                detail.price = rs.course.sell_price
                detail.save()
                course = Courses.objects.get(id=rs.product_id)
                course.save()

            CourseCarts.objects.filter(user=client).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed! Thank you!")
            return render(request, 'index.html', {'ordercode': ordercode})
        else:
            messages.warning(request, form.errors)
            return redirect('orderproduct')

    form = OrderForm
    client = Client.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user_id=client)
    info = Informations.objects.all().order_by('-id')[:1]
    context = {
        'shopcart': shopcart_,
        'client': client,
        'form': form,
        'info': info,
    }

    return render(request, 'checkout.html', context)