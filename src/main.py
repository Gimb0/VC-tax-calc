# usr/bin/env python3

from taxObjects import taxYear
from taxCalculator import taxCalculator

# CMD Line user interface asking user for taxable income


def getUserTaxableIncome(tY: taxYear):
    valid = False
    userMsg = "Please enter your total taxable income for the full income year: "

    while not valid:
        try:
            taxableIncome = input(userMsg)

            floatTaxableIncome = float(taxableIncome)

            tY.insertTaxableIncome(floatTaxableIncome)

            valid = True
        except ValueError:
            userMsg = "Please enter your income in the format: 123456.78"
        except Exception as e:
            print(f"Error occurred:\n{e}")

    return

# CMD Line user interface asking user for the financial year


def getUserFinancialYear(tY: taxYear):
    valid = False
    userMsg = "Please enter the income year (eg: 2020-2021):  "

    while not valid:
        try:
            FY = input(userMsg)
            FYList = FY.split("-")

            FYStart = int(FYList[0])
            FYEnd = int(FYList[1])

            if FYEnd != FYStart + 1:
                userMsg = "Please enter a valid Financial Year (eg. 2020-2021): "
            else:
                tY.insertFYStart(FYStart)
                tY.insertFYEnd(FYEnd)

                valid = True
        except ValueError:
            userMsg = "Please enter the income year in the format YYYY-YYYY (eg: 2020-2021): "
        except Exception as e:
            print(f"Error occurred\n{e}")
            exit(1)

    return


def main():
    print("Simple ATO Tax Calculator")
    tY = taxYear()

    getUserFinancialYear(tY)

    getUserTaxableIncome(tY)

    tc = taxCalculator(tY)

    print(f"\nYou have to pay ${tc.calculateTax()} in tax")


if __name__ == "__main__":
    main()
