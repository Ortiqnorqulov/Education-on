from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils import translation

from course.models import Courses, Category, CourseDetail
from home.models import ContactMessage, Informations, Slider, NewsLatter, Aboutus, Blog, Adversiting, Comment_blog, \
    FAQs, OurTeam, CourseBuy
from creatoradmin.forms import SignUpForm, UserUpdateForm, \
    EditCategoryForm, AddCategoryForm, AddInformationForm, EditInformationForm, EditSliderForm, \
    AppandSliderForm, UserPermissonForm, EditContactForm, EditFAQSForm, \
    AppandFAQSForm, EditAboutForm, AppandAboutForm, EditNewsForm, AppandNewsForm, \
    EditNewsCommentForm, ProfileCreatorUpdateForm, UserClientUpdateForm, \
    ProfileClinetUpdateForms, AppandAversitingForm, EditAdversitingForm, AddCourseForm, EditCourseForm, AddTeachersForm
from creatoradmin.models import Client, Creator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# - - - - - - - - - - - - - - - REGISTRATION - - - - - - - - - - - - - - - #
from order.models import CourseCarts, ShopCart


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Client()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            return redirect('home')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Auth/register.html', context)


# - - - - - - - - - - - - - - - LOGIN - - - - - - - - - - - - - - - #

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Creator.objects.get(user_id=request.user.id)
                return redirect('creator')
            except:
                try:
                    Client.objects.get(user_id=request.user.id)
                    return redirect('client')
                except:
                    return redirect('login_form')
        else:
            messages.warning(request, "Login Error! User name or Password is incorrect")
            return redirect('login_form')

    return render(request, 'Auth/login.html')


# - - - - - - - - - - - - - - - CREATOR / ADMIN - - - - - - - - - - - - - - - #

@login_required(login_url='login_form')
def creator(request):
    try:
        creator = Creator.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    category = Category.objects.all()
    course = Courses.objects.all()
    client = Client.objects.all()
    contact = ContactMessage.objects.all()
  #  order = Order.objects.all()
  #  order_product = OrderProduct.objects.all()
  #  order_product_count = order_product.count()
    category_count = category.count()
    product_count = course.count()
    client_count = client.count()
    contact_count = contact.count()
    context = {
        'client': client,
        'creator': creator,
        'category': category,
        'course': course,
        'contact': contact,
     #   'order': order,
      #  'order_product': order_product,
        'category_count': category_count,
        'product_count': product_count,
        'client_count': client_count,
        'contact_count': contact_count,
      #  'order_product_count': order_product_count,
    }
    return render(request, 'Creator/creator.html', context)


@login_required(login_url='login_form')
def register_creator(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Creator()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('user_update')
        else:
            messages.warning(request, form.errors)
            return redirect('register_creator')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Auth/register_creator.html', context)


# - - - - - - - - - - - - - - - Client - - - - - - - - - - - - - - - #

def user_update_client(request):
    if request.method == 'POST':
        user_form = UserClientUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileClinetUpdateForms(request.POST, request.FILES, instance=request.user.client)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('client')
    else:
        user_form = UserClientUpdateForm(instance=request.user)
        profile_form = ProfileClinetUpdateForms(instance=request.user.client)
        client = Client.objects.get(user=request.user)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'client': client,
        }
        return render(request, 'Client/user_update_client.html', context)


