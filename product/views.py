from django.shortcuts import render

# Create your views here.


# 画表格
def index(request):
    return render(request, 'product/excelPro2.html')


def searchProduct(request,slug=None):
    return render(request,'product/excelPro.html',{'IDNUM':slug})