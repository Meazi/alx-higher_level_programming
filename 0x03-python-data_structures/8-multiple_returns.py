#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), "None")
    else:
        for itm in sentence:
            return (len(sentence), itm[0])
