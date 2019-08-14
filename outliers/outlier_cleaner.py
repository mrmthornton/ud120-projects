#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    

    ### your code goes here
    l = len(ages)
    return_length = int(l*0.9)
    with_error = zip(ages, net_worths, (net_worths - predictions)**2)
    sort_by_err = sorted(with_error, key = lambda x: x[2])
    cleaned_data = sort_by_err[:return_length] #select first 90%

    
    return cleaned_data

