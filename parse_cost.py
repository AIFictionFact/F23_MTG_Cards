colorless_cost = ["","[","\\","]","^","_","`","{","|","}"]

def parse_cost(values):
    result_string = ""

    result_string+=colorless_cost[values[5]] # Add Colorless mana symbol

    for number in range(values[0]): # Add White mana symbols
        result_string += "@"  

    for number in range(values[1]): # Add Blue mana symbols
        result_string += "+"

    for number in range(values[2]): # Add Black mana symbols
        result_string += "="

    for number in range(values[3]): # Add Red mana symbols
        result_string += "<"

    for number in range(values[4]): # Add Green mana symbols
        result_string += ">"

    
    return result_string

# Example usage:
numbers = [1, 1, 1, 1, 1, 2]
result = parse_cost(numbers)
print(result)