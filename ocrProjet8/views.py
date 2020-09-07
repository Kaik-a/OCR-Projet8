from django.shortcuts import render

from search.forms import SearchForm


def home(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
    else:
        form = SearchForm()
    return render(request, 'home.html', {'form': form})


def legal_notice(request):
    return render(request, 'notice.html')


def contact(request):
    return render(request, 'contact.html')
