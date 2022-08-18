"""CampusNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.index_signup, name='index_signup'),


    path('home/', views.home, name="home"),
    path('mypage/', views.mypage, name="mypage"),

    path('free_board/', views.free_board, name="free_board"),
    path("free_borad/<int:post_id>/", views.Common_detail, name="Common_detail"),


    path('bulletinboard/', views.bulletinboard, name="bulletinboard"),
    path('bulletinboard/<int:post_id>/',
         views.computersearch, name="computersearch"),
    path('bulletinboard/<int:post_id>/sell_upload_form/',
         views.sell_upload_form, name="sell_upload_form"),

    # path('bulletinboard/<int:post_id>/sell_detail/<int:shop_id>',
    #      views.sell_detail, name="sell_detail"),

    path('sell_detail/', views.sell_detail, name="sell_detail"),
    path('payment/', views.payment, name="payment"),
    path('charge/', views.charge, name="charge"),
    path('chargecomplete/', views.chargecomplete, name="chargecomplete"),
    path('paycomplete/', views.paycomplete, name="paycomplete"),



    path('Q&A/', views.Q_A, name="Q&A"),
    path('Q&A/<int:post_id>', views.Q_A_detail, name="Q&A_detail"),
    path('QA_Upload_Form/', views.QA_upload_form, name="QA_upload_form"),

    path('Commom_Upload_Form/', views.upload_form, name="upload_form"),
    path('cart2/', views.cart2, name="cart2"),
]
