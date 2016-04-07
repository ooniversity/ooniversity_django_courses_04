from equation import Equation, input_parameter

def main():
    print "a*x^2 + b*x + c = 0"
    print "Enter the coefficient for the quadratic equation"
    a = input_parameter()
    b = input_parameter('b')
    c = input_parameter('c')

    qe = Equation(a, b, c)
    qe.calc_discr()

    if qe.get_discr() < 0:
        print "Roots of the equation does not exist"
    else:
        x1 = qe.get_eq_root()
        x2 = qe.get_eq_root(order=2)
        if x1 == x2:
            print "There is one equation root x1=x2=%g" % x1
        else:
            "There are roots of equation x1=%g, x2=%g" % (x1, x2)

if __name__ == "__main__":
    main()
