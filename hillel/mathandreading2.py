solvedmathProblems = int(raw_input("how many math problems did you solve today ?"))
reading = float(raw_input("how many pages did you read today?"))
if solvedmathProblems >= 11 and reading >= 15:
    print "You are done for the day."
if solvedmathProblems >= 11 and reading < 15:
    print "You need to work on your reading."
if solvedmathProblems < 11 and reading >= 15:
    print "You need to work on your math"
if solvedmathProblems < 11 and reading < 15:
    print "You still need to work on math and reading."



raw_input()
     









