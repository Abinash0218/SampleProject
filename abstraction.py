class ATM:
    def withdraw(self):
        self.__check()
        print("Money Withdrawn")

    def __check(self):
        print("Checking Balance")

atm=ATM()
atm.withdraw()