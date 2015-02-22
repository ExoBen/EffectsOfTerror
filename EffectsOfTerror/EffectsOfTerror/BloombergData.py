# This program exports a finction which extracts Bloomberg data from csv files
# containing details regarding specific entries

def getData():
    migration = []
    for line in open("MigrationData.txt"):
        terms = line[0:-1].split(",")
        migration.append(reversed(terms))

    risk = []
    for line in open("RiskData.txt"):
        terms = line[0:-1].split(",")
        risk.append(reversed(terms))

    stocks = []
    for line in open("StockIndexData.txt"):
        terms = line[0:-1].split(",")
        stocks.append(reversed(terms))

    bonds = []
    for line in open("BondsData.txt"):
        terms = line[0:-1].split(",")
        bonds.append(reversed(terms))

    return {
            "migration":migration,
            "risk":risk,
            "stocks":stocks,
            "bonds":bonds
            }

