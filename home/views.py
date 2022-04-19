from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from course.models import Courses, Category
from creatoradmin.models import Client
from home.forms import ContactForm, NewsLatterForm, CourseCommentForm, CourseBuyForm
from home.models import ContactMessage, Informations, Slider, Blog, OurTeam, Aboutus, NewsLatter, Comment_blog, \
    FAQs, Adversiting, CourseCommentsMessage, CourseBuy
from django.utils import translation

def home(request):
    course = Courses.objects.all()
    slider = Slider.objects.all()
    blog = Blog.objects.filter(status=True).order_by('-id')
    ourteam = OurTeam.objects.all()
    info = Informations.objects.all()
    category = Category.objects.filter(status=True).order_by('?')
    adversiting = Adversiting.objects.all()
    course_count = course.count()
    client = Client.objects.all()
    client_count = client.count()
    context = {
        'course': course,
        'slider': slider,
        'blog': blog,
        'ourteam': ourteam,
        'info': info,
        'category': category,
        'adversiting': adversiting,
        'course_count': course_count,
        'client_count': client_count,
    }
    return render(request, 'index.html', context)

def header(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    context = {
        'info': info,
        'category': category,
    }
    return render(request, 'header.html', context)

def footer(request):
    course = Courses.objects.all()
    ourteam = OurTeam.objects.all()
    info = Informations.objects.all()
    category = Category.objects.all()
    context = {
        'course': course,
        'ourteam': ourteam,
        'info': info,
        'category': category,
    }
    return render(request, 'footer.html', context)

def course_detail(request, id, slug):
    if request.method == 'POST':
        form = CourseCommentForm(request.POST)
        if form.is_valid():
            data = CourseCommentsMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = CourseCommentForm
    course = Courses.objects.get(pk=id)
    info = Informations.objects.all()
    category = Category.objects.all()
    coment = CourseCommentsMessage.objects.all()
    client = Client.objects.get(user=request.user)
    context = {
        'course': course,
        'info': info,
        'category': category,
        'form': form,
        'coment': coment,
        'client': client,
    }
    return render(request, 'courses-details.html', context)


def coursebuy(request):
    if request.method == 'POST':
        form = CourseBuyForm(request.POST)
        if form.is_valid():
            data = CourseBuy()
            data.username = form.cleaned_data['username']
            data.title = form.cleaned_data['title']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = CourseBuyForm
    context = {
        'form': form,
    }
    return render(request, 'courses-details.html', context)


def category_course(request, id):
    coursess = Courses.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {
        'coursess': coursess,
        'category': category,
    }
    return render(request, 'category_course.html', context)

def about(request):
    course = Courses.objects.all()
    aboutus = Aboutus.objects.filter(status='True')[:1]
    ourteam = OurTeam.objects.all()
    info = Informations.objects.all()
    category = Category.objects.all()
    context = {
        'course': course,
        'aboutus': aboutus,
        'ourteam': ourteam,
        'info': info,
        'category': category,
    }
    return render(request, 'about-1.html', context)


def coursesall(request):
    course = Courses.objects.all()
    info =Informations.objects.all()
    category = Category.objects.all()
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
        'category': category,
        'info': info,
    }
    return render(request, 'courses.html', context)


def blog(request):
    blog = Blog.objects.all()
    ourteam = OurTeam.objects.all()
    info = Informations.objects.all()
    course = Courses.objects.all()
    category = Category.objects.all()
    paginator = Paginator(blog, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'ourteam': ourteam,
        'info': info,
        'course': course,
        'category': category,
    }
    return render(request, 'blog.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = ContactForm
    info = Informations.objects.all()
    ourteam = OurTeam.objects.all()
    category = Category.objects.all()
    context = {
        'form': form,
        'info': info,
        'ourteam': ourteam,
        'category': category,
    }
    return render(request, 'contact-us.html', context)


def faq(request):
    info = Informations.objects.all()
    faq = FAQs.objects.all()
    category = Category.objects.all()
    context = {
        'info': info,
        'faq': faq,
        'category': category,
    }
    return render(request, 'faq.html', context)


def newsLatter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLatterForm(request.POST)
        if form.is_valid():
            data = NewsLatter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning emailingiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)




def eror404(request):
    return render(request, 'error-404.html')



def blog_detail(request,id):
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    blog_detail = Blog.objects.get(pk=id)
    blog = Blog.objects.filter(status='True').order_by('?')[:4]
    comment_blog = Comment_blog.objects.filter(blog_id=id, status='True')
    category = Category.objects.all()
    course = Courses.objects.all()
    context = {
        'blog_detail': blog_detail,
        'blog': blog,
        'info': info,
        'comment_blog': comment_blog,
        'category': category,
        'course': course,
    }
    return render(request, 'blog-details.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        course = Courses.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='TRUE')
        info = Informations.objects.all().order_by('-id')[:1]
        context = {
            'searched': searched,
            'course': course,
            'category': category,
            'info': info,
        }
        return render(request, 'search.html', context)


def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return redirect("home")
