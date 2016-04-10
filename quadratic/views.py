from django.shortcuts import render


class Equation(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_discriminant(self):
        return self.d

    def get_eq_root(self, order=1):
        if order == 1:
            x = (-self.b + self.d ** (1/2.0)) / 2 * self.a
        else:
            x = (-self.b - self.d ** (1/2.0)) / 2 * self.a
        return x


def quadratic_results(request):
    if str(request.GET.get('a')).isdigit():
        argument_a = int(request.GET.get('a'))
    else:
        try:
            argument_a = int(request.GET.get('a'))
        except ValueError:
            argument_a = str(request.GET.get('a'))

    if str(request.GET.get('b')).isdigit():
        argument_b = int(request.GET.get('b'))
    else:
        try:
            argument_b = int(request.GET.get('b'))
        except ValueError:
            argument_b = str(request.GET.get('b'))

    if str(request.GET.get('c')).isdigit():
        argument_c = int(request.GET.get('c'))
    else:
        try:
            argument_c = int(request.GET.get('c'))
        except ValueError:
            argument_c = str(request.GET.get('c'))

    if type(argument_a) == int and type(argument_b) == int and type(argument_c) == int:
        equation_inst = Equation(argument_a, argument_b, argument_c)
        if equation_inst.get_discriminant() < 0:
            discriminant = equation_inst.get_discriminant()

            parameters = {
                'a': argument_a,
                'b': argument_b,
                'c': argument_c,
                'discr': discriminant,
            }
            return render(request, 'results.html', parameters)
        else:
            discriminant = equation_inst.get_discriminant()
            x1 = equation_inst.get_eq_root()
            x2 = equation_inst.get_eq_root(order=2)
            if x1 == x2:
                if type(argument_a) == str:
                    err_str_a = True
                else:
                    err_str_a = False
                if type(argument_b) == str:
                    err_str_b = True
                else:
                    err_str_b = False
                if type(argument_c) == str:
                    err_str_c = True
                else:
                    err_str_c = False

                parameters = {
                    'a': argument_a,
                    'b': argument_b,
                    'c': argument_c,
                    'erra': err_str_a,
                    'errb': err_str_b,
                    'errc': err_str_c,
                    'discr': discriminant,
                    'x1': x1,
                }
                return render(request, 'results.html', parameters)
            else:
                if type(argument_a) == str:
                    err_str_a = True
                else:
                    err_str_a = False
                if type(argument_b) == str:
                    err_str_b = True
                else:
                    err_str_b = False
                if type(argument_c) == str:
                    err_str_c = True
                else:
                    err_str_c = False

                discriminant = equation_inst.get_discriminant()
                parameters = {
                    'a': argument_a,
                    'b': argument_b,
                    'c': argument_c,
                    'erra': err_str_a,
                    'errb': err_str_b,
                    'errc': err_str_c,
                    'discr': discriminant,
                    'x1': x1,
                    'x2': x2,
                }
                return render(request, 'results.html', parameters)
    else:
        if type(argument_a) == str:
            err_str_a = True
        else:
            err_str_a = False
        if type(argument_b) == str:
            err_str_b = True
        else:
            err_str_b = False
        if type(argument_c) == str:
            err_str_c = True
        else:
            err_str_c = False

        discriminant = None
        parameters = {
            'a': argument_a,
            'b': argument_b,
            'c': argument_c,
            'erra': err_str_a,
            'errb': err_str_b,
            'errc': err_str_c,
            'discr': discriminant,
        }
        return render(request, 'results.html', parameters)
