import subprocess

def search(searchParam, maxNum):
    #Use grep to search file and gather results
    c1 = ['grep', "-F", "-m", maxNum, searchParam, "../GTD.csv"]
    p1 = subprocess.Popen(c1, stdout=subprocess.PIPE)

    #Pass results of grep to the Haskell script for parsing
    c2 = ['../resultsParser']
    p2 = subprocess.Popen(c2, stdin=p1.stdout,stdout=subprocess.PIPE)

    #Return the result of the Haskell script
    result = p2.stdout.read()
    return result
