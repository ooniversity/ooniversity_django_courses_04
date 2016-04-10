# -*- coding: utf-8 --*-
from django.shortcuts import render


def quadratic_results(request):
    a = b = c = discr = ""
    x = x1 = x2 = ""
    a_alert = b_alert = c_alert = discr_alert = str()
    a_selfname = "a = "
    b_selfname = "b = "
    c_selfname = "c = "
    discr_selfname = ""
    x1_selfname = ""
    x2_selfname = ""
    ifexeption = 0
    headertext = u"Квадратное уравнение a*x*x + b*x + c = 0"

    try:
        a = int(request.GET["a"])
    except ValueError:
        ifexeption = 1
        if not request.GET["a"]:
            a_alert = u"коэффициент не определен"
        else:
            a_alert = u"коэффициент не целое число"
            a = request.GET["a"]
    if a == 0:
        ifexeption = 1
        a_alert = u"коэффициент при\
                  первом слагаемом уравнения не может быть равным нулю"

    try:
        b = int(request.GET["b"])
    except ValueError:
        ifexeption = 1
        if not request.GET["b"]:
            b_alert = u"коэффициент не определен"
        else:
            b_alert = u"коэффициент не целое число"
            b = request.GET["b"]

    try:
        c = int(request.GET["c"])
    except ValueError:
        ifexeption = 1
        if not request.GET["c"]:
            c_alert = u"коэффициент не определен"
        else:
            c_alert = u"коэффициент не целое число"
            c = request.GET["c"]

    if ifexeption == 0:
        discr_selfname = u"Дискриминант: "
        discr = b**2 - 4*a*c

        if discr < 0:
            discr_alert = u"Дискриминант меньше нуля, \
                          квадратное уравнение не имеет \
                          действительных решений."

        if discr == 0:
            x = (-b + discr ** (1/2.0)) / 2*a
            discr_alert = u"Дискриминант равен нулю, \
                          квадратное уравнение имеет \
                          один действительный корень: x1 = x2 = "
            x = (-b + discr ** (1/2.0)) / 2*a

        if discr > 0:
            x1 = (-b + discr ** (1/2.0)) / 2*a
            x2 = (-b - discr ** (1/2.0)) / 2*a
            discr_alert = u"Квадратное уравнение \
                          имеет два действительных корня: "
            x1_selfname = "x1 = "
            x2_selfname = ", x2 = "

    renderdict = {"a_selfname": a_selfname, "a": a, "a_alert": a_alert,
                  "b_selfname": b_selfname, "b": b, "b_alert": b_alert,
                  "c_selfname": c_selfname, "c": c, "c_alert": c_alert,
                  "discr_selfname": discr_selfname, "discr": discr,
                  "discr_alert": discr_alert, "oneroot": x,
                  "x1_selfname": x1_selfname, "x2_selfname": x2_selfname,
                  "firstroot": x1, "secondroot": x2, "headertext": headertext
                  }

    return render(request, 'results.html', renderdict)
