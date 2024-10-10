"""
Definition of urls for SchoolCommunityForums.
"""

from datetime import datetime
from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views


urlpatterns = [
    #登录注册
    path('login/', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('register', views.register,name='register'),

    path('', views.index, name='index'),
    
    #资讯
    path('schoolNew/', views.schoolNew,name='schoolNew'),
    path('schoolNewDetail', views.schoolNewDetail,name='schoolNewDetail'),
    path('schoolNewDetailComments', views.schoolNewDetailComments,name='schoolNewDetailComments'),
    path('schoolNewSeach', views.schoolNewSeach,name='schoolNewSeach'),    
   
    #个人信息
    path('userInfo', views.userInfo,name='userInfo'),
    

    #二手市场
    path('goods', views.goods,name='goods'),
    path('goodsDetail', views.goodsDetail,name='goodsDetail'),
    path('myGoods', views.myGoods,name='myGoods'), 
    path('myGoodsAdd', views.myGoodsAdd,name='myGoodsAdd'), 
    path('myGoodsEdit', views.myGoodsEdit,name='myGoodsEdit'), 
    path('myGoodsDelete', views.myGoodsDelete,name='myGoodsDelete'), 
    #path('goodsDetail/<id>', views.goodsDetail,name='goodsDetail'), 
    path('goodsDetailComments', views.goodsDetailComments,name='goodsDetailComments'), 
    

    #社区论坛
    path('communityForums', views.communityForums,name='communityForums'),
    path('communityForumsDetail', views.communityForumsDetail,name='communityForumsDetail'),
    path('myCommunityForums', views.myCommunityForums,name='myCommunityForums'), 
    path('myCommunityForumsAdd', views.myCommunityForumsAdd,name='myCommunityForumsAdd'), 
    path('myCommunityForumsEdit', views.myCommunityForumsEdit,name='myCommunityForumsEdit'), 
    path('myCommunityForumsDelete', views.myCommunityForumsDelete,name='myCommunityForumsDelete'),     
    path('communityForumsDetailComments', views.communityForumsDetailComments,name='communityForumsDetailComments'),         

    
    #管理员
    path('admin', views.admin,name='admin'),
    path('adminSchoolNew', views.adminSchoolNew,name='adminSchoolNew'),
    path('adminSchoolNewAdd', views.adminSchoolNewAdd,name='adminSchoolNewAdd'), 
    path('adminSchoolNewEdit', views.adminSchoolNewEdit,name='adminSchoolNewEdit'), 
    path('adminSchoolNewDelete', views.adminSchoolNewDelete,name='adminSchoolNewDelete'), 

    #用户管理
    path('adminUser', views.adminUser,name='adminUser'),
    path('adminUserAdd', views.adminUserAdd,name='adminUserAdd'), 
    path('adminUserEdit', views.adminUserEdit,name='adminUserEdit'), 
    path('adminUserDelete', views.adminUserDelete,name='adminUserDelete'),   


]
