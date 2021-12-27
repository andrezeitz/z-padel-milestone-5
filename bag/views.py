from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ View to return bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to bag"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'cloth_size' in request.POST:
        size = request.POST['cloth_size']
    if 'shoe_size_man' in request.POST:
        size = request.POST['shoe_size_man']
    if 'shoe_size_woman' in request.POST:
        size = request.POST['shoe_size_woman']           
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    messages.success(request, f'{product.name} added to cart')        
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a product in the bag"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
            
    messages.info(request, f'{product.name} was updated')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = Product.objects.get(pk=item_id)
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        del bag[item_id]['items_by_size'][size]
        if not bag[item_id]['items_by_size']:
            bag.pop(item_id)
    else:
        bag.pop(item_id)
    
    messages.error(request, f'{product.name} removed from cart')
    request.session['bag'] = bag
    
    return redirect(reverse('view_bag'))