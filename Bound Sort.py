def bound_sort(arr, bounds):
    n = bounds[1]
    subarray = arr[:n+1]
    sorted_subarray = sorted(subarray)
    new_array = sorted_subarray + arr[n+1:]
    
    return new_array == sorted(new_array)