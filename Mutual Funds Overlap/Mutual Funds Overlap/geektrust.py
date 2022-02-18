import json, sys, os, pdb

class Funds():

    def __init__(self):
        pass

    def getuniFundsHoldings(self):
        with open('stockHoldings.json', 'r') as data:
            self.uniFundsHoldings = json.loads(data.read())["funds"]


class Portfolio():

    def __init__(self, portfoliofundNames):
        self.portfoliofundNames = portfoliofundNames
        self.portfolioHoldings = dict()

    def getHoldingsFromEachFund(self, uniFundsHoldings):
        for fundDetail in uniFundsHoldings:
            if fundDetail["name"] in self.portfoliofundNames:
                self.portfolioHoldings[fundDetail["name"]] = fundDetail["stocks"]


def readInstructionsFile(instructionsFilePath):
    with open(instructionsFilePath, 'r') as data:
        instructions = data.read()

    instructions = instructions.split('\n')
    return instructions

def calculateOverlap(indexfundName, indexFundHoldings, portFolioFunds, portfolioHoldings):
    overlapsFound = []
    for fundName in portFolioFunds:
        commonFundsCount = 0

        for Stock in portfolioHoldings[fundName]:
            if Stock in indexFundHoldings:
                commonFundsCount += 1

        overlapValue = 2 * ((commonFundsCount)/(len(indexFundHoldings) +  len(portfolioHoldings[fundName]))) *  100

        if overlapValue > 0:
            overlapFound = "{0:s} {1:s} {2:.2f}%".format(indexfundName, fundName, overlapValue)
            print(overlapFound)
            overlapsFound.append(overlapFound)

    return overlapsFound



def main(instructionsFilePath):
    if not instructionsFilePath:
        instructionsFilePath = sys.argv[1]
    instructionsFilePath = os.path.join(instructionsFilePath)
    instructions = readInstructionsFile(instructionsFilePath)

    AllFunds = Funds()
    AllFunds.getuniFundsHoldings()

    # Getting our current portfolio
    for instruction in instructions:
        if 'CURRENT_PORTFOLIO' in instruction:
            portFolioFunds = instruction.split(' ')[1:]
            myPortfolio = Portfolio(portFolioFunds)
            myPortfolio.getHoldingsFromEachFund(AllFunds.uniFundsHoldings)

    # Calculating Overlap of Stocks Between Different Funds (OR) # Adding more stocks to portfolio
    overlapsForGivenFund = []
    for instruction in instructions:
        if 'CALCULATE_OVERLAP' in instruction:
            fundName = instruction.split(' ')[1]
            fundFound = False

            for fundDetail in AllFunds.uniFundsHoldings:
                if fundDetail["name"] == fundName:
                    fundFound = True
                    indexFundHoldings = fundDetail["stocks"]
                    fundOverlap = calculateOverlap(fundName, indexFundHoldings, portFolioFunds, myPortfolio.portfolioHoldings)
                    overlapsForGivenFund.append(fundOverlap)
                    break

            if not fundFound:
                print("FUND_NOT_FOUND")
            continue

        elif 'ADD_STOCK' in instruction:
                fundName, stockAdded = (instruction.split(' ')[1], ' '.join(instruction.split(' ')[2:]))
                myPortfolio.portfolioHoldings[fundName].append(stockAdded)

    return overlapsForGivenFund

if __name__ == '__main__':
    instructionsFilePath = ''
    main(instructionsFilePath)
