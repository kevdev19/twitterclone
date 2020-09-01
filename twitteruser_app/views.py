from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    return render(request, 'index.html', {})
