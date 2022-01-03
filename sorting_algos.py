def bubble_sort(collection):
    for pass_num in range(1, len(collection)):
        for i in range(len(collection) - pass_num):
            if collection[i] > collection[i+1]:
                collection[i], collection[i+1] = collection[i+1], collection[i]


def selection_sort(collection):
    for pass_num in range(len(collection) - 1):
        max_index = 0
        last_index = len(collection) - pass_num - 1
        for i in range(len(collection) - pass_num):
            if collection[i] > collection[max_index]:
                max_index = i
        collection[last_index], collection[max_index] = collection[max_index], collection[last_index]


def insertion_sort(collection):
    for i in range(1, len(collection)):
        current_value = collection[i]
        position = i
        while position > 0 and collection[position-1] > current_value:
            collection[position] = collection[position-1]
            position -= 1
        collection[position] = current_value


def shell_sort(collection):
    sublist_count = len(collection) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(collection, start_position, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(collection, start, gap):
    for i in range(start + gap, len(collection), gap):
        current_value = collection[i]
        position = i
        while position >= gap and collection[position - gap] > current_value:
            collection[position] = collection[position - gap]
            position -= gap
        collection[position] = current_value


def merge_sort(collection):
    if len(collection) > 1:
        midpoint = len(collection) // 2
        left_half = collection[:midpoint]
        right_half = collection[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        idx_left = 0
        idx_right = 0
        idx = 0
        while idx_left < len(left_half) and idx_right < len(right_half):
            if left_half[idx_left] <= right_half[idx_right]:
                collection[idx] = left_half[idx_left]
                idx_left += 1
            else:
                collection[idx] = right_half[idx_right]
                idx_right += 1
            idx += 1

        while idx_left < len(left_half):
            collection[idx] = left_half[idx_left]
            idx_left += 1
            idx += 1

        while idx_right < len(right_half):
            collection[idx] = right_half[idx_right]
            idx_right += 1
            idx += 1


def quick_sort(collection):
    quick_sort_helper(collection, 0, len(collection) - 1)

def quick_sort_helper(collection, start, end):
    if start < end:
        split_point = partition(collection, start, end)
        quick_sort_helper(collection, start, split_point - 1)
        quick_sort_helper(collection, split_point + 1, end)

def partition(collection, start, end):
    pivot_value = collection[start]
    left_mark = start + 1
    right_mark = end
    done = False
    while not done:
        while left_mark <= right_mark and collection[left_mark] <= pivot_value:
            left_mark += 1
        while collection[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            collection[left_mark], collection[right_mark] = collection[right_mark], collection[left_mark]
    collection[start], collection[right_mark] = collection[right_mark], collection[start]
    return right_mark
            
my_list = [53, 5, 3, 10, 2, 6]
merge_sort(my_list)
print(my_list)