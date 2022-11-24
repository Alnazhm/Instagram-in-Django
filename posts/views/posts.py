from django.views.generic import CreateView, View, FormView, DeleteView, UpdateView,DetailView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from posts.forms import PostForm
from posts.models import Post
from posts.models import Comment
from accounts.forms import CommentForm


class PostCreateView(CreateView):
    template_name = 'create_post.html'
    form_class = PostForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_id = self.kwargs['pk']
            form.save()
            return redirect('profile', pk=self.kwargs['pk'])
        context = {}
        context['form'] = form
        return self.render_to_response(context)


    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class PostLikeView(View):
    model = Post
    post_object = None

    def post(self, request, *args, **kwargs):
        self.post_object = get_object_or_404(Post, pk=kwargs.get('pk'))
        self.post_object.user_likes.add(request.user)
        Post.objects.filter(id=self.post_object.id).update(likes_count=(self.post_object.likes_count + 1))
        users_who_likes_post = self.post_object.posts_likes.values_list('author_id', flat=True)
        if request.user.pk in users_who_likes_post:
            self.remove_like()
        else:
            self.set_like()
        return redirect('index')

    def set_like(self):
        self.post_object.posts_likes.create(author=self.request.user)

    def remove_like(self):
        self.post_object.posts_likes.get(author=self.request.user).delete()


class CommentCreateView(FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            user = request.user
            Comment.objects.create(author=user, post=post, text=comment)
            user.commented_posts.add(post)
            Post.objects.filter(id=post.id).update(comments_count=(post.comments_count + 1))
        return redirect('index')


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class PostEditView(UpdateView):
    template_name = 'post_update.html'
    form_class = PostForm
    model = Post
    context_object_name = 'post'


    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    success_url = '/'