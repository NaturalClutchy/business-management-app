def display_paginated(items, items_per_page=5):
    total = len(items)
    page = 0
    while True:
        start = page * items_per_page
        end = start + items_per_page
        page_items = items[start:end]
        if not page_items:
            print("No more items.")
            return
        for item in page_items:
            print(item)

        print("\nOptions:")
        print("N - Next page")
        print("P - Previous page")
        print("E - Exit")
        choice = input("Enter your choice: ").lower().strip()
        if choice == "n":
            page += 1
        elif choice == "p" and page > 0:
            page -= 1
        elif choice == "e":
            break
        else:
            print("Invalid option.")
