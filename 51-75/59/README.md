# Challenge No. 59


Create a function that returns the count of all bridges in a two-dimensional grid.

Bridge B should be counted if:

    It connects from one end of the grid to the one opposite to it.

    It is unobstructed.

**Example**

    "#########/#       #/#   #   #/#   #   #/#### ####/#   #   #/#   #   #/#       #/#########"

In this case the number 4 is returned because, when unraveled, the string reveals four bridges that meet the requirements listed above as shown:

    #########/
    #       #/
    #   #   #/
    #   #   #/
    #### ####/
    #   #   #/
    #   #   #/
    #       #/
    #########

**Notes**

-   Slashes / act as separators.

-   Intersecting bridges can still count, as shown.

-   Vertical bridges count as long as the requirements are met.