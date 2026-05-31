import numpy as np

def get_stats(list_of_numbers):
    """Calculates the sum, count, and average (I assume mean) of a list of numbers"""
    return_list = {
        "sum":np.sum(list_of_numbers),
        "count":len(list_of_numbers),
        "average":np.mean(list_of_numbers)
    }
    return return_list