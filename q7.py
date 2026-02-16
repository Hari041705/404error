# Team Name: 404error
def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    result = {}
    for fruits in fruit_list:
        if fruits in result:
            result[fruits] += 1
        else:
            result[fruits] = 1
    return result
