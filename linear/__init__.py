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
def finds_28():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err
        
@check50.check(compiles)
def finds_64():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err    
        
@check50.check(compiles)
def finds_7():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err
        
@check50.check(compiles)
def does_not_find_31():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err 
        
@check50.check(compiles)
def does_not_find_59():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err        
