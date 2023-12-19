from dao.managementClass import *


print(" WELCOME TO CAR RENTAL SYSTEM ")
while(True):
    print("\n select 1 to ADD CUSTOMER")
    print(" 2 to UPDATE CUSTOMER INFORMATION")
    print(" 3 to FIND A CUSTOMER")
    print(" 4 to LIST CUSTOMERS")
    print(" 5 to REMOVE CUSTOMER")
    print(" 6 to ADD CAR")
    print(" 7 to REMOVE CAR")
    print(" 8 to LIST AVAILABLE CARS")
    print(" 9 to LIST RENTED CARS")
    print(" 10 to UPDATE CAR AVAILABILITY")
    print(" 11 to FIND A CAR")
    print(" 12 to UPDATE LEASE")
    print(" 13 to FIND TOTAL COST BASED ON TYPE")
    print(" 14 to CREATE LEASE")
    print(" 15 to FIND CAR BASED ON LEASE")
    print(" 16 to LIST ACTIVE LEASES")
    print(" 17 to LIST LEASE HISTORY")
    print(" 18 to RECORD PAYMENT")
    print(" 19 to PAYMENT HISTORY OF A CUSTOMER")
    print(" 20 to FIND TOTAL REVENUE")
    print(" 21 to EXIT")
    s = input("Enter your choice : ")
    if s == '1':
        try:
            customer.addCustomer()
        except Exception as e:
            print(str(s))
    elif s == '2':
        try:
            customer.updateCustomerInformation()
        except Exception as e:
            print(str(s))
    elif s == '3':
        try:
            customer.findCustomerById()
        except Exception as e:
            print(str(s))
    elif s == '4':
        try:
            customer.listCustomers()
        except Exception as e:
            print(str(s))
    elif s == '5':
        try:
            customer.removeCustomer()
        except Exception as e:
            print(str(s))
    elif s == '6':
        try:
            car.addCar()
        except Exception as e:
            print(str(s))
    elif s == '7':
        try:
            car.removeCar()
        except Exception as e:
            print(str(s))
    elif s == '8':
        try:
            car.listAvailableCars()
        except Exception as e:
            print(str(s))
    elif s == '9':
        try:
            car.listRentedCars()
        except Exception as e:
            print(str(s))
    elif s == '10':
        try:
            car.updateCarAvailability()
        except Exception as e:
            print(str(s))
    elif s == '11':
        try:
            car.findCarById()
        except Exception as e:
            print(str(s))
    elif s == '12':
        try:
            l.updateLease()
        except Exception as e:
            print(str(s))
    elif s == '13':
        try:
            l.totalCostBasedOnType()
        except Exception as e:
            print(str(s))
    elif s == '14':
        try:
            l.createLease()
        except Exception as e:
            print(str(s))
    elif s == '15':
        try:
            print(l.returnCar())
        except Exception as e:
            print(str(s))
    elif s == '16':
        try:
            l.listActiveLeases()
        except Exception as e:
            print(str(s))
    elif s == '17':
        try:
            l.listLeaseHistory()
        except Exception as e:
            print(str(s))
    elif s == '18':
        try:
            p.recordPayment()
        except Exception as e:
            print(str(s))
    elif s == '19':
        try:
            p.paymentHistory()
        except Exception as e:
            print(str(s))
    elif s == '20':
        try:
            p.totalRevenue()
        except Exception as e:
            print(str(s))
    elif s == '21':
        print("*" * 30 + " THANK YOU FOR USING CAR RENTAL SYSTEM " + "*" * 30)
        break
    else:
        print("Invalid choice")