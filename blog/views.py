from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Post
from .forms import PostForm


class PostsListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub')


class PostDetailsView(generic.DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

# def posts_list(request):
#     post = Post.objects.filter(status='pub')
#     return render(request, 'blog/posts_list.html', context={'post': post})

# def post_details(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_details.html', context={'post': post})

# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={'form':form})


    # def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})
