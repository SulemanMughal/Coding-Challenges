# Challenge No. 40

Create a function that checks if the box is completely filled with the asterisk symbol *.

**Examples**

    completely_filled([
      "#####",
      "#***#",
      "#***#",
      "#***#",
      "#####"
    ]) ➞ True
     
    completely_filled([
      "#####",
      "#* *#",
      "#***#",
      "#***#",
      "#####"
    ]) ➞ False
     
    completely_filled([
      "###",
      "#*#",
      "###"
    ]) ➞ True
     
    completely_filled([
      "##",
      "##"
    ]) ➞ True

**Notes**

    Boxes of size n <= 2 are considered automatically filled (see example #4).

    Empty space will always be a space character (" ").