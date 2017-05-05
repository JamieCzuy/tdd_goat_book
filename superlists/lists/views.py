from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.shortcuts import render

from lists.models import Item
from lists.models import List


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        item.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/{}/'.format(list_.id))


# Note: I don't like how this function is formatted. I hope he fixes it!
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/{}/'.format(list_.id))
        except ValidationError:
            item.delete()
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})
