# Team Name: 404error
def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    result = {}
    for fruits in fruit_list:
        if fruits in result:
            result[fruits] += 1
        else:
            result[fruits] = 1
    return result
assert count_inventory(["apple", "banana", "apple", "cherry"]) == {"apple": 2, "banana": 1, "cherry": 1}
assert count_inventory([]) == {}
assert count_inventory(["grape"]) == {"grape": 1}
assert count_inventory(["orange", "orange"]) == {"orange": 2}
assert count_inventory(["Apple", "apple"]) == {"Apple": 1, "apple": 1}