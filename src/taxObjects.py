from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass
class IndividualTaxBracket():
    FYStart: int
    FYEnd: int
    taxBracketID: int
    lumpSumTax: float
    taxRate: float
    taxRateThreshold: float
    taxableIncomeStart: float
    taxableIncomeFinish: float

    def __str__(self) -> str:
        return str(f"\t\tFY Start: {self.FYStart}\n\t\tFY End: {self.FYEnd}\n")


@dataclass
class TaxYear():
    FYStart: int
    FYEnd: int
    taxBrackets: tuple()

    def __str__(self) -> str:
        return str(f"\tFY Start: {self.FYStart}\n\tFY End: {self.FYEnd}\n")


@dataclass_json
@dataclass
class TaxRates():
    AllTaxYears: tuple()

    def __str__(self) -> str:
        out = "{\n"
        for i in self.AllTaxYears:
            out += str(i)

        return out + "\n}"


class taxYear:
    def insertFYStart(self, FYStart: int):
        self.FYStart = FYStart

    def insertFYEnd(self, FYEnd: int):
        self.FYEnd = FYEnd

    def insertTaxableIncome(self, taxableIncome: float):
        self.taxableIncome = taxableIncome
