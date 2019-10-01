import check50
import check50.c

@check50.check()
def exists():
    """linear.c exists."""
    check50.exists("linear.c")

@check50.check()
def compiles():
    """linear.c compiles."""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def finds_28():
    """finds 28"""
    check50.run("./linear").stdin("28").stdout("Found your number! Bingo!\n").exit(0)

        
@check50.check(compiles)
def finds_64():
    """finds 64"""
    check50.run("./linear").stdin("64").stdout("Found your number! Bingo!\n").exit(0)
        
@check50.check(compiles)
def finds_7():
    """finds 7"""
    check50.run("./linear").stdin("7").stdout("Found your number! Bingo!\n").exit(0)
        
@check50.check(compiles)
def does_not_find_31():
    """does not find 31"""
    check50.run("./linear").stdin("31").stdout("Sorry better luck next time!\n").exit(0)
        
@check50.check(compiles)
def does_not_find_59():
     """does not find 59"""
    check50.run("./linear").stdin("59").stdout("Sorry better luck next time!\n").exit(0)
