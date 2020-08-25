from django.views import generic
from .models import Post,Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'detail.html'
    context_object_name='ppost'
    def get_context_data(self,**kwargs):
        context_data = super(DetailView,self).get_context_data(**kwargs)
        context_data['form'] = CommentForm()
        context_data['comments'] = self.object.comment_set.all()
        return context_data


def comment_craete(request,post_id):
    if not request.user.is_anonymous:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            messages.info(request,"올바르지 않은 댓글 형식입니다")
    else:
        messages.info(request,"로그인을 해주세요 ")
    return HttpResponseRedirect(reverse('detail',args=(post_id,)))

def comment_delete(request,comment_id,post_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if my_comment.author == request.user:
        my_comment.delete() 
    else:
        messages.info(request,"댓글 작성자와 아이디가 일치하지 않습니다")
    return HttpResponseRedirect(reverse('detail',args=(post_id,)))

def comment_update(request,comment_id,post_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if my_comment.author == request.user:
        comment_form = CommentForm(instance=my_comment)
        if request.method == "POST":
            updated_form = CommentForm(request.POST, instance = my_comment)
            if updated_form.is_valid():
                updated_form.save()
                return HttpResponseRedirect(reverse('detail',args=(post_id,)))
        return render(request,'update.html',{'comment_form':comment_form} )
    else:
        messages.info(request,"댓글 작성자가 아닙니다")
        return HttpResponseRedirect(reverse('detail',args=(post_id,)))
