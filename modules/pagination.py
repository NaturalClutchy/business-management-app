def display_paginated(items, items_per_page=5):
    for i in range(0, len(items), items_per_page):
        page = items[i:i + items_per_page]
        for index, item in enumerate(page, start=i + 1):
            print(f"{index}. {item.strip()}")
        if i + items_per_page < len(items):
            input(" === Press Enter to view the next page: ")
