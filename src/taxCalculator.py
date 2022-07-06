from taxObjects import taxYear, IndividualTaxBracket
from taxRatesHandler import TaxRatesHandler


class taxCalculator:
    taxRatesHandler = TaxRatesHandler()

    def __init__(self, ty: taxYear) -> None:
        self.taxYear = ty

    # Return amount of tax to pay
    def calculateTax(self):
        taxBracket = self.taxRatesHandler.getIndividualTaxBracket(
            self.taxYear.taxableIncome, self.taxYear.FYStart, self.taxYear.FYEnd)

        taxAmount = str(round(taxBracket["lumpSumTax"] +
                              (taxBracket["taxRate"] * 0.01 *
                               (self.taxYear.taxableIncome - taxBracket["taxRateThreshold"])), 2))

        return taxAmount
