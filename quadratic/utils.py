#def input_parameter_a(p):
#    if p.replace('-', '').isdigit() and int(p) != 0:
#       return int(p)


def input_parameter(p):
    if p.replace('-', '').isdigit():
        return int(p)

def type_parametrs(item):
    if type(item) is int:
        item = 1
    else:
        item = 0
    return item



def get_discr(a, b, c):
    if type(a) and type(b) and type(c) is int:
        if a != 0: 
            d = b ** 2 - 4 * a * c
        else:
            d=''    
    return d


#def input_parameter(p):
 #   if p.replace('-', '').isdigit() and int(p) !=0:
  #      return int(p)
   # else:
    #    print '!!!'
