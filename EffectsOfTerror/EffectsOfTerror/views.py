from django.shortcuts import render
from subprocess import check_output
import searchGTD
import bloomberg

def home(request):
    return render(request, "index.html")

def search(request):
    searchParam = request.GET["query"]

    results = [searchGTD.search(searchParam, "30")]
    args = {"results":results[0]}

    return render(request, "searchResult.html", args)

def graph(request):
    result = bloomberg.request()
    args = {}
    for value in result["data"]:
        args[value] = value["securityData"]["fieldData"]
    args = {"result": result}
    return render(request, "graphData.html", args)
