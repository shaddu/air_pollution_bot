# -*- coding: utf-8 -*-


def handler(event, context):
    # Your code goes here!
    # e = event.get('e')
    # pi = event.get('pi')
    # return e + pi
    city = event['currentIntent']['slots']['city']
    session_attributes = event['sessionAttributes'] if event['sessionAttributes'] is not None else {}

    # + " is highly polluted"
    return close(
        session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': city + ' is highly polluted '
        }
    )

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response
