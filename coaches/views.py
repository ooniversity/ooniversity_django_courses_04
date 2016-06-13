# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Coach


def detail(request, teacher_id):
    teacher = Coach.objects.get(pk=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'coaches/detail.html', context)
