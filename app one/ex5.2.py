wait = ['john', 'edmond', 'mike']
# THIS IS FOR DESCENDING ORDER
wait.sort(reverse=True)
# WAIT.SORT() THIS IS FOR ASCENDING ORDER
for index, items in enumerate(wait):
    row = f"{index + 1}.{items.capitalize()}"
    print(row)
