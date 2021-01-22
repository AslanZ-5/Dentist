from django.shortcuts import render,redirect
from .models import Blog
from .forms import ArticleCreationForm


def blogView(request):
    articles = Blog.objects.all()

    return render(request, 'blog/blogView.html', {'articles': articles})


def detailView(request, pk):
    article = Blog.objects.get(pk=pk)
    return render(request, 'blog/detailView.html', {'article': article})


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


def updateView(request):
    pass
