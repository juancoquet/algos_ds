def sequential_search(list, item):
    for i in list:
        if i == item:
            return True
    return False

def binary_search(list, item):
    if not list:
        return False
    else:
        midpoint_idx = len(list) // 2
        if list[midpoint_idx] == item:
            return True
        else:
            if list[midpoint_idx] > item:
                return binary_search(list[:midpoint_idx], item)
            else:
                return binary_search(list[midpoint_idx+1:], item)

to_search = [1,2,3,4,5,6,7,8,9]

print(binary_search(to_search, 10))

