import sys

def main():
    #Boolean data type creation
    b1 = False
    b2 = True

    print("b1:", b1, "b2:", b2)
    print("type(b1):", type(b1), "type(b2):", type(b2))
    print("id(b1):", id(b1), "id(b2):", id(b2))

    #operation = Negation

    b3 = (not b1)
    b4 = (not b2)
    print("b3:", b3, "b4:", b4)

    #Conjunction- ANDING
    print("b1 and b1:", b1 and b1)
    print("b1 and b2:", b1 and b2)

    #Disjunction(ORING)
    print("b1 or b2:", b1 or b2)
    print("b2 or b1:", b2 or b1)

    #Integer operations
    n1 = 20
    n2 = 7
    print("n1 + n2:", n1 + n2)
    print("n1 - n2:", n1 - n2)
    print("n1 * n2:", n1 * n2)
    print("n1 // n2:", n1 // n2)
    print("n1 % n2:", n1 % n2)
    print("n1 / n2:", n1 / n2)
    print("n1 ** n2:", n1 ** n2) #power operation

    print("----------------------------------------")

    #Arbitory precision of arithmetic integer
    n1 = 2531164332323
    n2 = 1747496326832371065336325432
    n3 = n1 * n2
    print("n1:", n1)
    print("n2:", n2)
    print("n3 = n1 * n2:", n3)

    print("----------------------------------------")

    #creating int from string
    s = "123456"
    print("s:", s, "type(s):", type(s))
    n = int(s)
    print("n:", n, "type(n):", type(n))

    print("----------------------------------------")

    #Creating integer from floating point numbers= here fractional
    #part will be truncated
    f = 3.14
    print("f:", f, "type(f):", type(f))
    m = int(f)
    print("m:", m, "type(m):", type(m))

    print("----------------------------------------")

    #creating int from boolean
    b1 = False
    b2 = True
    n1 = int(b1)
    n2 = int(b2)
    print("n1:", n1, "type(n1):", type(n1))
    print("n2:", n2, "type(n2):", type(n2))

    print("----------------------------------------")

    f1 = 3.15
    f2 = 6.28

    print("f1/f2:", f1/f2)
    print("f1**f2:", f1**f2)

    print("----------------------------------------")

    #creating float from string
    s = "6.433"
    print("type(s):", type(s))
    f = float(s)
    print("type(f):", type(f))

    print("----------------------------------------")
    #creating float from int
    m = 549
    print("m:", m, "type(m):", type(m))
    f = float(m)
    print("f:", f, "type(f):", type(f))

    sys.exit(0)

    
    
    
main()


