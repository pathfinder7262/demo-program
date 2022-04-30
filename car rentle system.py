#take inpute car or bike
#first show the custmore availbale bikes and car and quantity
#take a inpute for quantity of a bike or car and tell then the charges/hr or /day againest them and entry the cust in db
#update the car or bike quantity 
#when cust return the bike then create recipt

import datetime

class rent():
    def __init__(self):
        print("Welcome to Chetan Car and Bike Rentle store")
        self.car = 100
        self.bile = 100
        self.bike_crg_pr_hr = 100
        self.bike_crg_pr_day = 1000
        self.car_crg_pr_hr = 200
        self.car_crg_pr_day = 2000

    def showqunt(self):
        print("Total Number of quantity of Bike for rent: ",self.bile)
        print("Total Number of quantity of car for rent: ",self.car)

    def cust():
        nm = input("Enter the Name OF Customer: ")
        opt = input("Enter the option for car or Bike(c/b): ")
        