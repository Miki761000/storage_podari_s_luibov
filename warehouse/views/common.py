from django.core.paginator import Paginator, EmptyPage, InvalidPage


def calculate_quantity_and_price(id, product, quantities):
    product_quantity_add = sum([quantity.product_quantity_add for quantity in quantities.filter(product_id=id)])
    product_quantity_remove = sum([quantity.product_quantity_sale for quantity in quantities.filter(product_id=id)])
    product_quantity_return = sum([quantity.product_quantity_returned for quantity in quantities.filter(product_id=id)])
    product_quantity_waste = sum([quantity.product_quantity_waste for quantity in quantities.filter(product_id=id)])
    product.product_quantity = product_quantity_add - product_quantity_remove + product_quantity_return - product_quantity_waste

    product_price_sum_add = sum([quantity.product_quantity_add * quantity.product_delivery_price_add for quantity in quantities.filter(product_id=id)])
    product_price_sum_ret = sum([quantity.product_quantity_returned * quantity.product_delivery_price_add for quantity in quantities.filter(product_id=id)])
    if product_quantity_add != 0:
        product.product_delivery_price = round((product_price_sum_add + product_price_sum_ret) / product_quantity_add, 2)

    return product.product_quantity, product.product_delivery_price


def page_range_def(request, type, items_per_page):
    paginator = Paginator(type, items_per_page)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        type = paginator.page(page)
    except(EmptyPage, InvalidPage):
        type = paginator.page(1)

    # Get the index of the current page
    index = type.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]

    return page_range
