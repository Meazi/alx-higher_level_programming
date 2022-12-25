#!/usr/bin/python3
def multiple_returns(sentence):
    for itm in sentence:
        return (len(sentence), itm[0])
