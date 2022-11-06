@staticmethod
def pizza_money(balance, actual, offenders_amount):
    amount = actual - balance
    print(f"The Amount left to pay is :${amount:,}")
    total_amount = amount / offenders_amount
    print(f"You will need to pay ${total_amount:,}  per person to complete the money:${amount:,}")
    return total_amount


if __name__ == "__main__":
    pizza_money(4300, 10000, 100)
