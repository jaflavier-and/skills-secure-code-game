'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

# Define limits
MAX_ITEM_VALUE = 100000 # Maximum value
MAX_QUANTITY = 100 # maximum quantity
MIN_QUANTITY = 0 # minimum quantity
MAX_TOTAL_VALUE = 1e6 # Maximum net value of an order

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    # net = 0
    customerPayment = Decimal('0') #total value customer paid
    orderTotalValue = Decimal('0')# total value of order


    for item in order.items:
        # calculate payment from customer
        if item.type == 'payment':
            if -MAX_ITEM_VALUE <= item.amount <= MAX_ITEM_VALUE :
                customerPayment += Decimal(str(item.amount))

        # calculate item values
        elif item.type == 'product' and MIN_QUANTITY <= item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_ITEM_VALUE:
            orderTotalValue += Decimal(str(item.amount)) * Decimal(str(item.quantity))
        else:
            return "Invalid item type: %s" % item.type

    # check for total value exceeding maximum total cost
    if orderTotalValue > MAX_TOTAL_VALUE or abs(customerPayment) > MAX_TOTAL_VALUE:
        return "Total amount payable for an order exceeded"

    if customerPayment != orderTotalValue:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, customerPayment - orderTotalValue)
    else:
        return "Order ID: %s - Full payment received!" % order.id