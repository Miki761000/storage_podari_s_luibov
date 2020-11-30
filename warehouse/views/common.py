def calculate_quantity_and_price(pk, product, quantities):
    product_quantity_add = sum([quantity.product_quantity_add for quantity in quantities.filter(product_id=pk)])
    product_quantity_remove = sum([quantity.product_quantity_sale for quantity in quantities.filter(product_id=pk)])
    product_quantity_return = sum([quantity.product_quantity_returned for quantity in quantities.filter(product_id=pk)])
    product_quantity_waste = sum([quantity.product_quantity_waste for quantity in quantities.filter(product_id=pk)])
    product.product_quantity = product_quantity_add - product_quantity_remove + product_quantity_return - product_quantity_waste

    product_price_sum_add = sum([quantity.product_quantity_add * quantity.product_delivery_price_add for quantity in quantities.filter(product_id=pk)])
    product_price_sum_ret = sum([quantity.product_quantity_returned * quantity.product_delivery_price_add for quantity in quantities.filter(product_id=pk)])
    if product_quantity_add != 0:
        product.product_delivery_price = round((product_price_sum_add + product_price_sum_ret) / product_quantity_add, 2)

    return product.product_quantity, product.product_delivery_price

