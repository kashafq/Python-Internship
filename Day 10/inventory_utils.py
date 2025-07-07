def export_inventory_report(products, filename="Inventory_Report.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\t---< Inventory Summary >---\n\n')
            for i, product in enumerate(products, 1):
                line = f"{i}) {product.name} -> Quantity: {product.quantity}, Price: Rs.{product.price}\n"
                clean_line = line.encode('ascii', errors='ignore').decode()
                f.write(clean_line)
        print("Export is complete.")
    except Exception as e:
        print("Error:", e)