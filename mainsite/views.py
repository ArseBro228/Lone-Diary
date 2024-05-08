from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.datetime_safe import datetime
from django.views import View

from .forms import UserCreationForm, PostForm
from .models import Lesson, Course, Category


# Create your views here.
def index(request):
    return render(request, 'mainsite/index.html')


def news(request):
    posts = Lesson.objects.all().order_by("-published_date")
    context = {
        'posts': posts,
    }

    return render(request, 'mainsite/news.html', context)


# def login(request):
#     return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logged_out.html')


def profile(request):
    return render(request, 'mainsite/profile.html')


def subjects(request):
    courses = Course.objects.all()
    context = {
        'courses': [
            {
                'id': course.id,
                'title': course.title,
                'posts_amount': course.lesson_set.count(),
            }
            for course in courses
        ]
    }
    return render(request, 'mainsite/subjects.html', context)


def contacts(request):
    return render(request, 'mainsite/contacts.html')


def posts(request, course_id):
    course = Course.objects.get(pk=course_id)
    posts = course.lesson_set.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        posts = posts.filter(category__name=selected_category)
    context = {
        'course_title': course.title,
        'posts': posts,
        'course_id': course.id,
        'categories': categories,
    }

    return render(request, 'mainsite/subjects/posts.html', context)


def post(request, title=None):
    post = get_object_or_404(Lesson, title=title)
    context = {"post": post}
    return render(request, 'mainsite/post.html', context)


def add_post(request, course_id = None):
    now = datetime.now()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now
            post.user = request.user
            post.course = Course.objects.get(pk=course_id)
            post.save()

    form = PostForm()
    context = {"form": form, "course_id": course_id}
    return render(request, 'mainsite/add_post.html', context)


class RegisterUser(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
