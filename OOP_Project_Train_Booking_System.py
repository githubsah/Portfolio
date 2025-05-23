class Train: 
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        
    def book_ticket(self):
        if self.seats > 0:
             self.seats -= 1
             print(f"\nThe Ticket has been booked successfully!!!!! Seats left : {self.seats}\n")
        else:
            print("\nThe Train is Full!!  Sorry the ticket cannot be booked.\n")
            
    def show_status(self):
        print(f"\nThe number of seats left in the train {self.name} is : {self.seats} \n")
        
    def fare_info(self):
        print(f"The fare is : ₹{self.fare}")
        
    @staticmethod
    def greet():
        print("Welcome to Indian Railways!!!!")
        

class PremiumTrain(Train)      :
    def __init__(self,name,seats,fare,menu):
        super().__init__(name,seats,fare)
        self.menu = menu
    
    def show_menu(self):
        print("\nToday's Menu : \n")
        for m in self.menu:
            print("-",m)
            
Train.greet()
rajdhani = Train("Rajdhani Express",2,1500)
rajdhani.show_status()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.show_status()
rajdhani.fare_info()

print("\n--- Shatabdi Express Booking (Premium Train) ---")
shatabdi = PremiumTrain("Shatabdi Express",1,2000,["Paneer","Dal","Roti","Ice-Cream"])
shatabdi.show_status()
shatabdi.book_ticket()
shatabdi.book_ticket()
shatabdi.show_status()
shatabdi.show_menu()
shatabdi.fare_info()

