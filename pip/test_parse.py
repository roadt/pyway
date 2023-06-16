
import parse
from parse import *

#   From there it's a simple thing to parse a string:
parse("It's {}, I love it!", "It's spam, I love it!")

#    Or to search a string for some pattern:
search('Age: {:d}\n', 'Name: Rufus\nAge: 42\nColor: red\n')

#    Or find all the occurrences of some pattern in a string:
''.join(r[0] for r in findall(">{}<", "<p>the <b>bold</b> text</p>"))


#    If you're going to use the same pattern to match lots of strings you can
#    compile it once:
p = compile("It's {}, I love it!")
print(p)
p.parse("It's spam, I love it!")
p.parse("It's candy, I love it!")


#    The default behaviour is to match strings case insensitively. You may match with
#    case by specifying `case_sensitive=True`:
parse('SPAM', 'spam', case_sensitive=True) is None



'''
    Format Syntax
    -------------
    
    A basic version of the `Format String Syntax`_ is supported with anonymous
    (fixed-position), named and formatted fields::
    
       {[field name]:[format spec]}
    
    Field names must be a valid Python identifiers, including dotted names;
    element indexes imply dictionaries (see below for example).
    
    Numbered fields are also not supported: the result of parsing will include
    the parsed fields in the order they are parsed.
    
    The conversion of fields to types other than strings is done based on the
    type in the format specification, which mirrors the ``format()`` behaviour.
    There are no "!" field conversions like ``format()`` has.
'''
parse("Bring me a {}", "Bring me a shrubbery")
r = parse("The {} who {} {}", "The knights who say Ni!")
print(r)
print(r.fixed)
print(r[0])
print(r[1:])



r = parse("Bring out the holy {item}", "Bring out the holy hand grenade")
print(r)
print(r.named)
print(r['item'])
'item' in r


'''
    Note that `in` only works if you have named fields.
    
    Dotted names and indexes are possible with some limits. Only word identifiers
    are supported (ie. no numeric indexes) and the application must make additional
    sense of the result:
'''

r = parse("Mmm, {food.type}, I love it!", "Mmm, spam, I love it!")
print(r)
print(r.named)
print(r['food.type'])

r = parse("My quest is {quest[name]}", "My quest is to seek the holy grail!")
print(r)
print(r['quest'])
print(r['quest']['name'])

#    If the text you're matching has braces in it you can match those by including
#    a double-brace ``{{`` or ``}}`` in your format string, just like format() does.

'''
    Format Specification
    --------------------
    
    Most often a straight format-less ``{}`` will suffice where a more complex
    format specification might have been used.
    
    Most of `format()`'s `Format Specification Mini-Language`_ is supported:
    
       [[fill]align][0][width][.precision][type]
    
    The differences between `parse()` and `format()` are:
    
    - The align operators will cause spaces (or specified fill character) to be
      stripped from the parsed value. The width is not enforced; it just indicates
      there may be whitespace or "0"s to strip.
    - Numeric parsing will automatically handle a "0b", "0o" or "0x" prefix.
      That is, the "#" format character is handled automatically by d, b, o
      and x formats. For "d" any will be accepted, but for the others the correct
      prefix must be present if at all.
    - Numeric sign is handled automatically.
    - The thousands separator is handled automatically if the "n" type is used.
    - The types supported are a slightly different mix to the format() types.  Some
      format() types come directly over: "d", "n", "%", "f", "e", "b", "o" and "x".
      In addition some regular expression character group types "D", "w", "W", "s"
      and "S" are also available.
    - The "e" and "g" types are case-insensitive so there is not need for
      the "E" or "G" types. The "e" type handles Fortran formatted numbers (no
      leading 0 before the decimal point).
    
    ===== =========================================== ========
    Type  Characters Matched                          Output
    ===== =========================================== ========
    l     Letters (ASCII)                             str
    w     Letters, numbers and underscore             str
    W     Not letters, numbers and underscore         str
    s     Whitespace                                  str
    S     Non-whitespace                              str
    d     Digits (effectively integer numbers)        int
    D     Non-digit                                   str
    n     Numbers with thousands separators (, or .)  int
    %     Percentage (converted to value/100.0)       float
    f     Fixed-point numbers                         float
    F     Decimal numbers                             Decimal
    e     Floating-point numbers with exponent        float
          e.g. 1.1e-10, NAN (all case insensitive)
    g     General number format (either d, f or e)    float
    b     Binary numbers                              int
    o     Octal numbers                               int
    x     Hexadecimal numbers (lower and upper case)  int
    ti    ISO 8601 format date/time                   datetime
          e.g. 1972-01-20T10:21:36Z ("T" and "Z"
          optional)
    te    RFC2822 e-mail format date/time             datetime
          e.g. Mon, 20 Jan 1972 10:21:36 +1000
    tg    Global (day/month) format date/time         datetime
          e.g. 20/1/1972 10:21:36 AM +1:00
    ta    US (month/day) format date/time             datetime
          e.g. 1/20/1972 10:21:36 PM +10:30
    tc    ctime() format date/time                    datetime
          e.g. Sun Sep 16 01:03:52 1973
    th    HTTP log format date/time                   datetime
          e.g. 21/Nov/2011:00:07:11 +0000
    ts    Linux system log format date/time           datetime
          e.g. Nov  9 03:37:44
    tt    Time                                        time
          e.g. 10:21:36 PM -5:30
    ===== =========================================== ========
    
'''


