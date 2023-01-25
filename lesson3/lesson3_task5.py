THOUSAND = 1000
FIVE_HUNDRED = 500
TWO_HUNDRED = 200
ONE_HUNDRED = 100
FIFTY = 50
TWENTY = 20
TEN = 10

MAX_BILLS = 10
MAX_BILLS_TOTAL = (FIVE_HUNDRED + TWO_HUNDRED + ONE_HUNDRED + FIFTY + TWENTY + TEN) * MAX_BILLS

thousand_bills = 0
five_hundred_bills = 0
two_hundred_bills = 0
one_hundred_bills = 0
fifty_bills = 0
twenty_bills = 0
ten_bills = 0

is_found = False

cash = int(input('Enter the amount of cash you need: '))

if cash > MAX_BILLS_TOTAL:
    thousand_bills = (cash - MAX_BILLS_TOTAL) // THOUSAND
    cash = cash - thousand_bills * THOUSAND
    if cash % MAX_BILLS_TOTAL > 0:
        thousand_bills += 1
        cash -= THOUSAND

for i_tens in range(MAX_BILLS, -1, -1):
    if is_found:
        break
    for i_twenties in range(MAX_BILLS, -1, -1):
        if is_found:
            break
        for i_fifties in range(MAX_BILLS, -1, -1):
            if is_found:
                break
            for i_one_hundreds in range(MAX_BILLS, -1, -1):
                if is_found:
                    break
                for i_two_hundreds in range(MAX_BILLS, -1, -1):
                    if is_found:
                        break
                    for i_five_hundreds in range(MAX_BILLS, -1, -1):
                        if is_found:
                            break
                        possible_cash = i_tens * TEN + i_twenties * TWENTY + i_fifties * FIFTY + \
                                        i_one_hundreds * ONE_HUNDRED + i_two_hundreds * TWO_HUNDRED + \
                                        i_five_hundreds * FIVE_HUNDRED
                        if possible_cash == cash:
                            is_found = True
                            ten_bills = i_tens
                            twenty_bills = i_twenties
                            fifty_bills = i_fifties
                            one_hundred_bills = i_one_hundreds
                            two_hundred_bills = i_two_hundreds
                            five_hundred_bills = i_five_hundreds

print(f"You've got the following bills: \n"
      f"{thousand_bills} thousand bill(s), \n"
      f"{five_hundred_bills} five hundred bill(s), \n"
      f"{two_hundred_bills} two hundred bill(s), \n"
      f"{one_hundred_bills} one hundred bill(s), \n"
      f"{fifty_bills} fifty bill(s), \n"
      f"{twenty_bills} twenty bill(s), \n"
      f"{ten_bills} ten bill(s).")
