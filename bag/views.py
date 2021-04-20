from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A  view that renders that shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # create or get session variable
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
            # if item in bag update quanity
            bag[item_id] += quantity
        else:
            # if item not in bag add to bag
            bag[item_id] = quantity

    # overwrite session varaible with updated version of bag
    request.session['bag'] = bag

    return redirect(redirect_url)
