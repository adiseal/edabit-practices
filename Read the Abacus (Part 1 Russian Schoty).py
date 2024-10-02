def schoty(wires):
    # Initialize an empty string to store the final number
    number = ''
    
    # Iterate over each wire to count the beads on the left of the "---"
    for wire in wires:
        # Count how many "O"s are on the left side of the "---"
        left_beads = wire.split('---')[0].count('O')
        # Add the left bead count to the number string
        number += str(left_beads)
    
    # Return the number as an integer
    return int(number)