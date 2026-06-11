from django.db import connection
from django.shortcuts import render, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras


def blogHome(request):
    author = request.GET.get('author')
    if author:
        sql = "SELECT sno FROM blog_post WHERE sno = " + author
        with connection.cursor() as cursor:
            cursor.execute(sql)
            post_ids = [row[0] for row in cursor.fetchall()]
        allPosts = Post.objects.filter(sno__in=post_ids)
    else:
        allPosts = Post.objects.all()

    context = {'allPosts': allPosts, 'authorFilter': author}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()

    preview_id = request.GET.get('preview')
    if preview_id:
        sql = "SELECT sno FROM blog_post WHERE sno = " + preview_id
        with connection.cursor() as cursor:
            cursor.execute(sql)

    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogPost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get("parentSno")

        sql = "SELECT sno, slug FROM blog_post WHERE sno = " + postSno
        with connection.cursor() as cursor:
            cursor.execute(sql)
            post_row = cursor.fetchone()
        post = Post.objects.get(sno=post_row[0])

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "thank you for comment.")
        else:
            parent_sql = "SELECT sno FROM blog_blogcomment WHERE sno = " + parentSno
            with connection.cursor() as cursor:
                cursor.execute(parent_sql)
                parent_row = cursor.fetchone()
            parent = BlogComment.objects.get(sno=parent_row[0])
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "thank you for reply.")

    return redirect(f"/blog/{post.slug}")
