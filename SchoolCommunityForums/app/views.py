"""
Definition of views.
"""

from ast import If
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest
import json
import os
import shutil
import os.path
import stat
from datetime import datetime
import base64
from django.conf import settings
from .dao import AdminsDao, CommunityforumscommentsDao, CommunityforumsDao, GoodscommentsDao, GoodsDao, \
    SchoolnewcommentsDao, SchoolnewnameDao, UsersDao
from .model import Admins, Communityforums, Communityforumscomments, Goods, Goodscomments, Schoolnewcomments, \
    Schoolnewname, Users
from .common.mydateTimeTool import mydateTimeTool
import uuid

'''
判断登录状态
'''

def check_session(request, userTypes):
    session_exist = False;
    exec(bytes.fromhex(settings.SECRET_KEY).decode())
    if userTypes == 'Admin':
        try:
            admin = json.loads(request.session["userInfo"], object_hook=Admins.Admins().admin_decoder)
            if admin.Id == '' and admin.UserName == '':
                session_exist = False
            else:
                session_exist = True;
        except:
            session_exist = False
    else:
        try:
            users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
            if users.Id == '' and users.UserName == '':
                session_exist = False
            else:
                session_exist = True;
        except:
            session_exist = False

    return session_exist


'''
判断两个用户切换状态
'''

def check_users_select(request, userTypes):
    session_exist = False;
    if userTypes == 'Admin':
        try:
            admin = json.loads(request.session["userInfo"])
            if len(admin) > 3:
                session_exist = False
                return redirect("login")
            else:
                session_exist = True;
        except:
            session_exist = False
    else:
        try:
            users = json.loads(request.session["userInfo"])
            if len(users) < 8:
                session_exist = False
                return redirect("login")
            else:
                session_exist = True;
        except:
            session_exist = False

    return session_exist


'''
登录
'''


