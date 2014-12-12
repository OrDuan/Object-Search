__author__ = 'Or Duan'


def object_search(string, obj, path='', depth=10):
    """
    This function searches overall object and his recursively iterators and looks for the 'string' var in it.
    @parm: string: The string you would like to search .
    @parm: obj: The object we will search on.
    @parm: path: Used by the function to save the current path
    @parm: depth: How many levels of inner iterators we should go.
    """

    # Stop the recursion
    if depth == 0:
        return

    # For each iterator call the this function again. For each variable check if it equal to 'string'
    for key in (x for x in dir(obj) if not x.startswith('_') and not callable(x)):
        val = getattr(obj, key)
        path = path + '/' + key

        # If found the string, print the current path
        if string in str(key) or string in str(val):
            print path

        # Check if is iterator
        try:
            iterator = iter(val)
        except TypeError:
            continue
        else:
            object_search(string, val, path, depth - 1)

# object_search('ItemDimensions', product)
