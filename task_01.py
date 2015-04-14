#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Combining two datasets using dictionaries """


def sum_orders(customers, orders):
    """Function takes two parameters customers and orders and combine
       the values into a single dictionary.
       Arg:
            customers(dict): a nested dictionary containing names and emails.
            orders(dict): a nested dictionary containing information like
                          customer id and order total.
      Return:
            returns a new dictionary combined with the keys and containing
            data from two dictionaries.
      Examples:
                CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                      5: {'name': 'Person Two', 'email': 'email@two.com'}}
                  ORDERS = {1: {'customer_id': 2, 'total': 10},
                      3: {'customer_id': 2, 'total': 10},
                      4: {'customer_id': 3, 'total': 15}}
                  >>>

    """
dict1 = {}
for cust in orders.itervalues():
    if cust['customer_id'] in dict1.keys():
        order1 = dict1[cust]['orders'] + 1
        total1 = dict1[cust]['total'] + [cust]['total']
    else:
        no_of_orders = 1
        order_total = [cust]['total']
        name1 = customers[somekey]['name']
        email1 = customers[somekey]['email']

return dict1
