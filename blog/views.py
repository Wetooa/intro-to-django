from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from .forms import ContactForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=posts)
    return render(request, "post_detail.html", {"posts": posts, "comments": comments})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            return render(request, "success.html", {"name": name})
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
