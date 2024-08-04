def total_sales(sales_table, product):
    # Get the list of product names from the first row
    product_names = sales_table[0]
    
    # Check if the product is in the list of product names
    if product not in product_names:
        return "Product not found"
    
    # Find the index of the product in the product names list
    product_index = product_names.index(product)
    
    # Initialize the total sales counter
    total = 0
    
    # Loop through the rows of sales data (excluding the first row)
    for row in sales_table[1:]:
        total += row[product_index]
    
    return total