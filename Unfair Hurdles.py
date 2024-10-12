def is_unfair_hurdle(hurdles):
    # Check the height of the hurdles
    height = len(hurdles)
    
    # If height is at least 4, we have a tall hurdle
    is_tall = height >= 4
    
    # Check the spacing between hurdles
    # The first row will be used to determine spacing
    first_row = hurdles[0]
    
    # Count spaces between the first two hurdles
    first_hurdle_index = first_row.find('#')
    second_hurdle_index = first_row.find('#', first_hurdle_index + 1)
    
    # Calculate the number of spaces between the two hurdles
    if second_hurdle_index != -1:
        spacing = second_hurdle_index - first_hurdle_index - 1
        is_close = spacing < 4
    else:
        is_close = False  # If there's only one hurdle, we can't consider it close
    
    # Return True if either condition for unfairness is met
    return is_tall or is_close

