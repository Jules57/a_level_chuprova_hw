THOUSAND = 1000
FIVE_HUNDRED = 500
TWO_HUNDRED = 200
ONE_HUNDRED = 100
FIFTY = 50
TWENTY = 20
TEN = 10

cash = int(input('Enter the amount of cash you need: '))

thousand_bills = cash // THOUSAND
cash %= THOUSAND
five_hundred_bills = cash // FIVE_HUNDRED
cash %= FIVE_HUNDRED
two_hundred_bills = cash // TWO_HUNDRED
cash %= TWO_HUNDRED
one_hundred_bills = cash // ONE_HUNDRED
cash %= ONE_HUNDRED
fifty_bills = cash // FIFTY
cash %= FIFTY
twenty_bills = cash // TWENTY
cash %= TWENTY
ten_bills = cash // TEN


print(f"You've got the following bills: \n"
      f"{thousand_bills} thousand bill(s), \n"
      f"{five_hundred_bills} five hundred bill(s), \n"
      f"{two_hundred_bills} two hundred bill(s), \n"
      f"{one_hundred_bills} one hundred bill(s), \n"
      f"{fifty_bills} fifty bill(s), \n"
      f"{twenty_bills} twenty bill(s), \n"
      f"{ten_bills} ten bill(s).")
