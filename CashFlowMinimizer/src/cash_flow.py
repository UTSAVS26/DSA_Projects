from src.utils import calculate_amount, get_min_index, get_max_index, min_of_2

def min_cash_flow_rec(amount):
    max_credit = get_max_index(amount)
    max_debit = get_min_index(amount)

    if amount[max_credit] == 0 and amount[max_debit] == 0:
        return

    min_val = min_of_2(-amount[max_debit], amount[max_credit])

    amount[max_credit] -= min_val
    amount[max_debit] += min_val

    print(f"Person {max_debit} pays {min_val} to Person {max_credit}")

    min_cash_flow_rec(amount)

def min_cash_flow(graph):
    amount = calculate_amount(graph)
    min_cash_flow_rec(amount)