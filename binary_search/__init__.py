import check50
import check50.c
import re

@check50.check()
def exists(self):
    """binary.c exists."""
    check50.exists("binary.c")

@check50.check(exists)
def compiles():
    """binary.c compiles."""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def finds_18():
    """finds 18"""
    check50.run("./binary").stdin("18").stdout("Found\n").exit(0)
        
@check50.check(compiles)
def finds_2():
    """finds 2"""
    check50.run("./linear").stdin("2").stdout("Found\n").exit(0)
        
@check50.check(compiles)
def finds_20():
    """finds 20"""
    check50.run("./linear").stdin("20").stdout("Found\n").exit(0)
        
@check50.check(compiles)
def does_not_find_9():
    """does not find 9"""
    check50.run("./linear").stdin("9").stdout("Not found!\n").exit(0)
        
@check50.check(compiles)
def does_not_find_30():
    """does not find 30"""
    check50.run("./linear").stdin("30").stdout("Not found!\n").exit(0)
