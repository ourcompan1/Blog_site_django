from django.shortcuts import render, redirect

posts = [
    {
        'Title': 'ТУТ СТАТЬЯ',
        "Description": 'Я почти сам это сделал',
        'Author': 'Тимофей',
        'Date': '26 января 2024 года'
    }
]


def index_page(request):
    return render(request, 'index.html', {'articles': posts, 'page': 'index'})


def about_page(request):
    return render(request, "about.html", {'page': 'about'})


def contact_page(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {'page': 'contact'})
    else:
        print(request.POST)
        return redirect(contact_page)
