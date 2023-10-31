from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from .models import Book
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Create your views here.

def helloView(request):
    return render(request, 'report/home.html')

def uploadView(request):
    if request.method == "POST":
        if file := request.FILES['uploadExcel']:
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                try:
                    Book.objects.create(book_id = row['id'],
                                        book_title = row['title'],
                                        book_subtitle = row['subtitle'],
                                        book_authors = row['authors'],
                                        book_publisher = row['publisher'],
                                        book_publishdate = row['published_date'],
                                        book_category = row['category'],
                                        book_distexpense = row['distribution_expense']
                                        )
                except Exception as e:
                    pass
            return redirect('hello')
    return render(request, 'report/upload.html')

def reportView(request):
    books = Book.objects.all()

    # categoryPlot
    category_counts = {}
    for book in books:
        category = book.book_category
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    categories = list(category_counts.keys())
    counts = list(category_counts.values())
    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts)
    plt.xlabel('Categories')
    plt.ylabel('Number of Books')
    plt.title('Book Categories')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    chart_image = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    context = {
        'chart_image':chart_image
    }

    return render(request, 'report/report.html', context)