def user_password_client(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile password successfully updated')
            return redirect('client')
        else:
            messages.error(request, 'Eror password')
            return redirect('user_password_client')
    else:
        form = PasswordChangeForm(request.user)
        client = Client.objects.get(user=request.user)
        context = {
            'form': form,
            'client': client,
        }
        return render(request, 'Client/user_password_client.html', context)


def user_orders_product(request):
    current_user = request.user
    client = Client.objects.get(user=request.user)
   # coursee = CourseCarts.objects.filter(user_id=current_user.id)
    shopcart_ = ShopCart.objects.filter(user_id=client)
    corsedetail = CourseDetail.objects.all()
    context = {
        'shopcart_': shopcart_,
      #  'coursee': coursee,
        'client': client,
        'corsedetail': corsedetail,
    }
    return render(request, 'Client/page_order_detail.html', context)





@login_required(login_url='login_form')
def user_orders_product_detail(request, id, oid):
    current_user = request.user
    coursee = CourseCarts.objects.get(user_id=current_user.id, id=oid)
    client = Client.objects.get(user=request.user)
    context = {
        'client': client,
        'coursee': coursee,
    }
    return render(request, 'Client/page_order_detail.html', context)


# - - - - - - - - - - - - - - - USER PROFILE - - - - - - - - - - - - - - - #

@login_required(login_url='login_form')
def client(request):
    try:
        client = Client.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')

    if request.method == 'POST':
        user_form = UserClientUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileClinetUpdateForms(request.POST, request.FILES, instance=request.user.client)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('client')
    else:
        user_form = UserClientUpdateForm(instance=request.user)
        profile_form = ProfileClinetUpdateForms(instance=request.user.client)
        client = Client.objects.get(user=request.user)

    #current_user = request.user
    ordeer = CourseBuy.objects.all()
#    order_product_count = order_product.count()
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'client': client,
        'ordeer': ordeer,
#        'order_product_count': order_product_count,

    }
    return render(request, 'Client/page_accaunt.html', context)

# - - - - - - - - - - - - - - - LOGOUT - - - - - - - - - - - - - - - #

def logout_form(request):
    logout(request)
    return redirect('home')


# - - - - - - - - - - - - - - - PASSWORD UPDATE - - - - - - - - - - - - - - - #


def password_change(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

@login_required(login_url='login_form')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('creator')
        else:
            messages.error(request, 'Error password')
            return redirect('user_password')
    else:
        form = PasswordChangeForm(request.user)
        creator = Creator.objects.get(user=request.user)
        context = {
            'form': form,
            'creator': creator,
        }
        return render(request, 'Auth/user_password.html', context)


# - - - - - - - - - - - - - - - USER UPDATE - - - - - - - - - - - - - - - #


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileCreatorUpdateForm(request.POST, request.FILES, instance=request.user.creator)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('creator')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileCreatorUpdateForm(instance=request.user.creator)
        creator = Creator.objects.get(user=request.user)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'creator': creator,
        }
        return render(request, 'Auth/user_update.html', context)


# - - - - - - - - - - - - - - - INFORMATION - - - - - - - - - - - - - - - #

def information_add(request):
    if request.method == 'POST':
        form = AddInformationForm(request.POST, request.FILES)
        if form.is_valid():
            information = Informations()
            information.title_uz = form.cleaned_data.get('title_uz')
            information.title_en = form.cleaned_data.get('title_en')
            information.title_ru = form.cleaned_data.get('title_ru')
            information.country = form.cleaned_data.get('country')
            information.city = form.cleaned_data.get('city')
            information.address_en = form.cleaned_data.get('address_en')
            information.address_ru = form.cleaned_data.get('address_ru')
            information.address_uz = form.cleaned_data.get('address_uz')
            information.phone = form.cleaned_data.get('phone')
            information.email = form.cleaned_data.get('email')
            information.telegram = form.cleaned_data.get('telegram')
            information.instagram = form.cleaned_data.get('instagram')
            information.facebook = form.cleaned_data.get('facebook')
            information.twitter = form.cleaned_data.get('twitter')
            information.location = form.cleaned_data.get('location')
            if request.FILES:
                information.logo = request.FILES['icon']
            if request.FILES:
                information.icon = request.FILES['logo']
            information.description_uz = form.cleaned_data.get('description_uz')
            information.description_en = form.cleaned_data.get('description_en')
            information.description_ru = form.cleaned_data.get('description_ru')
            information.status = form.cleaned_data.get('status')
            information.save()
            messages.success(request, 'Your account has been updated')
            return redirect('information_update')
        else:
            messages.error(request, 'Error password')
            return redirect('information_add')
    form = AddInformationForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Information/information_add.html', context)


