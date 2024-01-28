class Bill:

    def __init__(self, amount: int = 0, period: str = "") -> None:
        self.amount = amount
        self.period = period

    def __repr__(self):
        return f"Bill({self.amount!r}, {self.period!r})"

class Flatmate:

    def __init__(self, name: str = "", days_in_house: int = 0) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def __repr__(self):
        return f"Flatmate({self.name!r}, {self.days_in_house!r})"


def pays(bill, flatmates: tuple = ()) -> dict:
    total_days = sum([x.days_in_house for x in flatmates])
    day_price = bill.amount / total_days
    return {x.name: round(x.days_in_house * day_price) for x in flatmates}


class PdfReport:

    def __init__(self, filename: str = "") -> None:
        self.filename = filename

    def generate(self, bill, flatmates: tuple = ()) -> None:
        name = self.filename
        pass


def main():
    bill_amount = int(input("Enter the amount of the bill: "))
    bill_period = input("Enter the period of the bill: ")
    bill = Bill(amount=bill_amount, period=bill_period)
    number_flatmate = int(input("How many flatmate are?: "))
    i = 0
    flatmate = []
    while i < number_flatmate:
        i += 1
        name = str(input("Enter de name of the flatmate: "))
        day_in_house = int(input("Enter the days that the flatmate stayed in the house: "))
        flatmate.append(Flatmate(name=name, days_in_house=day_in_house))

    flatmates = tuple(flatmate)
    pay_dict = pays(bill, flatmates)
    print(pay_dict)


if __name__ == "__main__":
    main()
