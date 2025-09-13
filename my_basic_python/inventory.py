stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():# k as key, v as value, inventory.items() iterate over key-value pairs
        print(str(v) + " " + k)
        item_total += v # adds all the value pairs together
    print("Total number of items: " + str(item_total))

display_inventory(stuff)

# Another inventory example
def add_to_inventory(inventory, added_items):
    for item in added_items: # for each item in the added_items list
        # add the item to the inventory dictionary
        # if the item already exists, increment its count
        # if it does not exist, add it with a count of 1
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print("Inventory:")
    item_total = 0
    
    for item, count in inventory.items():# counts every item in the inventory
        # print the item and its count
        print(f"{count} {item}(s)")
        item_total += count # total the items
    print("Total number of items: " + str(item_total))
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)