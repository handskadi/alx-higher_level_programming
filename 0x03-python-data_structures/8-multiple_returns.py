#!/usr/bin/python3
def multiple_returns(sentence):
    # Define a fun tht returns a tuple with the len of a str and its 1st char
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
