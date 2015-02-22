# This program exports a finction which extracts Bloomberg data from csv files
# containing details regarding specific entries

def bloombergData():
    migration = []
    for line in open("MigrationData.txt"):
        terms = line[0:-1].split(",")
        migration += terms

    risk = []
    for line in open("RiskData.txt"):
        terms = line[0:-1].split(",")
        risk += terms

    stocks = []
    for line in open("StockIndexData.txt"):
        terms = line[0:-1].split(",")
        stocks += terms

    bonds = []
    for line in open("BondsData.txt"):
        terms = line[0:-1].split(",")
        bonds += terms

    return {
            "migration":migration,
            "risk":risk,
            "stocks":stocks,
            "bonds":bonds
            }

