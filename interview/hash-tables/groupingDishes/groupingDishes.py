from collections import defaultdict
def groupingDishes(dishes):
    d = defaultdict(list)
    for dish in dishes:
        for ingredient in dish[1:]:
            d[ingredient].append(dish[0])
            
    arr = []
    for i, d in d.items():
        if len(d) > 1:
            arr.append([i] + sorted(d))
            
    return sorted(arr, key=lambda x: x[0])