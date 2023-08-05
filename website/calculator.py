# this script uses a simple algorithm to calculate the compost ratio based on waste type and pile size

def calculate_compost_ratios(waste_type, pile_size, composting_time):
    """
    Calculates the ideal proportions of organic materials for composting based on user inputs.
    Args:
        waste_type (str): The type of organic waste being composted (e.g. food waste, livestock waste, household waste)
        pile_size (int): The size of the compost pile in kilograms
        composting_time (int): The desired composting time in months
    Returns:
        A dictionary containing the ideal ratios of nitrogen-rich materials, potassium-rich materials, and moisture.
    """
    if waste_type == 'Agricultural waste':
        # Ideal ratios for food scraps composting
        nitrogen_ratio = 25 # nitrogen to potassium ratio
        Potassium_ratio = 1
        moisture = 50 # ideal moisture level in percentage
    elif waste_type == 'Livestock waste':
        # Ideal ratios for yard waste composting
        nitrogen_ratio = 30
        Potassium_ratio = 1
        moisture = 60
    elif waste_type == 'Fooder and Sludge':
        # Ideal ratios for coffee grounds composting
        nitrogen_ratio = 20
        Potassium_ratio = 1
        moisture = 60
    elif waste_type == 'Paper waste':
        # Ideal ratios for paper waste composting
        nitrogen_ratio = 175
        Potassium_ratio = 1
        moisture = 40
    elif waste_type == 'Household waste':
        # Ideal ratios for manure composting
        nitrogen_ratio = 20
        Potassium_ratio = 1
        moisture = 50
    else:
        raise ValueError('Invalid waste type')
    
    # Calculate the amount of nitrogen-rich and Potassium-rich materials needed based on the pile size and desired composting time
    nitrogen_materials = pile_size * nitrogen_ratio * composting_time
    Potassium_materials = pile_size * Potassium_ratio * composting_time
    
    # Calculate the amount of moisture needed based on the total weight of the compost pile
    total_weight = nitrogen_materials + Potassium_materials
    moisture_amount = round(((moisture / 100) * total_weight), 2)
    
    # Calculate the final ratios of nitrogen-rich and potassium-rich materials and return them as a dictionary
    nitrogen_ratio_final = round((nitrogen_materials / total_weight), 2)
    Potassium_ratio_final = round((Potassium_materials / total_weight), 2)
    return {'nitrogen_ratio': nitrogen_ratio_final, 'Potassium_ratio': Potassium_ratio_final, 'moisture': moisture_amount}