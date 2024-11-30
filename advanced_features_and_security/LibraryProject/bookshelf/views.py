# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article, Book
from .forms import ExampleForm

@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # logic to edit the article
    return render(request, 'edit_article.html', {'article': article})

def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()
    # Render the book list to a template
    return render(request, 'bookshelf/book_list.html', {'books': books})

#Use Django ORM for queries
def secure_search_view(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) #Case-insensitive filter
    return render(request, 'bookshelf/book_list.html', {'books': books})

#Use the ExampleForm in views.py to validate user inputs.
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Use query safely
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
