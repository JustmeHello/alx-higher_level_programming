#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute] = value

