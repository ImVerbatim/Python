def len_link(lst):
    """Returns the length of the link.

    >>> lst = link(1, link(2, link(3, link(4))))
    >>> len_link(lst)
    4
    >>> len_link(empty)
    0
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return 0
    return len_link(rest(lst)) + 1

def reduce_links(lst, item, index):
    """ Returns a link matching lst but with the given item inserted at the
    specified index. If the index is greater than the current length, the item
    is appended to the end of the list.

    >>> lst = link(1, link(2, link(3)))
    >>> new = insert(lst, 9001, 1)
    >>> print_link(new)
    1 9001 2 3
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:    #if the list is empty return with item to link
        return link(item, empty)
    elif index == 0:    
        return link(item,lst)
    else:
        return link(first(lst) , insert(rest(lst),item, index-1))

# Linked list ADT

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)
