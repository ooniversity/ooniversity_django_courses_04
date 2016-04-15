from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from coaches.models import Coach


def detail(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    return render(request, 'coaches/detail.html', {'coach': coach})
