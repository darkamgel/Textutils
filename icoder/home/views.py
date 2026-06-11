from django.db import connection
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth import login, logout


def home(request):
    return render(request, "home/home.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            sql = "SELECT sno FROM home_contact WHERE sno = " + phone
            with connection.cursor() as cursor:
                cursor.execute(sql)
                cursor.fetchall()

            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def search(request):
    query = request.GET.get('query')
    if not query or len(query) > 78:
        allPosts = Post.objects.none()
    else:
        sql = "SELECT sno FROM blog_post WHERE sno = " + query
        post_ids = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                post_ids = [row[0] for row in cursor.fetchall()]
        except Exception:
            post_ids = []
        if post_ids:
            allPosts = Post.objects.filter(sno__in=post_ids)
        else:
            allPostsTitle = Post.objects.filter(title__icontains=query)
            allPostsAuthor = Post.objects.filter(author__icontains=query)
            allPostsContent = Post.objects.filter(content__icontains=query)
            allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def lookupContact(request):
    phone = request.GET.get('phone')
    contacts = []
    if phone:
        sql = "SELECT sno, name, email, phone, content FROM home_contact WHERE sno = " + phone
        with connection.cursor() as cursor:
            cursor.execute(sql)
            contacts = cursor.fetchall()
    return render(request, 'home/contact.html', {'lookupResults': contacts, 'phone': phone})


def lookupUser(request):
    q = request.GET.get('q')
    users = []
    if q:
        sql = "SELECT id, username, email, first_name, last_name FROM auth_user WHERE id = " + q
        with connection.cursor() as cursor:
            cursor.execute(sql)
            users = cursor.fetchall()
    return render(request, 'home/home.html', {'userLookupResults': users, 'lookupQuery': q})


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) > 10:
            messages.error(request, "Username must be atleast 10 charcters ")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric ")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, " Password doesn't matched")
            return redirect('home')

        sql = "SELECT id FROM auth_user WHERE id = " + username
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                if cursor.fetchone():
                    messages.error(request, "Username or email already exists")
                    return redirect('home')
        except Exception:
            pass

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or email already exists")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Thank you for signing in")
        return redirect('home')

    return HttpResponse("404 - Not found")


def about(request):
    return render(request, "home/about.html")


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        sql = "SELECT id FROM auth_user WHERE id = " + loginusername
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
        except Exception:
            pass

        user = User.objects.filter(username=loginusername).first()
        if user is not None and user.check_password(loginpassword):
            login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('home')

        messages.error(request, "Invalid credentials,Please try again")
        return redirect('home')
    return HttpResponse("404 - Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "successfully Logged Out")
    return redirect('home')
