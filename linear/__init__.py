import check50
import check50.c
import re

@check50.check()
def exists(self):
    """linear.c exists."""
    check50.exists("linear.c")

@check50.check(exists)
def compiles():
    """linear.c compiles."""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def finds_Chen():
    """finds Chen"""
    check50.run("./linear").stdin("Chen").stdout("Calling Chen\n").exit(0)
        
@check50.check(compiles)
def finds_Malan():
    """finds Malan"""
    check50.run("./linear").stdin("Malan").stdout("Calling Malan\n").exit(0)
        
@check50.check(compiles)
def does_not_finds_Tanzosh():
    """does not finds Tanzosh"""
    check50.run("./linear").stdin("Tanzosh").stdout("Quitting\n").exit(0)
        
