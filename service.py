# -*- coding: utf-8 -*-


def handler(event, context):
    # Your code goes here!
    # e = event.get('e')
    # pi = event.get('pi')
    # return e + pi
    result = event['currentIntent']['slots']['city']
    # + " is highly polluted"
    return result
