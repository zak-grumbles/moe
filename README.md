# moe.py
A few functions that can be used to select an item from a list using the "Eeny, Meeny, Miny, Moe" method.

I wrote this one night after seeing this selection method used in a cartoon and getting
curious about what an algorithmic version of the method would look like. 

It serves no purpose, but here it is.

## Algorithm
In case you are somehow unfamiliar with the selection method, it involves "iterating" through a list
of things, advancing with each word and wrapping at the end if necessary. This makes for a pretty simple
algorithm that can be used for pretty much any rhyme.

```
f(n) = n[ len(n) - 1 ]                  # rhyme_length % num_items == 0
f(n) = n[ rhyme_length % len(n) - 1 ]   # num_items < rhyme_length
f(n) = n[ rhyme_length - 1 ]            # num_items >= rhyme_length
```

## Script
In the script below, I've considered a few different versions of the classic "Eeny, Meeny, Miny, Moe" rhyme,
but the `pick` method could be used with any rhyme. Have fun, although I can't imagine what this could possibly
be useful for.
