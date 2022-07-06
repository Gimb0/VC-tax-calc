from taxObjects import TaxRates, TaxYear, IndividualTaxBracket
from os.path import exists
from sys import argv
import traceback


class TaxRatesHandler:
    taxRatesFile: str = "../tax-rates.json"
    taxRates = TaxRates(tuple())

    def __init__(self):

        if exists(self.taxRatesFile):
            with open(self.taxRatesFile, 'r') as f:
                self.taxRates = TaxRates.from_json(f.read())

    # Write tax rates object containing every years data to a local json file
    def saveTaxRatesToFile(self):
        with open(self.taxRatesFile, 'w') as f:
            f.write(self.taxRates.to_json())

    # CMD Line user interface for inserting FY tax data
    def insertFYTaxRates(self):
        print("Inserting tax rates for new financial year")

        valid = False
        taxBracketList = []
        taxYear = TaxYear(0, 0, taxBracketList)

        while not valid:
            try:
                FYStart = int(
                    input("Please enter the financial year start (eg. 2020): "))
                FYEnd = int(
                    input("Please enter the financial year end (eg. 2021): "))
                NumberOfTaxBrackets = int(
                    input("Enter number of tax brackets for this financial year: "))

                taxYear.FYStart = FYStart
                taxYear.FYEnd = FYEnd
                for bracket in range(0, NumberOfTaxBrackets):
                    print(f"Enter the details for bracket: {bracket}")
                    taxableIncomeStart = float(
                        input("Enter the starting taxable income: "))
                    taxableIncomeFinish = float(input(
                        "Enter the finishing taxable income (enter 0 for now limit): "))
                    lumpSum = float(
                        input("Enter the lump sum (enter 0 for no lump sum): "))
                    taxThreshold = float(
                        input("Enter the income tax threshold: "))
                    taxRate = float(
                        input("Enter the tax rate for this bracket: "))

                    taxBracket = IndividualTaxBracket(
                        FYStart, FYEnd, bracket, lumpSum, taxRate, taxThreshold, taxableIncomeStart, taxableIncomeFinish)

                    taxBracket_list = list(taxYear.taxBrackets)
                    taxBracket_list.append(taxBracket)
                    taxYear.taxBrackets = tuple(taxBracket_list)
            except:
                print(f"Error occurred\n")
                traceback.print_exc()
                exit(1)

            valid = True

        allTaxYears_list = list(self.taxRates.AllTaxYears)
        allTaxYears_list.append(taxYear)
        self.taxRates.AllTaxYears = tuple(allTaxYears_list)

        self.saveTaxRatesToFile()

    # Return the tax bracket the user falls under
    def getIndividualTaxBracket(self, taxableIncome, FYStart, FYEnd):
        allTaxYears_list = list(self.taxRates.AllTaxYears)
        taxBrackets = tuple()
        FYFound = False
        for taxYear in allTaxYears_list:
            if taxYear["FYStart"] == FYStart and taxYear["FYEnd"] == FYEnd:
                taxBrackets = taxYear["taxBrackets"]
                FYFound = True
                break

        if not FYFound:
            print(
                "Financial Year not found\n"
                "Insert Financial Year data: python3 taxRatesHandler.py -i"
            )
            exit(1)

        taxBrackets_list = list(taxBrackets)
        for taxBracket in taxBrackets_list:
            if taxableIncome > taxBracket["taxableIncomeStart"] and (taxableIncome < taxBracket["taxableIncomeFinish"] or taxBracket["taxableIncomeFinish"] == 0):
                return taxBracket

        # if taxBracket was not returned then something has gone wrong
        print("error: tax bracket not found\nexiting!!!")
        exit(1)


if __name__ == "__main__":
    trh = TaxRatesHandler()

    if argv[1] == "-i":
        trh.insertFYTaxRates()
