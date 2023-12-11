def heapify(array):
    last_parent_idx = len(array) // 2 - 1 
    for idx in range(last_parent_idx, -1, -1): 
        move_down(array, idx, len(array) - 1)
    return array

def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]: 
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx] 
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            break
    

myarr = [23, 44, 11, 27, 54, 35, 13, 61, 22, 48, 41, 39, 52, 17, 65]
print(heapify(myarr))