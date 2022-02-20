def decoded_seven_seg(w: bool, x: bool, y: bool, z: bool) -> tuple[bool]:
    """Given 4 binary digits, returns a tuple of 7 segment control values."""

    return ((w or (x and z) or (not x and not z) or y),                 # a
            (w or not x or (y and z) or (not y and not z)),             # b
            (w or x or not y or z),                                     # c
            (w or (x and not y and z) or (not x and y)
             or (not x and not z) or (y and not z)),                    # d
            ((not w or not y) and (not x or y) and not z),              # e
            (w or (x and not y) or (x and not z) or (not y and not z)), # f
            ((w or not x or not y or not z) and (w or x or y)))         # g


def seven_seg(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool) -> str:
    """Given a set of 7 boolean values corresponding to each segment, returns
    a string representation of a 7 segment display.

    The display looks like this:
         _
        |_|
        |_|

    And the mapping of the booleans is as follows:
         a
        fgb
        edc
    """

    return (
        (" _" if a else "") + "\n"
        + ("|" if f else " ") + ("_" if g else " ") + ("|" if b else "") + "\n"
        + ("|" if e else " ") + ("_" if d else " ") + ("|" if c else "") + "\n")
