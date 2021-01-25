from django.shortcuts import render, redirect
from .models import Blog
from .forms import ArticleCreationForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



def blogView(request):
    articles = Blog.objects.all()

    return render(request, 'blog/blogView.html', {'articles': articles})


def detailView(request, pk):
    article = Blog.objects.get(pk=pk)
    return render(request, 'blog/detailView.html', {'article': article})


class updateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Blog
    fields = ['title', 'text']
    template_name = 'blog/update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class deleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:blog')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required(login_url='/login/')
def createView(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect(instance.get_absolute_url())
    else:
        form = ArticleCreationForm()
    return render(request, 'blog/art_create.html', {'form': form})
