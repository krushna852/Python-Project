class User:
    def __init__(self,name,income):
        self.name=name
        self.__income=income

class Expense(User):
    hist={"Food":[],
          "Enterntainment":[],
          "Daily Expense":[]}
    
    def __init__(self, name, income):
        super().__init__(name, income)
    
    def food(self,expense):
        if 0 < expense and expense <= self._User__income:
            self._User__income -= expense
            self.hist["Food"].append(f"Transaction Competed {expense}")
        else:
            print("Your Balance is over")

    def Enternainment(self,expense):
        if 0 < expense and expense <= self._User__income:
            self._User__income -= expense
            self.hist["Enterntainment"].append(f"Transaction Competed {expense}")
        else:
            print("Your Balance is over")

    def Daily(self,expense):
        if 0 < expense and expense <= self._User__income:
            self._User__income -= expense
            self.hist["Daily Expense"].append(f"Transaction Competed {expense}")
        else:
            print("Your Balance is over")
        
    def History(self):
        print(self.hist)
    
    def Balanace(self):
        print(self._User__income)


U1=Expense("Krushna",50000)

U1.food(10000)
U1.Enternainment(5000)
U1.Daily(20000)
U1.History()
U1.Balanace()