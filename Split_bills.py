def split_expenses(names, expenses):
    total_expenses = sum(expenses)
    num_people = len(names)
    each_share = total_expenses / num_people

    balances = {name: expense - each_share for name, expense in zip(names, expenses)}

    while any(abs(balance) > 1e-9 for balance in balances.values()):
        payer = max(balances, key=balances.get)
        receiver = min(balances, key=balances.get)

        if balances[payer] == 0 or balances[receiver] == 0:
            break

        amount = min(abs(balances[payer]), abs(balances[receiver]))
        balances[payer] -= amount
        balances[receiver] += amount

        print(f"{receiver} needs to pay {payer} an amount of {amount:.2f}")


def main():
    names = []
    expenses = []

    print("Enter the names and expenses for each person (separated by space):")
    print("Example: John 50.00")
    print("Type 'done' to finish input.")

    while True:
        input_data = input().strip().lower()

        if input_data == 'done':
            break

        data = input_data.split()
        if len(data) != 2:
            print("Invalid input. Try again.")
            continue

        person, expense_str = data
        try:
            expense = float(expense_str)
        except ValueError:
            print("Invalid expense amount. Try again.")
            continue

        names.append(person)
        expenses.append(expense)

    print("\nExpense distribution:")
    split_expenses(names, expenses)


if __name__ == "__main__":
    main()
