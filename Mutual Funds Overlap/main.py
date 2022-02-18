import json, sys, os, pdb

class Funds():

    def __init__(self):
        pass

    def GetUniFundsHoldings(self):
        with open('StockHoldings.json', 'r') as data:
            self.UniFundsHoldings = json.loads(data.read())["funds"]


class Portfolio():

    def __init__(self, PortfolioFundNames):
        self.PortfolioFundNames = PortfolioFundNames
        self.PortfolioHoldings = dict()

    def GetHoldingsFromEachFund(self, UniFundsHoldings):
        for FundDetail in UniFundsHoldings:
            if FundDetail["name"] in self.PortfolioFundNames:
                self.PortfolioHoldings[FundDetail["name"]] = FundDetail["stocks"]


def ReadInstructionsFile(InstructionsFilePath):
    with open(InstructionsFilePath, 'r') as data:
        instructions = data.read()

    instructions = instructions.split('\n')
    return instructions

def CalculateOverlap(IndexFundName, IndexFundHoldings, PortfolioHoldings):
    for FundName in PortfolioHoldings:
        CommonFundsCount = 0
        print(f"Checking Overlap(%) Between {IndexFundName} and {FundName}")

        for Stock in PortfolioHoldings[FundName]:
            if Stock in IndexFundHoldings:
                CommonFundsCount += 1

        OverlapValue = 2 * ((CommonFundsCount)/(len(IndexFundHoldings) +  len(PortfolioHoldings[FundName]))) *  100
        print(f"\tOverlap Found is {round(OverlapValue, 2)}%")
# def ParseInstructions(instructions):
#     instructions = instructions.split('\n')
#
#     for instruction in instructions:
#         pass

def main():
    InstructionsFilePath = sys.argv[1]
    InstructionsFilePath = os.path.join(InstructionsFilePath)
    instructions = ReadInstructionsFile(InstructionsFilePath)

    AllFunds = Funds()
    AllFunds.GetUniFundsHoldings()

    # Getting our current portfolio
    for instruction in instructions:
        if 'CURRENT_PORTFOLIO' in instruction:
            PortFolioFunds = instruction.split(' ')[1:]
            MyPortfolio = Portfolio(PortFolioFunds)
            MyPortfolio.GetHoldingsFromEachFund(AllFunds.UniFundsHoldings)

    # Calculating Overlap of Stocks Between Different Funds (OR) # Adding more stocks to portfolio
    for instruction in instructions:
        if 'CALCULATE_OVERLAP' in instruction:
            FundName = instruction.split(' ')[1]

            for FundDetail in AllFunds.UniFundsHoldings:
                if FundDetail["name"] == FundName:
                    IndexFundHoldings = FundDetail["stocks"]
                    CalculateOverlap(FundName, IndexFundHoldings, MyPortfolio.PortfolioHoldings)

            print("FUND_NOT_FOUND")


        elif 'ADD_STOCK' in instruction:
                FundName, StockAdded = instruction.split(' ')[1:]
                MyPortfolio.PortfolioHoldings[FundName].append(StockAdded)