def information_update(request):
    information = Informations.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(information, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        information = paginator.page(page)
    except PageNotAnInteger:
        information = paginator.page(1)
    except EmptyPage:
        information = paginator.page(paginator.num_pages)
    context = {
        'information': information,
        'creator': creator,
    }
    return render(request, 'Information/information_update.html', context)


def information_edit(request, id):
    information = Informations.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditInformationForm(request.POST, request.FILES, instance=information)
        if request.FILES:
            information.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('information_update')
        else:
            messages.error(request, 'Error password')
            return redirect("information_edit")
    else:
        form = EditInformationForm(instance=information)
        context = {
            'form': form,
            'creator': creator,
            'information': information,
        }
        return render(request, 'Information/information_edit.html', context)


def information_delete(request, id):
    information = Informations.objects.get(pk=id)
    information.delete()
    return redirect('information_update')


def information_delete_all(request):
    information = Informations.objects.all()
    information.delete()
    return redirect('information_update')


# - - - - - - - - - - - - - - - CATEGORY - - - - - - - - - - - - - - - #

def category_add(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title_uz = form.cleaned_data.get('title_uz')
            category.title_en = form.cleaned_data.get('title_en')
            category.title_ru = form.cleaned_data.get('title_ru')
            category.description_uz = form.cleaned_data.get('description_uz')
            category.description_en = form.cleaned_data.get('description_en')
            category.description_ru = form.cleaned_data.get('description_ru')
            if request.FILES:
                category.image = request.FILES['image']
            category.slug = form.cleaned_data.get('slug')
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('category_update')
    form = AddCategoryForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Category/add_category.html', context)


def category_update(request):
    category = Category.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(category, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        category = paginator.page(page)
    except PageNotAnInteger:
        category = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'creator': creator,
    }
    return render(request, 'Category/category_update.html', context)


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('category_update')
        else:
            messages.error(request, 'Error password')
            return redirect('category_edit')
    else:
        form = EditCategoryForm(instance=category)
        context = {
            'form': form,
            'creator': creator,
            'category': category,
        }
        return render(request, 'Category/category_edit.html', context)




def category_delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category_update')


def category_delete_all(request):
    category = Category.objects.all()
    category.delete()
    return redirect('category_update')


# - - - - - - - - - - - - - - - Course - - - - - - - - - - - - - - - #

def course_add(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = Courses()
            course.category = form.cleaned_data.get('category')
            course.teacher = form.cleaned_data.get('teacher')
            course.title_en = form.cleaned_data.get('title_en')
            course.title_ru = form.cleaned_data.get('title_ru')
            course.title_uz = form.cleaned_data.get('title_uz')
            course.old_price = form.cleaned_data.get('old_price')
            course.sell_price = form.cleaned_data.get('sell_price')
            if request.FILES:
                course.image = request.FILES['image']
            course.slug = form.cleaned_data.get('slug')
            course.status = form.cleaned_data.get('status')
            course.description_en = form.cleaned_data.get('description_en')
            course.description_ru = form.cleaned_data.get('description_ru')
            course.description_uz = form.cleaned_data.get('description_uz')
            course.lenguage_en = form.cleaned_data.get('lenguage_en')
            course.lenguage_ru = form.cleaned_data.get('lenguage_ru')
            course.lenguage_uz = form.cleaned_data.get('lenguage_uz')
            course.duration = form.cleaned_data.get('duration')
            course.level_en = form.cleaned_data.get('level_en')
            course.level_ru = form.cleaned_data.get('level_ru')
            course.level_uz = form.cleaned_data.get('level_uz')
            course.link = form.cleaned_data.get('link')
            course.save()
            return redirect('course_update')
    form = AddCourseForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Courses/add-cource.html', context)

def course_update(request):
    course = Courses.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(course, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        course = paginator.page(page)
    except PageNotAnInteger:
        course = paginator.page(1)
    except EmptyPage:
        course = paginator.page(paginator.num_pages)
    context = {
        'course': course,
        'creator': creator,
    }
    return render(request, 'Courses/course_update.html', context)


def course_edit(request, id):
    course = Courses.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, request.FILES, instance=course)
        if request.FILES:
            course.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('course_update')
        else:
            messages.error(request, 'Error password')
            return redirect('course_edit')
    else:
        form = EditCourseForm(instance=course)
        context = {
            'form': form,
            'creator': creator,
            'course': course,
        }

        return render(request, 'Courses/course_edit.html', context)


def course_all(request):
    course = Courses.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'Courses/courses.html', context)


def course_delete(request, id):
    course = Courses.objects.get(pk=id)
    course.delete()
    return redirect('course_update')


def course_delete_all(request):
    course = Courses.objects.all()
    course.delete()
    return redirect('course_update')


# - - - - - - - - - - - - - - - - TEACHER - - - - - - - - - - - - - - #

def teacher(request):
    teachers = OurTeam.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'Teacher/teachers.html', context)


def addteacher(request):
    if request.method == 'POST':
        form = AddTeachersForm(request.POST, request.FILES)
        if form.is_valid():
            news = OurTeam()
            news.title_uz = form.cleaned_data.get('title_uz')
            news.title_en = form.cleaned_data.get('title_en')
            news.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                news.image = request.FILES['image']
            news.status = form.cleaned_data.get('status')
            news.description_uz = form.cleaned_data.get('description_uz')
            news.description_en = form.cleaned_data.get('description_en')
            news.description_ru = form.cleaned_data.get('description_ru')
            news.telegram = form.cleaned_data.get('telegram')
            news.instagram = form.cleaned_data.get('instagram')
            news.twitter = form.cleaned_data.get('twitter')
            news.facebook = form.cleaned_data.get('facebook')
            news.save()
            return redirect('creator')
    form = AddTeachersForm()
    context = {
        'form': form,
    }
    return render(request, 'Teacher/teacher-profile.html', context)


# - - - - - - - - - - - - - - - NEWS - - - - - - - - - - - - - - - #

def news_add(request):
    if request.method == 'POST':
        form = AppandNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = Blog()
            news.title_uz = form.cleaned_data.get('title_uz')
            news.title_en = form.cleaned_data.get('title_en')
            news.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                news.image = request.FILES['image']
            news.status = form.cleaned_data.get('status')
            news.description_uz = form.cleaned_data.get('description_uz')
            news.description_en = form.cleaned_data.get('description_en')
            news.description_ru = form.cleaned_data.get('description_ru')
            news.save()
            return redirect('news_update')
    form = AppandNewsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Blog/news_add.html', context)


def news_update(request):
    news = Blog.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(news, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news': news,
        'creator': creator,
    }
    return render(request, 'Blog/news_update.html', context)


def news_edit(request, id):
    news = Blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditNewsForm(request.POST, request.FILES, instance=news)
        if request.FILES:
            news.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your news has been updated')
            return redirect('news_update')
        else:
            messages.error(request, 'Error password')
            return redirect('news_edit')
    else:
        form = EditNewsForm(instance=news)
        context = {
            'form': form,
            'creator': creator,
            'blog': news,
        }

        return render(request, 'Blog/news_edit.html', context)


def news_delete(request, id):
    news = Blog.objects.get(pk=id)
    news.delete()
    return redirect('news_update')


def news_delete_all(request):
    news = Blog.objects.all()
    news.delete()
    return redirect('news_update')


# - - - - - - - - - - - - - - - ABOUT - - - - - - - - - - - - - - - #

def about_add(request):
    if request.method == 'POST':
        form = AppandAboutForm(request.POST, request.FILES)
        if form.is_valid():
            about = Aboutus()
            about.title_uz = form.cleaned_data.get('title_uz')
            about.title_en = form.cleaned_data.get('title_en')
            about.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                about.image = request.FILES['image']
            about.status = form.cleaned_data.get('status')
            about.description_uz = form.cleaned_data.get('description_uz')
            about.description_en = form.cleaned_data.get('description_en')
            about.description_ru = form.cleaned_data.get('description_ru')
            about.save()
            return redirect('about_update')
    form = AppandAboutForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'About/add_about.html', context)


