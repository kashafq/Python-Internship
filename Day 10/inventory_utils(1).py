import os
def export_inventory_report(products, filename="Inventory_Report.txt"):
    try:
        print("Export function called.") 
        with open(filename, 'w', encoding='utf-8', errors='replace') as f:
            f.write('---< Inventory Summary >---\n\n')
            for i, product in enumerate(products, 1):
                line = (f"{i}) {product.name} -> Quantity: {product.quantity}, "
                        f"Unit Price: Rs.{product.price}, Total Value: Rs.{product.total_value():.2f}\n")
                f.write(line)
        
        full_path = os.path.abspath(filename)
        print(f"Inventory report exported successfully to:\n{full_path}")

    except Exception as e:
        print("Error while exporting:", e)
