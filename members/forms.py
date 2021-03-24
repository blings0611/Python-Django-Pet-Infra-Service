from django import forms
from members.models import Member
# from django.contrib.auth.hashers import check_password


class MemberForm(forms.ModelForm):
    verify_password = forms.CharField(label = '비밀번호 확인', widget = forms.PasswordInput)
    class Meta:
        model = Member
        fields = ['username', 'email', 'password', 'verify_password', 'nickname', 'prof_pic', 'species', 'local']
        widgets = {
            'password' : forms.PasswordInput(),
        }
    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('verify_password')
        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디",
    error_messages={
        'required':"아이디를 입력하세요"
    })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
    error_messages={
        'required':"비밀번호를 입력하세요"
    } )

    #유효성 검사하는 clean 메소드를 오버라이드
    def clean(self):
        clean_data = super().clean() #역추적해보면 원래 cleaned_data를 리턴하고있다.
        # 비어있지않은 데이터라면
        username = clean_data.get('username') # 필드에 입력한 값을 변수로 받음
        password = clean_data.get('password')

        # 회원 일치 조회
        if password and username :
            try:
                user = Member.objects.get(username = username)
            except Member.DoesNotExist:
                self.add_error("username", "아이디가 존재하지 않습니다.")
                return

            if password != user.password:
                self.add_error("password", "비밀번호가 일치하지 않습니다.")
            else:
                self.user_id = user.id
                self.username = user.username
    

class MemberEditForm(MemberForm):
    class Meta:
        model = Member
        fields = ['nickname', 'species', 'local', 'password']


