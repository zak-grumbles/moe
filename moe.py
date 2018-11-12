""" moe.py

A set of functions that can be used to select an item from a list using the
"Eeny, Meeny, Miny, Moe" method.

There are a few versions of the rhyme. The "regular" one is as follows:

Eeny, Meeny, Miny, Moe
Catch a tiger by his toe
If he hollers let him go
Eeny, Meeny, Miny, Moe
My mother told me
To pick the very best one
And you are it

This script will deal with a few different versions of the rhyme:

"regular"   -   As written above
"short"     -   Does not contain the last three lines
"not"       -   Has a "not" before the "it" on the final line.
"""

# Lengths of the various versions of the rhyme
REGULAR_LENGTH = 30
NOT_LENGTH = 31
SHORT_LENGTH = 16


"""
Performs the selection on the given list with the given rhyme length.

:param  items            list to select from.
:param  rhyme_length     Number of words in version of rhyme.
:return selected item from given items.
"""
def pick(items, rhyme_length):

    if items is None or rhyme_length is None or len(items) == 0:
        return None
    else:
        num_items = len(items)

        if num_items >= rhyme_length:
            return items[rhyme_length - 1]
        elif rhyme_length % num_items == 0:
            return items[-1]
        else:
            index = rhyme_length % num_items
            return items[index - 1]


"""
Calls the pick method with the short rhyme length.

:param  items        items to select from.
:return selected item.
"""
def short_moe(items):
    global SHORT_LENGTH

    return pick(items, SHORT_LENGTH)


"""
Calls the pick method with the regular rhyme length.

:param  items        items to select from.
:return selected item.
"""
def moe(items):
    global REGULAR_LENGTH

    return pick(items, REGULAR_LENGTH)


"""
Calls the pick method with the "not" rhyme length.

:param  items        items to select from.
:return selected item.
"""
def not_moe(items):
    global NOT_LENGTH

    return pick(items, NOT_LENGTH)

