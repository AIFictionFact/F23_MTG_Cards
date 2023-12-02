colorless_cost = ["","[","\\","]","^","_","`","{","|","}"]

def parse_cost(values):
    result_string = ""

    if values[5] < 10: 
        result_string+=colorless_cost[values[5]] # Add Colorless mana symbol

    for number in range(values[3]): # Add White mana symbols
        result_string += "@"  

    for number in range(values[1]): # Add Blue mana symbols
        result_string += "+"

    for number in range(values[4]): # Add Black mana symbols
        result_string += "="

    for number in range(values[0]): # Add Red mana symbols
        result_string += "<"

    for number in range(values[2]): # Add Green mana symbols
        result_string += ">"

    
    return result_string

def parse_type(values):
    result_string = ""

    if values[6] == 1:
        result_string += "Creature "
    if values[7] == 1:
        result_string += "Instant "
    if values[8] == 1:
        result_string += "Sorcery "
    if values[9] == 1:
        result_string += "Artifact "
    if values[10] == 1:
        result_string += "Enchantment "

    return result_string


# Example usage:
numbers = [1, 1, 1, 1, 1, 2]
result = parse_cost(numbers)
print(result)
