# 여기서는 ModelForm class를 정의해요!
# ModelForm이 자동으로 Form field(HTML tag)를 생성해줘요
# Form 처리를 상당히 간단하게 처리할 수 있어요!

from django import forms
from board.models import Post, Posthr, Postps


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'author_name', 'p_title', 'p_contents', 'p_date', 'p_count']
        widgets = {
            'author': forms.HiddenInput(),
            'author_name': forms.HiddenInput(),
            'p_title': forms.TextInput(attrs={'id': 'p_title',
                                              'class': 'form-control'}),
            'p_contents': forms.TextInput(attrs={'id': 'p_contents',
                                                 'class': 'form-control'}),
            'p_date': forms.HiddenInput(),
            'p_count': forms.HiddenInput(),
        }

        labels = {
            'p_title': '글 제목',
            'p_contents': '글 내용'
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author_name'].widget.attrs['maxlength'] = 10
        self.fields['author_name'].required = False
        self.fields['p_date'].required = False
        self.fields['author'].required = False
        self.fields['p_count'].required = False


class PosthrForm(forms.ModelForm):
    class Meta:
        model = Posthr
        fields = ['author', 'author_name', 'phr_title', 'phr_contents', 'phr_date', 'phr_count']
        widgets = {
            'author': forms.HiddenInput(),
            'author_name': forms.HiddenInput(),
            'phr_title': forms.TextInput(attrs={'id': 'phr_title',
                                              'class': 'form-control'}),
            'phr_contents': forms.TextInput(attrs={'id': 'phr_contents',
                                                 'class': 'form-control'}),
            'phr_date': forms.HiddenInput(),
            'phr_count': forms.HiddenInput(),
        }

        labels = {
            'phr_title': '글 제목',
            'phr_contents': '글 내용'
        }

    def __init__(self, *args, **kwargs):
        super(PosthrForm, self).__init__(*args, **kwargs)
        self.fields['author_name'].widget.attrs['maxlength'] = 10
        self.fields['author_name'].required = False
        self.fields['phr_date'].required = False
        self.fields['author'].required = False
        self.fields['phr_count'].required = False


class PostpsForm(forms.ModelForm):
    class Meta:
        model = Postps
        fields = ['author', 'author_name', 'pps_title', 'pps_contents', 'pps_date', 'pps_count']
        widgets = {
            'author': forms.HiddenInput(),
            'author_name': forms.HiddenInput(),
            'pps_title': forms.TextInput(attrs={'id': 'pps_title',
                                              'class': 'form-control'}),
            'pps_contents': forms.TextInput(attrs={'id': 'pps_contents',
                                                 'class': 'form-control'}),
            'pps_date': forms.HiddenInput(),
            'pps_count': forms.HiddenInput(),
        }

        labels = {
            'pps_title': '글 제목',
            'pps_contents': '글 내용'
        }

    def __init__(self, *args, **kwargs):
        super(PostpsForm, self).__init__(*args, **kwargs)
        self.fields['author_name'].widget.attrs['maxlength'] = 10
        self.fields['author_name'].required = False
        self.fields['pps_date'].required = False
        self.fields['author'].required = False
        self.fields['pps_count'].required = False