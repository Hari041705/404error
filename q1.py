#Team Name: 404error
def calculate_total_bill(amount: float, tip_percent: int) -> float:
    amount = float(amount)
    tip_percent = float(tip_percent)
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)
print(calculate_total_bill(100, 15))  