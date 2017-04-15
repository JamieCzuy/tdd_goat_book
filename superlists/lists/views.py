from django.shortcuts import redirect
from django.shortcuts import render

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    else:
        items = Item.objects.all()
        return render(request, 'home.html', {'items': items})
