from django.shortcuts import render
from subprocess import check_output
import searchGTD
import bloombergTests as bloom

import ast

def home(request):
    return render(request, "index.html")

def search(request):
    searchParam = request.GET["query"]

    results = [searchGTD.search(searchParam, "30")]
    args = {"results":results[0]}

    return render(request, "searchResult.html", args)

def graph(request):
    country = request.GET["country"]
    year = request.GET["year"]
    month = request.GET["month"]
    day = request.GET["day"]
    query = bloom.getBloombergQueries(country, year, month, day)
    result = bloom.request(query)
    print result
    args = {}
    args["result"] = result
    return render(request, "graphData.html", args)
