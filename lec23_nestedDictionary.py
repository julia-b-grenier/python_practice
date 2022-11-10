"""
Difference :
    • Lists are useful when you have an ordered list of things,
    and the same element might appear more than once.
    Useful whenever order is important!

    • Dictionaries are useful when you have an unordered
    collection, and you would like to ‘index’ on something
    other than non-negative integers. Very useful for
    counting elements.

The values inside a dictionary can themselves be
dictionaries. 
Can we use dictionaries as keys? No, because
dictionaries are mutable, and keys must be immutable!

"""

# Nested dictionnary

cs_enrolment = {"COMP202" : {"W19" : 590, "F19" : 744},
                "COMP250" : {"W19" : 624, "F19" : 633}}

comp202_enrolment = cs_enrolment["COMP202"]

print("In Winter 2019 COMP 202 had", comp202_enrolment["W19"], "students enrolled")


