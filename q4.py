# Team Name: 404error
def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        if is_student:
            return 12
        else:
            return 15
print(get_ticket_price(10, False))  