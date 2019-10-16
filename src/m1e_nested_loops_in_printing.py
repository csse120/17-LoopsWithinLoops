"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and many others before them.
"""
# -----------------------------------------------------------------------------
# Students: READ and RUN this program.  There is nothing else for you
#           to do in here. But DO study these examples carefully,
#           and refer back to them as necessary.
# -----------------------------------------------------------------------------


def main():
    """ Calls the other functions to demonstrate them. """
    classic_example_1(4, 7)
    classic_example_2(6)
    classic_example_3(5, 9)


def classic_example_1(n, m):
    """ Prints the loop variables of a loop within a loop. """
    # -------------------------------------------------------------------------
    # Classic nested-loops, type 1:
    #    The number of inner-loop iterations does NOT depend
    #    on the current value of the outer-loop variable.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------')
    print('Classic example 1:')
    print('-----------------------------')

    for k in range(n):
        for j in range(m):
            print(k, j)
        print('Completed the inner loop {} times'.format(k + 1))


def classic_example_2(n):
    """ Prints the loop variables of a loop within a loop. """
    # -------------------------------------------------------------------------
    # Classic nested-loops, type 2:
    #    The number of inner-loop iterations DOES depend
    #    on the current value of the outer-loop variable.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------')
    print('Classic example 2:')
    print('-----------------------------')

    for k in range(n):  # The ONLY difference from the previous
        for j in range(k + 1):  # example is   k+1   on this line.
            print(k, j)
        print('Completed the inner loop {} times'.format(k + 1))


def classic_example_3(n, m):
    """
    Prints a multiplication table for numbers from 1 to n multiplied
    by numbers from 1 to m, where n and m are the given parameters.
    Prints only the products (unlike classic example 1),
    and prints each "chunk" of the table on a single row.

    Preconditions: n and m are positive integers.
    """
    # -------------------------------------------------------------------------
    # Same as classic example 1, but shows how to keep successive
    # print statements on the same line, then go to the next line.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------')
    print('Classic example 1:')
    print('-----------------------------')

    for k in range(n):
        print(k, end=':  ')
        for j in range(m):
            print(' ', j, end='')
        print('Completed the inner loop {} times'.format(k + 1))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
