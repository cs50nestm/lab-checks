import check50
import check50.c
import re

@check50.check()
def exists(self):
    """insertion.c exists."""
    check50.exists("insertion.c")

@check50.check(exists)
def compiles():
    """insertion.c compiles."""
    check50.c.compile("insertion.c", lcs50=True)

@check50.check(compiles)
def sorts():
    """sorts {1, 8, 4, 6, 0, 3, 5, 2, 7, 9}"""
    check50.run("./insertion").stdout("0 1 2 3 4 5 6 7 8 9 \n").exit(0)
