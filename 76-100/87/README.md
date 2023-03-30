# Challenge No. 87

    Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given string (p).

    Ignore any digit that is placed after or before the given string.

    Whether the first letter is capitalized or not, if all letters of the word match the given string (p), it is valid.

    If it does not match the given string (p) then None.

**Examples**

    find_pattern({
      "Phrase1": "CCOVIDD-19 is no good",
      "Phrase2": "COVID-18 is no good",
      "Phrase3": "COVID-17 is no good"
    }, "COVID-19")
     
    ➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]

    find_pattern({
      "Phrase1": "Edabit is great",
      "Phrase2": "Edabit is very great",
      "Phrase3": "Edabit is really great"
    }, "really")
     
    ➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]