# 1.Basic - Print all integers from 0 to 150.
for x in range(151):
    print(x)
# 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for mul in range(5,1001):
    if mul% 5 == 0:
        print(mul)
# 3Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead.
#  If divisible by 10, print "Coding Dojo".
for multi in range(1, 101):
    if multi % 10 == 0:
        print("Coding")
    elif multi % 5 == 0:
        print("Coding Dojo")
    else:
        print(multi)
# 4Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
final_sum = 0
for odd in range(500001):
   if odd % 2 != 0:
        # print(odd)
        final_sum += odd
print(final_sum)
# 5Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdoun in range(2018,0,-4):
    print(countdoun)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for counter in range(lowNum, (highNum + 1)):
    if counter % mult == 0:
        print(counter)
