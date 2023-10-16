def superheroes(names):
    # Initialize an empty list to store the names of superheroes ending in "man."
    superman_names = []
    
    # Iterate through the list of names.
    for name in names:
        # Convert the name to lowercase for case-insensitive matching.
        lowercase_name = name.lower()
        
        # Check if the lowercase name ends with "man" and is not a superheroine.
        if lowercase_name.endswith("man") and "woman" not in lowercase_name:
            superman_names.append(name)
    
    # Sort the list of superhero names alphabetically and return it.
    return sorted(superman_names)

