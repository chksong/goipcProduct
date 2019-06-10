from django.shortcuts import render

# Create your views here.


# 画表格
def index(request):
    return render(request, 'product/product.html')