"""
In the morning all the doors in the school are closed. The school is quite big: there are N doors. Then pupils start coming. It might be hard to believe, but all of them want to study! Also, there are exactly N children studying in this school, and they come one by one.

When these strange children pass by some doors they change their status (i.e. Open -> Closed, Closed -> Open). Each student has their number, and each i-th student alters the status of every i-th door. For example: when the first child comes to the schools, he changes every first door (he opens all of them). The second one changes the status of every second door (he closes some doors: the 2nd, the 4th and so on). Finally, when the last one – the n-th – comes to the school, he changes the status of each n-th door (there's only one such door, though).

You need to count how many doors are left opened after all the students have come.


Here you can see red squares – closed doors, green – opened ones.

Input:

n – the number of doors and students, n ∈ N, n ∈ [1, 100000]

Output:

o – the number of opened doors, o ∈ N

doors(5)
Should return

2


"""



def doors(n):
    school_doors = [False] * n
    for i in range(1, n + 1):
        for j in range(i - 1, n, i):
            school_doors[j] = False if school_doors[j] else True
    return school_doors.count(True)









from random import randrange

def changern(a):
    if isinstance(a,bool):
        return not a
    else:
        return [not i for i in a]

def door(n):
    return int(n ** .5)
    
test.describe("Basic tests")
test.assert_equals(doors(5), 2)
test.assert_equals(doors(10), 3)
test.assert_equals(doors(100), 10)

test.describe("Random tests")
for i in range(100):
    j = randrange(100000)    
    test.assert_equals(doors(j), door(j))