import eel
from core import array_oops, matric_oops, utils

@eel.expose
def arr_min(arr):
    return array_oops.arr_min(arr)

@eel.expose
def arr_search_sorted(arr, value):
    try:
        return array_oops.arr_search_sorted(arr, value)
    except utils.UnsortedArrayError:
        return "unsorted"