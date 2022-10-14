from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.views import generic

from .forms import NewPostForm
from .models import Post
from django.shortcuts import get_object_or_404


class PostListView(generic.ListView):
    model = Post
    template_name = 'po.html'
    context_object_name = 'p1'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_created')


# def post_list_view(request):
#     p1 = Post.objects.filter(status='pub').order_by('-datetime_add')
#
#     return render(request, 'po.html', {'p1': p1})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'po'


# def post_detail_view(request, pk):
#
#     po = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'po': po})


class PostCreateFormView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


# def post_create(request, ):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('p_list')
#
#     else:  # get request
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form': form}, )


# if request.method == 'POST':
#     post_title = request.POST.get('title')
#     post_text = request.POST.get('text')
#     user = User.objects.all()[0]  # چون کاربری بجز یکی نداریم اولین سطر دیتا بیس را بجاش میذاریم
#
#     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
#
# print(request.POST.get('title')),
# print(request.POST.get('text')),
#
# return render(request, 'blog/post_create.html', )

# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('p_list')
#     return render(request, 'blog/post_create.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('p_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('p_list'),
