from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A  view that renders that shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # if item in bag update quanity
        bag[item_id] += quantity
    else:
        # if item not in bag add to bag
        bag[item_id] = quantity

    # overwrite session varaible with updated version of bag
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
