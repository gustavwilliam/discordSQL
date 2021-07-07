from collections import UserDict


class ObjectDict(UserDict):
    """
    A dictionary where the keys are the values of a certain attribute of the items.
    
    Default attribute to use as key is "name".
    
    Example usage:
    
    >>> class Table:
    ...     def __init__(self, name):
    ...         self.name = name
    ...         
    >>> tables = ObjectDict(
    ...     Table("rock"),
    ...     Table("block of wood"),
    ...     Table("cardboard box"),
    ... )
    ... 
    >>> tables["rock"]
    <__main__.Table object at XXX>
    >>> tables["cardboard box"].name
    cardboard box
    """
    def __init__(self, *args, key: str = "name") -> None:
        super().__init__()
        for arg in args:
            self[getattr(arg, key)] = arg
