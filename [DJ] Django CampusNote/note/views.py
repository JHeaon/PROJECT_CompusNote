from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import Post
from .models import user
from .models import QAPost
from .models import Subject
from .models import Shop
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['password']

        if not (username and password):
            print("no")
        else:
            return render(request, 'users/main.html')

    else:
        print("no")
        return render(request, 'index.html')


def index_signup(request):

    if request.method == "POST":
        _user = user()
        _user.user_id = request.POST['id']
        _user.user_pwd = request.POST['password']
        _user.user_nickname = request.POST['nickname']
        _user.user_name = request.POST['name']
        _user.user_university = request.POST['school']
        _user.user_e_mail = request.POST['email']
        _user.user_phonenumber = request.POST['phonenumber']
        _user.save()
        return render(request, 'index.html')

    else:
        return render(request, 'index_signup.html')


def home(request):
    return render(request, "Home.html")


def free_board(request):
    posts = Post.objects.all()
    return render(request, "Free_board.html", {'posts': posts})


def bulletinboard(request):
    posts = Subject.objects.all()
    return render(request, "bulletinboard.html", {"posts": posts})


def Q_A(request):
    QAPosts = QAPost.objects.all()
    return render(request, "Q&A.html", {'posts': QAPosts})


def mypage(request):
    return render(request, "mypage.html")


def cart2(request):
    return render(request, "cart2.html")


@csrf_exempt
def upload_form(request):
    if request.method == "POST":
        _post = Post()
        _post.title = request.POST['title']
        _post.content = request.POST['content']
        _post.tag = request.POST['tag']
        _post.file = request.POST['file']
        _post.save()

        posts = Post.objects.all()

        return render(request, "./Free_board.html", {"posts": posts})

    else:
        return render(request, "Common_Upload_Form.html")


@csrf_exempt
def QA_upload_form(request):
    if request.method == "POST":
        _post = QAPost()
        _post.title = request.POST['title']
        _post.content = request.POST['content']
        _post.tag = request.POST['tag']
        _post.file = request.POST['file']
        _post.save()

        posts = QAPost.objects.all()
        return render(request, "./Q&A.html", {"posts": posts})

    else:
        return render(request, "QA_Upload_Form.html")


def Q_A_detail(request, post_id):
    post = QAPost.objects.get(id=post_id)
    return render(request, "Common_Detail.html", {"post": post})


def Common_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "Common_Detail.html", {"post": post})


def computersearch(request, post_id):
    post = Subject.objects.get(id=post_id)
    shop = Shop.objects.all()
    return render(request, "computerSearch.html", {"post": post, "shop": shop})


@csrf_exempt
def sell_upload_form(request, post_id):
    if request.method == "POST":
        post = Subject.objects.get(id=post_id)
        shop = Shop()
        shop.title = request.POST['title']
        shop.price = request.POST['price']
        shop.content = request.POST['text']
        shop.file = request.POST['file']
        shop.tag = request.POST['hashTag']
        shop.save()
        return render(request, "home.html")
    else:
        return render(request, "Sell_Upload_Form.html")


def sell_detail(request):
    return render(request, "Sell_Detail.html")


def payment(request):
    return render(request, "payment.html")


def charge(request):
    return render(request, "charge.html")


def chargecomplete(request):
    return render(request, "chargecomplete.html")


def paycomplete(request):
    return render(request, "paycomplete.html")

# path('charge/', views.charge, name="charge"),
#     path('chargecomplete/', views.chargecomplete, name="chargecomplete"),
#     path('paycomplete/', views.paycomplete, name="paycomplete"),
