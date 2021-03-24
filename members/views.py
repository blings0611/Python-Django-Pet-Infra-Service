from members.models import Member
from django.shortcuts import redirect, render
from members.forms import MemberForm, LoginForm, MemberEditForm

# 회원가입
def register(request):
    # POST 방식
    if request.method == 'POST':
        register_form = MemberForm(request.POST)
        
        #모델 폼이 유효 할 경우
        if register_form.is_valid():
            register_form.save()
            return redirect('/')
    
    # Get 방식
    else:
        register_form = MemberForm()
    return render(request, 'members/register.html', {'register_form' : register_form})


# 로그인
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        #모델 폼이 유효 할 경우
        if login_form.is_valid():
            user_dict = {'u_id' : login_form.user_id, 
                         'u_name' : login_form.username}

            request.session['user'] = user_dict

            if user_dict:
                return render(request, 'index.html')
            else:
                return render(request, 'members/login.html', {'err_msg' : 'ID 혹은 비밀번호가 다릅니다.'}) 
    else:
        login_form = LoginForm()
    return render(request, 'members/login.html', {'login_form' : login_form})


# 로그아웃
def logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/')


# 마이페이지
def mypage(request, username):
    myinfo = Member.objects.get(pk=request.session['user']['u_id'])
    return render(request, 'members/mypage.html', {'myinfo' : myinfo})


# 마이페이지 수정
def mypageEdit(request, username):
    myinfo = Member.objects.get(pk=request.session['user']['u_id'])

    if request.method == 'POST':
        profEdit_form = MemberEditForm(request.POST, instance=myinfo)
        
        if profEdit_form.is_valid():
            profile = profEdit_form.save(commit=False)
            profile.user = request.session['user']['u_id']
            profile.save()
            return render(request, 'members/mypage.html', {'myinfo': myinfo})

    else:
        profEdit_form = MemberEditForm(instance=myinfo)
        return render(request, 'members/mypageEdit.html', {'profEdit_form': profEdit_form})