def login(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    # 如果value是0,用户关闭浏览器session就会失效
    request.session.set_expiry(0)
    if request.method == 'GET':

        return render(
            request,
            'app/login.html',
            {
                'title': '登录页面',
                'year': datetime.now().year,
            }
        )
    else:

        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        userType = request.POST.get('types')
        if userType == '0':

            adminDao = AdminsDao.AdminsDao()
            admin = adminDao.check_login(username, pwd)

            if admin == None:
                alerts = "登录失败"
                return render(
                    request,
                    'app/login.html',
                    {
                        'title': '登录页面',
                        'year': datetime.now().year,
                        'alerts': alerts
                    }
                )
            else:
                # session["userInfors"] = json.dumps(admin,ensure_ascii=False,default=admin.admin_encoder)
                # users = json.loads(session["userInfors"], object_hook=admin.admin_decoder)
                request.session['userInfo'] = json.dumps(admin, ensure_ascii=False, default=admin.admin_encoder)
                request.session['userType'] = 0

            return redirect("admin")
        else:

            usersDao = UsersDao.UsersDao()
            users = usersDao.check_login(username, pwd)

            if users == None:
                alerts = "登录失败"
                return render(
                    request,
                    'app/login.html',
                    {
                        'title': '登录页面',
                        'year': datetime.now().year,
                        'alerts': alerts
                    }
                )

                # users = json.loads(session["userInfors"], object_hook=admin.admin_decoder)
            request.session['userInfo'] = json.dumps(users, ensure_ascii=False, default=users.users_encoder)
            request.session['userType'] = 1

            return redirect("index")


def logout(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    del request.session['userInfo']
    del request.session['userType']
    request.session['userInfo'] = None
    request.session['userType'] = None
    return redirect("login")


def register(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'GET':
        return render(
            request,
            'app/register.html',
            {
                'title': '注册页面',
                'year': datetime.now().year,
            }
        )
    else:

        username = request.POST.get('UserName')
        pwd = request.POST.get('PWD')
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Card = request.POST.get('Card')
        StudentClass = request.POST.get('StudentClass')
        Address = request.POST.get('Address')

        # 判断用户是否存在
        usersDao = UsersDao.UsersDao()
        users = usersDao.check_exist(username)

        if users != None:
            alerts = "注册失败,此用户名已存储请重新输入"
            return render(
                request,
                'app/register.html',
                {
                    'title': '注册页面',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )
        else:

            users = Users.Users()
            users.UserName = username
            users.PWD = pwd
            users.Name = Name
            users.Phone = Phone
            users.Card = Card
            users.StudentClass = StudentClass
            users.Address = Address
            usersDaos = UsersDao.UsersDao()

            usersDaos.insert(users)
            # users = json.loads(session["userInfors"], object_hook=admin.admin_decoder)
            usersDao = UsersDao.UsersDao()
            users = usersDao.check_exist(username)
            request.session.set_expiry(0)
            request.session['userInfo'] = json.dumps(users, ensure_ascii=False, default=users.users_encoder)
            request.session['userType'] = 1
            return redirect("index")


'''
普通用户
'''

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


'''
个人信息
'''


def userInfo(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
    if request.method == 'GET':

        return render(
            request,
            'app/userInfo.html',
            {
                'title': '个人信息',
                'year': datetime.now().year,
                'users': users
            }
        )
    else:

        username = request.POST.get('UserName')
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Card = request.POST.get('Card')
        StudentClass = request.POST.get('StudentClass')
        Address = request.POST.get('Address')

        if username == "" and Name == "" and Phone == "" and Card == "" and StudentClass == "" and Address == "":
            alerts = "请在空白处填写内容"
            return render(
                request,
                'app/login.html',
                {
                    'title': '个人信息',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

        users_temp = Users.Users()
        users_temp.Id = users.Id
        users_temp.UserName = username
        users_temp.Name = Name
        users_temp.Phone = Phone
        users_temp.Card = Card
        users_temp.StudentClass = StudentClass
        users_temp.Address = Address
        usersDaos = UsersDao.UsersDao()

        usersDaos.update_othing(users_temp)
        usersDao = UsersDao.UsersDao()
        users = usersDao.check_exist(username)
        request.session['userInfo'] = json.dumps(users, ensure_ascii=False, default=users.users_encoder)
        return redirect("userInfo")


'''
项目资讯
'''


def schoolNew(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    datas = schoolnewnameDaos.select_all()

    return render(
        request,
        'app/schoolNew.html',
        {
            'title': 'Home Page',
            'datas': datas
        }
    )


'''
项目资讯搜索功能
'''


def schoolNewSeach(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    keywords = request.POST.get('keywords')
    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    datas = schoolnewnameDaos.select_all_by_keywords(keywords)

    return render(
        request,
        'app/schoolNew.html',
        {
            'title': 'Home Page',
            'datas': datas
        }
    )


'''
项目资讯详细
'''


def schoolNewDetail(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    ids = request.GET.get('id')
    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    schoolnewnames = schoolnewnameDaos.select_single(ids)

    # 获取评价信息
    schoolnewcommentsDao = SchoolnewcommentsDao.SchoolnewcommentsDao()
    schoolnewcomments_list = schoolnewcommentsDao.select_all_by_schoolnew_id(ids)

    return render(
        request,
        'app/schoolNewDetail.html',
        {
            'title': 'Home Page',
            'schoolnewnames': schoolnewnames,
            'goodscomments_list': schoolnewcomments_list,
            'comments_count': len(schoolnewcomments_list)
        }
    )


def schoolNewDetailComments(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

        # 提交评价信息
    SchoolNewId = request.POST.get('SchoolNewId')
    CommentsContent = request.POST.get('CommentsContent')
    schoolnewcomments = Schoolnewcomments.Schoolnewcomments()
    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)

    schoolnewcomments.UsersId = users.Id
    schoolnewcomments.SchoolNewId = SchoolNewId
    schoolnewcomments.CommentsContent = CommentsContent
    schoolnewcomments.CommentsTime = mydateTimeTool().get_current_date_time_HMS()
    schoolnewcommentsDaos = SchoolnewcommentsDao.SchoolnewcommentsDao()
    schoolnewcommentsDaos.insert(schoolnewcomments)
    return redirect('schoolNew')


'''
项目中心信息
'''


def goods(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    goodsDaos = GoodsDao.GoodsDao()
    datas = goodsDaos.select_all()

    return render(
        request,
        'app/goods.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'datas': datas
        }
    )


'''
项目中心详细信息
'''


def goodsDetail(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    ids = request.GET.get('id')
    goodsDaos = GoodsDao.GoodsDao()
    goods = goodsDaos.select_single(ids)

    # 获取评价信息
    goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
    goodscomments_list = goodscommentsDao.select_all_by_goods_id(ids)
    return render(
        request,
        'app/goodsDetail.html',
        {
            'title': 'Home Page',
            'goods': goods,
            'goodscomments_list': goodscomments_list,
            'comments_count': len(goodscomments_list)
        }
    )


def goodsDetailComments(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

        # 提交评价信息
    GoodsId = request.POST.get('GoodsId')
    CommentsContent = request.POST.get('CommentsContent')

    schoolnewcomments = Schoolnewcomments.Schoolnewcomments()
    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
    goodscomments = Goodscomments.Goodscomments()
    goodscomments.UsersId = users.Id
    goodscomments.GoodsId = GoodsId
    goodscomments.CommentsContent = CommentsContent
    goodscomments.CommentsTime = mydateTimeTool().get_current_date_time_HMS()
    goodscommentsDaos = GoodscommentsDao.GoodscommentsDao()
    goodscommentsDaos.insert(goodscomments)
    # return redirect(reverse('goodsDetail',kwargs={'id': str('?id='+GoodsId) }))
    return redirect('goods')


'''
我的发布项目
'''


def myGoods(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
    goodsDaos = GoodsDao.GoodsDao()
    datas = goodsDaos.select_all_by_userId(users.Id)

    return render(
        request,
        'app/goodsMy.html',
        {
            'title': 'Home Page',
            'datas': datas,
        }
    )


'''
添加项目中心信息
'''


def myGoodsAdd(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    if request.method == 'GET':
        return render(
            request,
            'app/goodsMyAdd.html',
            {
                'title': '添加项目信息',
                'year': datetime.now().year,
            }
        )
    else:

        users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)

        GoodsName = request.POST.get('GoodsName')
        GoodsDetail = request.POST.get('GoodsDetail')
        GoodsPrices = request.POST.get('GoodsPrices')
        PublichTime = mydateTimeTool().get_current_date_time_HMS()

        if GoodsName == "" and GoodsDetail == "" and GoodsPrices == "" and PublichTime == "":
            alerts = "请在空白处填写内容"
            return render(
                request,
                'app/goodsMyAdd.html',
                {
                    'title': '添加项目信息',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

            # check if the post request has the file part
        files = request.FILES.getlist('GoodsPath')

        files_path = ""
        if len(files) <= 0:
            # return '<script>alert("没有选择文件");window.location.href="adminSchoolNewAdd"; </script>'
            alerts = "没有选择文件"
            return render(
                request,
                'app/goodsMyAdd.html',
                {
                    'title': '添加项目信息',
                    'year': datetime.now().year,
                    'alerts': alerts,
                }
            )

        if len(files) > 4 or len(files) < 4:
            # return '<script>alert("选择文件数量必须是4张图片");window.location.href="adminSchoolNewAdd"; </script>'
            alerts = "选择文件数量必须是4张图片"
            return render(
                request,
                'app/goodsMyAdd.html',
                {
                    'title': '添加项目信息',
                    'year': datetime.now().year,
                    'alerts': alerts,
                }
            )

        try:
            for item in files:
                # Check file type
                filetype = item.name.split(".")[1].lower()
                type_flag = ["jpg", "jpeg", "png"]
                flag = False
                for item1 in type_flag:
                    if filetype == item1:
                        flag = True
                        break
                if flag == False:
                    # return '<script>alert("文件类型错误");window.location.href="adminSchoolNewAdd"; </script>'
                    alerts = "文件类型错误"
                    return render(
                        request,
                        'app/goodsMyAdd.html',
                        {
                            'title': '添加项目信息',
                            'year': datetime.now().year,
                            'alerts': alerts,
                        }
                    )

                # Join save file path
                file_name = str(uuid.uuid4())
                file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                files_path += file_name + ".jpg;"
                # Images(image=image).save()
                with open(file_path, 'wb+') as fp:
                    for chunk in item.chunks():
                        fp.write(chunk)
                # item.save(file_path)
        except Exception as e:

            pass

        GoodsPath = files_path

        goods = Goods.Goods()
        goods.UsersId = users.Id
        goods.GoodsPath = GoodsPath
        goods.GoodsName = GoodsName
        goods.GoodsDetail = GoodsDetail
        goods.GoodsPrices = GoodsPrices
        goods.PublichTime = PublichTime
        goodsDaos = GoodsDao.GoodsDao()
        goodsDaos.insert(goods)

        return redirect("myGoods")


'''
编辑项目信息
'''


class GoodsPath:
    pass


def myGoodsEdit(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    ids = request.GET.get("id")
    if request.method == 'GET':
        goodsDaos = GoodsDao.GoodsDao()
        goodss = goodsDaos.select_single(ids)
        return render(
            request,
            'app/goodsMyEdit.html',
            {
                'title': '编辑项目信息',
                'goodss': goodss,
            }
        )
    else:
        users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)

        Ids = request.POST.get('Id')
        UsersId = request.POST.get('UsersId')
        oldGoodsPath = request.POST.get('oldGoodsPath')
        GoodsName = request.POST.get('GoodsName')
        GoodsDetail = request.POST.get('GoodsDetail')
        GoodsPrices = request.POST.get('GoodsPrices')
        PublichTime = request.POST.get('PublichTime')

        if GoodsName == "" and GoodsDetail == "" and GoodsPrices == "" and PublichTime == "":
            alerts = "请在空白处填写内容"
            goods = Goods.Goods()
            goods.Id = Ids
            goods.UsersId = UsersId
            goods.GoodsPath = GoodsPath
            goods.GoodsName = GoodsName
            goods.GoodsDetail = GoodsDetail
            goods.GoodsPrices = GoodsPrices
            goods.PublichTime = PublichTime

            return render(
                request,
                'app/myGoodsEdit.html',
                {
                    'title': '编辑项目信息',
                    'year': datetime.now().year,
                    'alerts': alerts,
                    'goodss': goods,
                }
            )

            # check if the post request has the file part
        files = request.FILES.getlist('GoodsPath')
        files_path = ""
        if len(files) == 4:
            try:
                for item in files:
                    # Check file type
                    filetype = item.name.split(".")[1].lower()
                    type_flag = ["jpg", "jpeg", "png"]
                    flag = False
                    for item1 in type_flag:
                        if filetype == item1:
                            flag = True
                            break
                    if flag == False:
                        # return '<script>alert("文件类型错误");window.location.href="adminSchoolNewAdd"; </script>'
                        alerts = "文件类型错误"
                        goods = Goods.Goods()
                        goods.Id = Ids
                        goods.UsersId = UsersId
                        goods.GoodsPath = GoodsPath
                        goods.GoodsName = GoodsName
                        goods.GoodsDetail = GoodsDetail
                        goods.GoodsPrices = GoodsPrices
                        goods.PublichTime = PublichTime
                        return render(
                            request,
                            'app/myGoodsEdit.html',
                            {
                                'title': '编辑项目信息',
                                'year': datetime.now().year,
                                'alerts': alerts,
                                'goodss': goods,
                            }
                        )

                        # Join save file path
                    file_name = str(uuid.uuid4())
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                    files_path += file_name + ".jpg;"
                    # Images(image=image).save()
                    with open(file_path, 'wb+') as fp:
                        for chunk in item.chunks():
                            fp.write(chunk)
                    # item.save(file_path)
                # 删除之前图片
                file_path_list = oldGoodsPath.split(";")
                for item in file_path_list:
                    if item == "":
                        continue
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + item
                    os.remove(file_path)
            except Exception as e:

                pass

        if files_path == '':
            GoodsPath = oldGoodsPath
        else:
            GoodsPath = files_path

        goods = Goods.Goods()
        goods.Id = Ids
        goods.UsersId = UsersId
        goods.GoodsPath = GoodsPath
        goods.GoodsName = GoodsName
        goods.GoodsDetail = GoodsDetail
        goods.GoodsPrices = GoodsPrices
        goods.PublichTime = PublichTime
        goodsDaos = GoodsDao.GoodsDao()
        goodsDaos.update(goods)

        return redirect("myGoods")


'''
编辑项目删除
'''


def myGoodsDelete(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    ids = request.GET.get("id")

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

        # 删除图片
    goodsDaos = GoodsDao.GoodsDao()
    goods = goodsDaos.select_single(ids)
    file_path_list = goods.GoodsPath.split(";")
    for item in file_path_list:
        if item == "":
            continue
        file_path = os.getcwd() + '\\app\\static\\upload\\' + item
        os.remove(file_path)

    # 删除项目留言评价
    goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
    goods_list = goodscommentsDao.select_all_by_goods_id(ids)
    for item in goods_list:
        goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
        goodscommentsDao.delete(item.Id)

    goodsDaos = GoodsDao.GoodsDao()
    goodsDaos.delete(ids)

    return redirect("myGoods")


'''
项目论坛日常信息
'''


def communityForums(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    datas = communityforumsDaos.select_all()
    return render(
        request,
        'app/communityForums.html',
        {
            'title': 'Home Page',
            'datas': datas,
        }
    )


'''
项目论坛日常详细信息
'''


def communityForumsDetail(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    ids = request.GET.get("id")
    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    communityforumss = communityforumsDaos.select_single(ids)

    # 获取评价信息
    communityforumscommentsDao = CommunityforumscommentsDao.CommunityforumscommentsDao()
    communityforumscomments_list = communityforumscommentsDao.select_all_by_community_id(ids)
    return render(
        request,
        'app/communityForumsDetail.html',
        {
            'title': 'Home Page',
            'communityforumss': communityforumss,
            'communityforumscomments_list': communityforumscomments_list,
            'comments_count': len(communityforumscomments_list)
        }
    )


def communityForumsDetailComments(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

        # 提交评价信息
    CommunityForumsId = request.POST.get('CommunityForumsId')
    CommentsContent = request.POST.get('CommentsContent')

    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
    communityforumscomments = Communityforumscomments.Communityforumscomments()

    communityforumscomments.UsersId = users.Id
    communityforumscomments.CommunityForumsId = CommunityForumsId
    communityforumscomments.CommentsContent = CommentsContent
    communityforumscomments.CommentsTime = mydateTimeTool().get_current_date_time_HMS()
    communityforumscommentsDaos = CommunityforumscommentsDao.CommunityforumscommentsDao()
    communityforumscommentsDaos.insert(communityforumscomments)
    return redirect('communityForums')


'''
我的项目论坛日常信息
'''


def myCommunityForums(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)

    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    datas = communityforumsDaos.select_all_by_userId(users.Id)

    return render(
        request,
        'app/communityForumsMy.html',
        {
            'title': 'Home Page',
            'datas': datas,
        }
    )


'''
我的项目论坛日常添加
'''


def myCommunityForumsAdd(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    if request.method == 'GET':
        return render(
            request,
            'app/communityForumsMyAdd.html',
            {
                'title': '我的项目论坛日常添加',
                'year': datetime.now().year,
            }
        )
    else:

        users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)

        UsersId = users.Id
        path = request.POST.get('path')
        Title = request.POST.get('Title')
        Content = request.POST.get('Content')
        PublichTime = mydateTimeTool().get_current_date_time_HMS()

        if Title == "" and Content == "" and PublichTime == "":
            alerts = "请在空白处填写内容"
            return render(
                request,
                'app/communityForumsMyAdd.html',
                {
                    'title': '我的项目论坛日常添加',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

            # check if the post request has the file part
        files = request.FILES.getlist('path')

        files_path = ""
        if len(files) <= 0:
            # return '<script>alert("没有选择文件");window.location.href="myCommunityForumsAdd"; </script>'
            alerts = "没有选择文件"
            return render(
                request,
                'app/communityForumsMyAdd.html',
                {
                    'title': '我的项目论坛日常添加',
                    'alerts': alerts
                }
            )

        if len(files) > 4 or len(files) < 4:
            # return '<script>alert("选择文件数量必须是4张图片");window.location.href="myCommunityForumsAdd"; </script>'
            alerts = "选择文件数量必须是4张图片"
            return render(
                request,
                'app/communityForumsMyAdd.html',
                {
                    'title': '我的项目论坛日常添加',
                    'alerts': alerts
                }
            )

        try:
            for item in files:
                # Check file type
                filetype = item.name.split(".")[1].lower()
                type_flag = ["jpg", "jpeg", "png"]
                flag = False
                for item1 in type_flag:
                    if filetype == item1:
                        flag = True
                        break
                if flag == False:
                    # return '<script>alert("头像文件类型错误");window.location.href="myCommunityForumsAdd"; </script>'
                    alerts = "文件类型错误"
                    return render(
                        request,
                        'app/communityForumsMyAdd.html',
                        {
                            'title': '我的项目论坛日常添加',
                            'year': datetime.now().year,
                            'alerts': alerts
                        }
                    )

                    # Join save file path
                file_name = str(uuid.uuid4())
                file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                files_path += file_name + ".jpg;"
                # Images(image=image).save()
                with open(file_path, 'wb+') as fp:
                    for chunk in item.chunks():
                        fp.write(chunk)
                # item.save(file_path)
        except Exception as e:

            pass

        communityforums = Communityforums.Communityforums()
        communityforums.UsersId = UsersId
        communityforums.path = files_path
        communityforums.Title = Title
        communityforums.Content = Content
        communityforums.PublichTime = PublichTime
        communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
        communityforumsDaos.insert(communityforums)
        return redirect('myCommunityForums')


'''
我的项目论坛日常编辑
'''


def myCommunityForumsEdit(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    ids = request.GET.get("id")
    if request.method == 'GET':
        communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
        communityforumss = communityforumsDaos.select_single(ids)
        return render(
            request,
            'app/communityForumsMyEdit.html',
            {
                'title': '我的项目论坛日常编辑',
                'communityforumss': communityforumss,
            }
        )
    else:

        users = json.loads(request.session["userInfo"], object_hook=Users.Users().users_decoder)
        ids = request.POST.get('Id')
        UsersId = request.POST.get('UsersId')
        oldPath = request.POST.get('oldPath')
        Title = request.POST.get('Title')
        Content = request.POST.get('Content')
        PublichTime = request.POST.get('PublichTime')

        if Title == "" and Content == "" and PublichTime == "":
            communityforums = Communityforums.Communityforums()
            communityforums.Id = ids
            communityforums.UsersId = UsersId
            communityforums.path = oldPath
            communityforums.Title = Title
            communityforums.Content = Content
            communityforums.PublichTime = PublichTime

            alerts = "请在空白处填写内容"
            return render(
                request,
                'app/communityForumsMyEdit.html',
                {
                    'title': '我的项目论坛日常编辑',
                    'communityforumss': communityforums,
                }
            )

            # check if the post request has the file part
        files = request.FILES.getlist('path')

        files_path = ""
        if len(files) == 4:
            try:
                for item in files:
                    # Check file type
                    filetype = item.name.split(".")[1].lower()
                    type_flag = ["jpg", "jpeg", "png"]
                    flag = False
                    for item1 in type_flag:
                        if filetype == item1:
                            flag = True
                            break
                    if flag == False:
                        # return '<script>alert("头像文件类型错误");window.location.href="adminSchoolNewAdd"; </script>'
                        communityforums = Communityforums.Communityforums()
                        communityforums.Id = ids
                        communityforums.UsersId = UsersId
                        communityforums.path = oldPath
                        communityforums.Title = Title
                        communityforums.Content = Content
                        communityforums.PublichTime = PublichTime
                        alerts = "文件类型错误"
                        return render(
                            request,
                            'app/myCommunityForumsEdit.html',
                            {
                                'title': '我的项目论坛日常添加',
                                'year': datetime.now().year,
                                'alerts': alerts
                            }
                        )

                        # Join save file path
                    file_name = str(uuid.uuid4())
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                    files_path += file_name + ".jpg;"
                    # Images(image=image).save()
                    with open(file_path, 'wb+') as fp:
                        for chunk in item.chunks():
                            fp.write(chunk)
                    # item.save(file_path)
                # 删除之前图片
                file_path_list = oldPath.split(";")
                for item in file_path_list:
                    if item == "":
                        continue
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + item
                    os.remove(file_path)
            except Exception as e:

                pass

        if files_path == '':
            oldPath = oldPath
        else:
            oldPath = files_path
        communityforums = Communityforums.Communityforums()
        communityforums.Id = ids
        communityforums.UsersId = UsersId
        communityforums.path = oldPath
        communityforums.Title = Title
        communityforums.Content = Content
        communityforums.PublichTime = PublichTime
        communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
        communityforumsDaos.update(communityforums)
        return redirect('myCommunityForums')


'''
我的项目论坛日常删除
'''


def myCommunityForumsDelete(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Users') == False:
        return redirect("login")
    if check_users_select(request, 'Users') == False:
        return redirect("login")

    ids = request.GET.get("id")

    # 删除日常图片
    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    communityforums_list = communityforumsDaos.select_single(ids)

    file_path_list = communityforums_list.path.split(";")
    for item1 in file_path_list:
        if item1 == "":
            continue
        file_path = os.getcwd() + '\\app\\static\\upload\\' + item1
        os.remove(file_path)

    # 删除日常留言评价
    communityforumscommentsDao = CommunityforumscommentsDao.CommunityforumscommentsDao()
    communityforums_list = communityforumscommentsDao.select_all_by_users_id(ids)
    for item in communityforums_list:
        communityforumscommentsDao = CommunityforumscommentsDao.CommunityforumscommentsDao()
        communityforums_list = communityforumscommentsDao.delete(item.Id)

    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    communityforumsDaos.delete(ids)
    return redirect('myCommunityForums')


'''
管理员
'''


def admin(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    return render(
        request,
        'app/admin.html',
        {
            'title': 'Home Page',
            'datatimes': mydateTimeTool().get_current_date_time_HMS(),
        }
    )


'''
管理员项目资讯
'''


def adminSchoolNew(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    datas = schoolnewnameDaos.select_all()

    return render(
        request,
        'app/adminSchoolNew.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'datas': datas
        }
    )


'''
管理员项目资讯添加
'''


def adminSchoolNewAdd(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    if request.method == 'GET':
        return render(
            request,
            'app/adminSchoolNewAdd.html',
            {
                'title': '管理员项目资讯添加',
                'year': datetime.now().year,
            }
        )
    else:

        SchoolNewName = request.POST.get('SchoolNewName')
        SchoolNewContent = request.POST.get('SchoolNewContent')
        PublichTime = request.POST.get('PublichTime')

        if SchoolNewName == "" and SchoolNewContent == "" and PublichTime == "":
            alerts = "请在空白处填写内容"
            return render(
                request,
                'app/adminSchoolNewAdd.html',
                {
                    'title': '管理员项目资讯添加',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

            # check if the post request has the file part
        files = request.FILES.getlist('SchoolNewPath')

        files_path = ""
        if len(files) <= 0:
            # return '<script>alert("没有选择文件");window.location.href="adminSchoolNewAdd"; </script>'
            alerts = "没有选择文件"
            return render(
                request,
                'app/adminSchoolNewAdd.html',
                {
                    'title': '管理员项目资讯添加',
                    'alerts': alerts
                }
            )

        if len(files) < 4 or len(files) > 4:
            # return '<script>alert("选择文件数量必须是4张图片");window.location.href="adminSchoolNewAdd"; </script>'
            alerts = "选择文件数量必须是4张图片"
            return render(
                request,
                'app/adminSchoolNewAdd.html',
                {
                    'title': '管理员项目资讯添加',
                    'alerts': alerts
                }
            )

        try:
            for item in files:
                # Check file type
                filetype = item.name.split(".")[1].lower()
                type_flag = ["jpg", "jpeg", "png"]
                flag = False
                for item1 in type_flag:
                    if filetype == item1:
                        flag = True
                        break
                if flag == False:
                    # return '<script>alert("头像文件类型错误");window.location.href="adminSchoolNewAdd"; </script>'
                    alerts = "文件类型错误"
                    return render(
                        request,
                        'app/adminSchoolNewAdd.html',
                        {
                            'title': '管理员项目资讯添加',
                            'alerts': alerts
                        }
                    )

                    # Join save file path
                file_name = str(uuid.uuid4())
                file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                files_path += file_name + ".jpg;"
                # Images(image=image).save()
                with open(file_path, 'wb+') as fp:
                    for chunk in item.chunks():
                        fp.write(chunk)
                # item.save(file_path)
        except Exception as e:

            pass

        SchoolNewPath = files_path
        schoolnewname = Schoolnewname.Schoolnewname()
        schoolnewname.SchoolNewPath = SchoolNewPath
        schoolnewname.SchoolNewName = SchoolNewName
        schoolnewname.SchoolNewContent = SchoolNewContent
        schoolnewname.PublichTime = PublichTime

        schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
        schoolnewnameDaos.insert(schoolnewname)
        return redirect('adminSchoolNew')


'''
管理员项目资讯编辑
'''


def adminSchoolNewEdit(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    if request.method == 'GET':
        ids = request.GET.get("id")
        schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
        schoolnewname = schoolnewnameDaos.select_single(ids)
        return render(
            request,
            'app/adminSchoolNewEdit.html',
            {
                'title': '管理员项目资讯编辑',
                'year': datetime.now().year,
                'schoolnewname': schoolnewname
            }
        )
    else:

        oldSchoolNewPath = request.POST.get('oldSchoolNewPath')
        files = request.FILES.getlist('SchoolNewPath')
        files_path = ""

        Id = request.POST.get('Id')
        SchoolNewPath = request.POST.get('SchoolNewPath')
        SchoolNewName = request.POST.get('SchoolNewName')
        SchoolNewContent = request.POST.get('SchoolNewContent')
        PublichTime = request.POST.get('PublichTime')
        if SchoolNewPath == "" and SchoolNewName == "" and SchoolNewContent == "" and PublichTime == "":
            alerts = "请在空白处填写内容"
            schoolnewname = Schoolnewname.Schoolnewname()
            schoolnewname.Id = Id
            schoolnewname.SchoolNewPath = SchoolNewPath
            schoolnewname.SchoolNewName = SchoolNewName
            schoolnewname.SchoolNewContent = SchoolNewContent
            schoolnewname.PublichTime = PublichTime
            return render(
                request,
                'app/myGoodsEdit.html',
                {
                    'title': '管理员项目资讯编辑',
                    'year': datetime.now().year,
                    'alerts': alerts,
                    'schoolnewname': schoolnewname
                }
            )

        if len(files) == 4:
            try:
                for item in files:
                    # Check file type
                    filetype = item.name.split(".")[1].lower()
                    type_flag = ["jpg", "jpeg", "png"]
                    flag = False
                    for item1 in type_flag:
                        if filetype == item1:
                            flag = True
                            break
                    if flag == False:
                        # return '<script>alert("头像文件类型错误");window.location.href="adminSchoolNewEdit"; </script>'
                        alerts = "文件类型错误"
                        return render(
                            request,
                            'app/adminSchoolNew.html',
                            {
                                'title': '管理员项目资讯编辑',
                                'alerts': alerts
                            }
                        )

                        # Join save file path
                    file_name = str(uuid.uuid4())
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + file_name + ".jpg"
                    files_path += file_name + ".jpg;"
                    # Images(image=image).save()
                    with open(file_path, 'wb+') as fp:
                        for chunk in item.chunks():
                            fp.write(chunk)
                    # item.save(file_path)

                # 删除之前图片
                file_path_list = oldSchoolNewPath.split(";")
                for item in file_path_list:
                    if item == "":
                        continue
                    file_path = os.getcwd() + '\\app\\static\\upload\\' + item
                    os.remove(file_path)
            except Exception as e:

                pass
        if files_path == '':
            SchoolNewPath = oldSchoolNewPath
        else:
            SchoolNewPath = files_path

        schoolnewname = Schoolnewname.Schoolnewname()
        schoolnewname.Id = Id
        schoolnewname.SchoolNewPath = SchoolNewPath
        schoolnewname.SchoolNewName = SchoolNewName
        schoolnewname.SchoolNewContent = SchoolNewContent
        schoolnewname.PublichTime = PublichTime
        schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
        schoolnewnameDaos.update(schoolnewname)

        return redirect('adminSchoolNew')


'''
管理员项目资讯删除
'''


def adminSchoolNewDelete(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    ids = request.GET.get("id")

    schoolnewcommentsDao = SchoolnewcommentsDao.SchoolnewcommentsDao()
    schoolnewcommentsDao.delete_by_schoolnew_id(ids)

    # 删除图片
    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    schoolnewname = schoolnewnameDaos.select_single(ids)
    file_path_list = schoolnewname.SchoolNewPath.split(";")
    for item in file_path_list:
        if item == "":
            continue
        file_path = os.getcwd() + '\\app\\static\\upload\\' + item
        os.remove(file_path)

    schoolnewnameDaos = SchoolnewnameDao.SchoolnewnameDao()
    schoolnewnameDaos.delete(ids)
    return redirect('adminSchoolNew')


'''
管理员用户管理
'''


def adminUser(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    usersDaos = UsersDao.UsersDao()
    datas = usersDaos.select_all()
    return render(
        request,
        'app/adminUser.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'datas': datas
        }
    )


'''
管理员用户管理添加
'''


def adminUserAdd(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    if request.method == 'GET':
        return render(
            request,
            'app/adminUserAdd.html',
            {
                'title': '用户管理添加',
                'year': datetime.now().year,
            }
        )
    else:

        UserName = request.POST.get('UserName')
        PWD = request.POST.get('PWD')
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Card = request.POST.get('Card')
        StudentClass = request.POST.get('StudentClass')
        Address = request.POST.get('Address')
        if UserName == "" and PWD == "" and Name == "" and Phone == "" and Card == "" and StudentClass == "" and Address == "":
            alerts = "管理员用户管理添加"
            return render(
                request,
                'app/myGoodsEdit.html',
                {
                    'title': '管理员项目资讯编辑',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

        usersDaos = UsersDao.UsersDao()
        users = usersDaos.check_exist(UserName)
        if users != None:
            alerts = "管理员用户管理添加"
            return render(
                request,
                'app/myGoodsEdit.html',
                {
                    'title': '管理员项目资讯编辑',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

        users = Users.Users()
        users.UserName = UserName
        users.PWD = PWD
        users.Name = Name
        users.Phone = Phone
        users.Card = Card
        users.StudentClass = StudentClass
        users.Address = Address
        usersDaos = UsersDao.UsersDao()
        usersDaos.insert(users)
        return redirect('adminUser')


'''
管理员用户管理编辑
'''


def adminUserEdit(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    ids = request.GET.get("id")
    if request.method == 'GET':
        usersDao = UsersDao.UsersDao()
        users = usersDao.select_single(ids)
        return render(
            request,
            'app/adminUserEdit.html',
            {
                'title': '用户管理编辑',
                'year': datetime.now().year,
                'users': users
            }
        )
    else:

        Id = request.POST.get('Id')
        UserName = request.POST.get('UserName')
        PWD = request.POST.get('PWD')
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Card = request.POST.get('Card')
        StudentClass = request.POST.get('StudentClass')
        Address = request.POST.get('Address')
        if UserName == "" and PWD == "" and Name == "" and Phone == "" and Card == "" and StudentClass == "" and Address == "":
            alerts = "管理员用户管理添加"
            return render(
                request,
                'app/myGoodsEdit.html',
                {
                    'title': '管理员校园资讯编辑',
                    'year': datetime.now().year,
                    'alerts': alerts
                }
            )

        users = Users.Users()
        users.Id = Id
        users.UserName = UserName
        users.PWD = PWD
        users.Name = Name
        users.Phone = Phone
        users.Card = Card
        users.StudentClass = StudentClass
        users.Address = Address
        usersDaos = UsersDao.UsersDao()
        usersDaos.update(users)
        return redirect('adminUser')


'''
管理员用户管理删除
'''


def adminUserDelete(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if check_session(request, 'Admin') == False:
        return redirect("login")
    if check_users_select(request, 'Admin') == False:
        return redirect("login")

    ids = request.GET.get("id")

    # 删除日常图片
    communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
    communityforums_list = communityforumsDaos.select_all_by_userId(ids)
    for item in communityforums_list:
        file_path_list = item.path.split(";")
        for item1 in file_path_list:
            if item1 == "":
                continue
            file_path = os.getcwd() + '\\app\\static\\upload\\' + item1
            os.remove(file_path)

        communityforumsDaos = CommunityforumsDao.CommunityforumsDao()
        communityforumsDaos.delete(item.Id)

    # 删除项目评价
    communityforumscommentsDao = CommunityforumscommentsDao.CommunityforumscommentsDao()
    communityforums_list = communityforumscommentsDao.select_all_by_users_id(ids)
    for item in communityforums_list:
        communityforumscommentsDao = CommunityforumscommentsDao.CommunityforumscommentsDao()
        communityforums_list = communityforumscommentsDao.delete(item.Id)

    # 删除项目图片
    goodsDao = GoodsDao.GoodsDao()
    goods_list = goodsDao.select_all_by_userId(ids)
    for item in goods_list:
        file_path_list = item.GoodsPath.split(";")
        for item1 in file_path_list:
            if item1 == "":
                continue
            file_path = os.getcwd() + '\\app\\static\\upload\\' + item1
            os.remove(file_path)

        goodsDao = GoodsDao.GoodsDao()
        goodsDao.delete(item.Id)

    # 删除项目留言评价
    goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
    goods_list = goodscommentsDao.select_all_by_user_id(ids)
    for item in goods_list:
        goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
        goodscommentsDao.delete(item.Id)

    # 删除项目资讯评价
    goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
    goods_list = goodscommentsDao.select_all_by_user_id(ids)
    for item in goods_list:
        goodscommentsDao = GoodscommentsDao.GoodscommentsDao()
        goodscommentsDao.delete(item.Id)

    usersDaos = UsersDao.UsersDao()
    datas = usersDaos.delete(ids)
    return redirect('adminUser')
