from django.shortcuts import render
from subprocess import check_output
import searchGTD

def home(request):
    return render(request, "index.html")

def search(request):
    searchParam = request.GET["query"]

    results = searchGTD.search(searchParam)
    args = {"results":results}

    return render(request, "searchResult.html", args)
