from django.shortcuts import render, redirect
from .models import Post, Posthr, Postps
from .forms import PostForm, PosthrForm, PostpsForm
from datetime import datetime
from django.core.paginator import Paginator
from members.models import Member


# 자유게시판
def p_list(request):
    posts = Post.objects.all().order_by('-id')

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    board_page = paginator.get_page(page)

    return render(request, 'board/list.html', {
        'post_list': posts,

        'board_page': board_page
    })


def p_create(request):
    # POST방식
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.author = Member.objects.get(pk=request.session['user']['u_id'])
            obj.author_name = request.session['user']['u_name']
            obj.p_date = datetime.now()
            obj.save()
            print('OK')
            return redirect('board:p_list')
        else:
            print('ERROR')
            return redirect('board:p_list')

    # GET방식
    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'board/create.html',
                      {'post_form': post_form})


def p_detail(request, post_id):
    # 조회수를 올린다
    post = Post.objects.get(pk=post_id)
    post.p_count += 1
    post.save()
    return render(request, 'board/detail.html', {
        'post': post
    })


def p_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('board:p_list')


def p_update(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.p_date = datetime.now()
            obj.save()
            return redirect('board:p_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'board/update.html', {
        'post_form': form
    })


# 병원후기 게시판
def phr_list(request):
    posts = Posthr.objects.all().order_by('-id')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    board_page = paginator.get_page(page)

    return render(request, 'board/list2.html', {
        'post_list': posts,
        'board_page': board_page
    })


def phr_create(request):
    # POST방식
    if request.method == 'POST':
        post_form = PosthrForm(request.POST)

        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.author = Member.objects.get(pk=request.session['user']['u_id'])
            obj.author_name = request.session['user']['u_name']
            obj.phr_date = datetime.now()
            obj.save()
            print('OK')
            return redirect('board:phr_list')
        else:
            print('ERROR')
            return redirect('board:phr_list')

    # GET방식
    if request.method == 'GET':
        post_form = PosthrForm()
        return render(request, 'board/create2.html',
                      {'post_form': post_form})


def phr_detail(request, post_id):
    # 조회수를 올린다
    post = Posthr.objects.get(pk=post_id)
    post.phr_count += 1
    post.save()
    return render(request, 'board/detail2.html', {
        'post': post
    })


def phr_delete(request, post_id):
    post = Posthr.objects.get(pk=post_id)
    post.delete()
    return redirect('board:phr_list')


def phr_update(request, post_id):
    post = Posthr.objects.get(pk=post_id)

    if request.method == "POST":
        form = PosthrForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.phr_date = datetime.now()
            obj.save()
            return redirect('board:phr_list')
    else:
        form = PosthrForm(instance=post)
    return render(request, 'board/update2.html', {
        'post_form': form
    })


# 펫 분실 게시판
def pps_list(request):
    posts = Postps.objects.all().order_by('-id')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    board_page = paginator.get_page(page)
    return render(request, 'board/list3.html', {
        'post_list': posts,
        'board_page': board_page
    })


def pps_create(request):
    # POST방식
    if request.method == 'POST':
        post_form = PostpsForm(request.POST)

        if post_form.is_valid():
            obj = post_form.save(commit=False)

            obj.author = Member.objects.get(pk=request.session['user']['u_id'])
            obj.author_name = request.session['user']['u_name']
            obj.pps_date = datetime.now()
            obj.save()
            print('OK')
            return redirect('board:pps_list')
        else:
            print('ERROR')
            return redirect('board:pps_list')

    # GET방식
    if request.method == 'GET':
        post_form = PostpsForm()
        return render(request, 'board/create3.html',
                      {'post_form': post_form})


def pps_detail(request, post_id):
    # 조회수를 올린다
    post = Postps.objects.get(pk=post_id)
    post.pps_count += 1
    post.save()

    return render(request, 'board/detail3.html', {
        'post': post
    })


def pps_delete(request, post_id):
    post = Postps.objects.get(pk=post_id)
    post.delete()
    return redirect('board:pps_list')


def pps_update(request, post_id):
    post = Postps.objects.get(pk=post_id)

    if request.method == "POST":
        form = PostpsForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.pps_date = datetime.now()
            obj.save()
            return redirect('board:pps_list')
    else:
        form = PostpsForm(instance=post)

    return render(request, 'board/update3.html', {
        'post_form': form
    })

