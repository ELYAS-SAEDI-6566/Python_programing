def fruits(tuple_of_fruits): 
    result = {}
    for fruit in tuple_of_fruits :
        if fruit['shape'] == 'sphere' and 600 >= fruit['mass'] >= 300 and 500 >= fruit['volume'] >= 100 :
            if fruit["name"] not in result:
                result[fruit["name"]] = 0
                result[fruit["name"]] += 1
            else :
                result[fruit["name"]] += 1
    return result
#_____________For exampel_____________#
# print(fruits((
#     {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
#     {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
#     {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
#     {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))