def about_update(request):
    about = Aboutus.objects.filter(status='True')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(about, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        about = paginator.page(page)
    except PageNotAnInteger:
        about = paginator.page(1)
    except EmptyPage:
        about = paginator.page(paginator.num_pages)
    context = {
        'about': about,
        'creator': creator,
    }
    return render(request, 'About/about_update.html', context)


def about_edit(request, id):
    about = Aboutus.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditAboutForm(request.POST, request.FILES, instance=about)
        if request.FILES:
            about.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('about_update')
        else:
            messages.error(request, 'Error password')
            return redirect('about_edit')
    else:
        form = EditAboutForm(instance=about)
        context = {
            'form': form,
            'creator': creator,
            'about': about,
        }

        return render(request, 'About/about_edit.html', context)


def about_delete(request, id):
    about = Aboutus.objects.get(pk=id)
    about.delete()
    return redirect('about_update')


def about_delete_all(request):
    about = Aboutus.objects.all()
    about.delete()
    return redirect('about_update')


# - - - - - - - - - - - - - - - FAQ - - - - - - - - - - - - - - - #

def faq_add(request):
    if request.method == 'POST':
        form = AppandFAQSForm(request.POST)
        if form.is_valid():
            faq = FAQs()
            faq.number = form.cleaned_data.get('number')
            faq.question_en = form.cleaned_data.get('question_en')
            faq.question_ru = form.cleaned_data.get('question_ru')
            faq.question_uz = form.cleaned_data.get('question_uz')
            faq.status = form.cleaned_data.get('status')
            faq.answer_uz = form.cleaned_data.get('answer_uz')
            faq.answer_en = form.cleaned_data.get('answer_en')
            faq.answer_ru = form.cleaned_data.get('answer_ru')
            faq.save()
            return redirect('faq_update')
    form = AppandFAQSForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Faq/faq_add.html', context)


def faq_update(request):
    faq = FAQs.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(faq, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        faq = paginator.page(page)
    except PageNotAnInteger:
        faq = paginator.page(1)
    except EmptyPage:
        faq = paginator.page(paginator.num_pages)
    context = {
        'faq': faq,
        'creator': creator,
    }
    return render(request, 'Faq/faq_update.html', context)


def faq_edit(request, id):
    faq = FAQs.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditFAQSForm(request.POST, request.FILES, instance=faq)
        if request.FILES:
            faq.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('faq_update')
        else:
            messages.error(request, 'Error password')
            return redirect('faq_edit')
    else:
        form = EditFAQSForm(instance=faq)
        context = {
            'form': form,
            'creator': creator,
            'faq': faq,
        }
        return render(request, 'Faq/faq_edit.html', context)


def faq_delete(request, id):
    faq = FAQs.objects.get(pk=id)
    faq.delete()
    return redirect('faq_update')


def faq_delete_all(request):
    faq = FAQs.objects.all()
    faq.delete()
    return redirect('faq_update')


# - - - - - - - - - - - - - - - NEWSLETTER - - - - - - - - - - - - - - - #

def newsletter_get(request):
    newsletter = NewsLatter.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(newsletter, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        newsletter = paginator.page(page)
    except PageNotAnInteger:
        newsletter = paginator.page(1)
    except EmptyPage:
        newsletter = paginator.page(paginator.num_pages)
    context = {
        'newsletter': newsletter,
        'creator': creator,
    }
    return render(request, 'Newslatter/newsletter_get.html', context)


def newsletter_delete(request, id):
    newsletter = NewsLatter.objects.get(pk=id)
    newsletter.delete()
    return redirect('newsletter_get')


def newsletter_delete_all(request):
    newsletter = NewsLatter.objects.all()
    newsletter.delete()
    return redirect('newsletter_get')


# - - - - - - - - - - - - - - - CONTACT - - - - - - - - - - - - - - - #

def contact_get(request):
    contact = ContactMessage.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(contact, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    context = {
        'contact': contact,
        'creator': creator,
    }
    return render(request, 'Contact/contact_get.html', context)


def contact_edit(request, id):
    contact = ContactMessage.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('contact_get')
        else:
            messages.error(request, 'Error password')
            return redirect('contact_edit')
    else:
        form = EditContactForm(instance=contact)
        context = {
            'form': form,
            'creator': creator,
            'contact': contact,
        }

        return render(request, 'Contact/contact_edit.html', context)


def contact_delete(request, id):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_get')


def contact_delete_all(request):
    contact = ContactMessage.objects.all()
    contact.delete()
    return redirect('contact_get')


# - - - - - - - - - - - - - - - NEWS COMMENT - - - - - - - - - - - - - - - #

def news_comment_get(request):
    comment = Comment_blog.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(comment, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context = {
        'comment': comment,
        'creator': creator,
    }
    return render(request, 'News_comment/news_comment_get.html', context)


def news_comment_edit(request, id):
    comment = Comment_blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditNewsCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('news_comment_get')
        else:
            messages.error(request, 'Error password')
            return redirect('news_comment_edit')
    else:
        form = EditNewsCommentForm(instance=comment)
        context = {
            'form': form,
            'creator': creator,
            'comment': comment,
        }

        return render(request, 'News_comment/news_comment_edit.html', context)


def news_comment_delete(request, id):
    news_comment = Comment_blog.objects.get(pk=id)
    news_comment.delete()
    return redirect('news_comment_get')


def news_comment_delete_all(request):
    news_comment = Comment_blog.objects.all()
    news_comment.delete()
    return redirect('news_comment_get')




# - - - - - - - - - - - - - - - USER PERMISSION - - - - - - - - - - - - - - - #

def user_add_permission(request, id):
    if request.method == 'POST':
        form = UserPermissonForm(request.POST, request.FILES)
        if form.is_valid():
            creator = Creator()
            creator.user = form.cleaned_data.get('user')
            # creator.phone = form.cleaned_data.get('phone')
            # creator.address = form.cleaned_data.get('address')
            # creator.city = form.cleaned_data.get('city')
            if request.FILES:
                creator.image = request.FILES['image']
            # creator.country = form.cleaned_data.get('country')
            client = Client.objects.get(pk=id)
            client.delete()
            creator.save()
            return redirect('creator')
    form = UserPermissonForm()
    client = Client.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
        'client': client,
    }
    return render(request, 'Creator_add/add_user_permission.html', context)


def users_get(request):
    users = Client.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(users, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'users': users,
        'creator': creator,
    }
    return render(request, 'Creator_add/get_users.html', context)


def users_delete(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('users_get')


def users_delete_all(request):
    client = Client.objects.all()
    client.delete()
    return redirect('users_get')



# - - - - - - - - - - - - - - - SLIDER - - - - - - - - - - - - - - - #

def slider_add(request):
    if request.method == 'POST':
        form = AppandSliderForm(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title_en = form.cleaned_data.get('title_en')
            slider.title_ru = form.cleaned_data.get('title_ru')
            slider.title_uz = form.cleaned_data.get('title_uz')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.description_uz = form.cleaned_data.get('description_uz')
            slider.description_en = form.cleaned_data.get('description_en')
            slider.description_ru = form.cleaned_data.get('description_ru')
            slider.save()
            return redirect('slider_update')
    form = AppandSliderForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Slider/slider_add.html', context)


def slider_update(request):
    slider = Slider.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(slider, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        slider = paginator.page(page)
    except PageNotAnInteger:
        slider = paginator.page(1)
    except EmptyPage:
        slider = paginator.page(paginator.num_pages)
    context = {
        'slider': slider,
        'creator': creator,
    }
    return render(request, 'Slider/slider_update.html', context)


def slider_edit(request, id):
    slider = Slider.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditSliderForm(request.POST, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('slider_update')
        else:
            messages.error(request, 'Error password')
            return redirect('slider_edit')
    else:
        form = EditSliderForm(instance=slider)
        context = {
            'form': form,
            'creator': creator,
            'slider': slider,
        }

        return render(request, 'Slider/slider_edit.html', context)


def slider_delete(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('slider_update')


def slider_delete_all(request):
    slider = Slider.objects.all()
    slider.delete()
    return redirect('slider_update')


# - - - - - - - - - - - - - - - ADVERSITING - - - - - - - - - - - - - - - #

def add_adversiting(request):
    if request.method == 'POST':
        form = AppandAversitingForm(request.POST, request.FILES)
        if form.is_valid():
            adversiting = Adversiting()
            adversiting.title_en = form.cleaned_data.get('title_en')
            adversiting.title_ru = form.cleaned_data.get('title_ru')
            adversiting.title_uz = form.cleaned_data.get('title_uz')
            adversiting.description_en = form.cleaned_data.get('description_en')
            adversiting.description_ru = form.cleaned_data.get('description_ru')
            adversiting.description_uz = form.cleaned_data.get('description_uz')
            if request.FILES:
                adversiting.image = request.FILES['image']
            adversiting.status = form.cleaned_data.get('status')
            adversiting.save()
            return redirect('adversiting_update')
    form = AppandAversitingForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Adversiting/addadversiting.html', context)


def adversiting_update(request):
    adversiting = Adversiting.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(adversiting, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        adversiting = paginator.page(page)
    except PageNotAnInteger:
        adversiting = paginator.page(1)
    except EmptyPage:
        adversiting = paginator.page(paginator.num_pages)
    context = {
        'adversiting': adversiting,
        'creator': creator,
    }
    return render(request, 'Adversiting/adversiting_update.html', context)


def adversiting_edit(request, id):
    adversiting = Adversiting.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditAdversitingForm(request.POST, request.FILES, instance=adversiting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('adversiting_update')
        else:
            messages.error(request, 'Error password')
            return redirect('adversiting_edit')
    else:
        form = EditAdversitingForm(instance=adversiting)
        context = {
            'form': form,
            'creator': creator,
            'adversiting': adversiting,
        }

        return render(request, 'Adversiting/adversiting_edit.html', context)


def adversiting_delate(request, id):
    adversiting = Adversiting.objects.get(pk=id)
    adversiting.delete()
    return redirect('adversiting_update')


def adversiting_delate_all(request):
    adversiting = Adversiting.objects.all()
    adversiting.delete()
    return redirect('adversiting_update')


# - - - - - - - - - - - - - - - SEARCH - - - - - - - - - - - - - - - #

def searched(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        course = Courses.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='True').order_by('-id')
        context = {
            'category': category,
            'searched': searched,
            'course': course,
        }
        return render(request, 'Searched/searched.html', context)


# - - - - - - - - - - - - - - - LANGUAGE - - - - - - - - - - - - - - - #

def selectlanguage_admin(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("creator")


def selectlanguage_client(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("client")



# - - - - - - - - - - - - - - - Search - - - - - - - - - - - - - - - #

def search_dashbourd(request):
    if request.method == 'POST':
        searched = request.POST['search']
        course = Courses.objects.filter(title__contains=searched)
        course_count = course.count()
        category = Category.objects.filter(status='TRUE')
        creator = Creator.objects.get(user=request.user)
        info = Informations.objects.all().order_by('-id')[:1]
        context = {
            'searched': searched,
            'course': course,
            'course_count': course_count,
            'category': category,
            'creator': creator,
            'info': info,
        }
        return render(request, 'Searched/dashbourd_search.html', context)


