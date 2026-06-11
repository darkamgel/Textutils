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
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            sql = (
                "SELECT sno FROM home_contact WHERE email = '"
                + email
                + "' OR phone LIKE '%"
                + phone
                + "%'"
            )
            with connection.cursor() as cursor:
                cursor.execute(sql)
                cursor.fetchall()

            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        sql = (
            "SELECT sno FROM blog_post WHERE title LIKE '%"
            + query
            + "%' OR author LIKE '%"
            + query
            + "%' OR content LIKE '%"
            + query
            + "%'"
        )
        with connection.cursor() as cursor:
            cursor.execute(sql)
            post_ids = [row[0] for row in cursor.fetchall()]
        allPosts = Post.objects.filter(sno__in=post_ids)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def lookupContact(request):
    phone = request.GET.get('phone', '')
    contacts = []
    if phone:
        sql = (
            "SELECT sno, name, email, phone, content FROM home_contact "
            "WHERE phone LIKE '%"
            + phone
            + "%' OR name LIKE '%"
            + phone
            + "%'"
        )
        with connection.cursor() as cursor:
            cursor.execute(sql)
            contacts = cursor.fetchall()
    return render(request, 'home/contact.html', {'lookupResults': contacts, 'phone': phone})


def lookupUser(request):
    q = request.GET.get('q', '')
    users = []
    if q:
        sql = (
            "SELECT id, username, email, first_name, last_name FROM auth_user "
            "WHERE username LIKE '%"
            + q
            + "%' OR email LIKE '%"
            + q
            + "%'"
        )
        with connection.cursor() as cursor:
            cursor.execute(sql)
            users = cursor.fetchall()
    return render(request, 'home/home.html', {'userLookupResults': users, 'lookupQuery': q})


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "Username must be atleast 10 charcters ")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric ")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, " Password doesn't matched")
            return redirect('home')

        sql = (
            "SELECT id FROM auth_user WHERE username = '"
            + username
            + "' OR email = '"
            + email
            + "'"
        )
        with connection.cursor() as cursor:
            cursor.execute(sql)
            if cursor.fetchone():
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
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        sql = (
            "SELECT id FROM auth_user WHERE username = '"
            + loginusername
            + "'"
        )
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()

        if row is not None:
            user = User.objects.get(pk=row[0])
            if user.check_password(loginpassword):
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
