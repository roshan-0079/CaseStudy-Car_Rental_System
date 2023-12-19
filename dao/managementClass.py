from exception.exception import *
from dao.vehicle import Vehicle
from dao.payment import Payment
from dao.customer import Customer
from dao.lease import Lease


# CUSTOMER MANAGEMENT
class CustomerManagement(Customer):
    # FUNCTION TO ADD A CUSTOMER
    def addCustomer(self):
        self.insert()

    # FUNCTION TO UPDATE CUSTOMER INFORMATION
    def updateCustomerInformation(self):
        self.update()

    # THIS METHOD WILL GET A PARTICULAR CUSTOMER RECORD
    def findCustomerById(self):
        id = int(input("Enter customer ID : "))
        data = self.select()
        try:
            for i in data:
                if i[0] == id:
                    print(i)
                    break
            else:
                raise CustomerNotFoundException
        except CustomerNotFoundException as e:
            print(e)
            return(e)

    # THIS METHOD WILL LIST ALL THE CUSTOMERS
    def listCustomers(self):
        data = self.select()
        for i in data:
            print(i)

    # THIS CUSTOMER WILL REMOVE A CUSTOMER FROM THE DATABASE
    def removeCustomer(self):
        self.delete()


# CAR MANAGEMENT
class CarManagement(Vehicle):
    # THIS METHOD WILL ADD A CAR IN THE DATA
    def addCar(self):
        self.insert()

    # THIS METHOD WILL REMOVE A CAR FROM THE DATA
    def removeCar(self):
        self.delete()

    # THIS METHOD WILL LIST ALL THE AVAILABLE CARS IN THE DATA
    def listAvailableCars(self):
        data = self.select()
        for i in data:
            if i[5] == 1:
                print(i)

    # THIS METHOD WILL SHOW ALL THE CARS THAT ARE RENTED
    def listRentedCars(self):
        data = self.select()
        for i in data:
            if i[5] == 0:
                print(i)

    # THIS METHOD IS USED TO CHANGE THE STATUS OF A CAR
    def updateCarAvailability(self):
        self.update()

    # THIS METHOD WILL GET A PARTICULAR CAR RECORD
    def findCarById(self):
        id = int(input("Enter Vehicle ID : "))
        data = self.select()
        try:
            for i in data:
                if i[0] == id:
                    print(i)
                    break
            else:
                raise CarNotFoundException
        except CarNotFoundException as e:
            print(e)
            return(e)


# LEASE MANAGEMENT
class LeaseManagement(Lease):
    # THIS METHOD WILL UPDATE A LEASE RECORD
    def updateLease(self):
        self.update()

    # THIS METHOD WILL GIVE TOTAL COST BASED ON TYPE OF LEASE - DAILY/MONTHLY
    def totalCostBasedOnType(self):
        query = '''SELECT L.TYPE, SUM(P.AMOUNT) FROM LEASE AS L 
                    INNER JOIN PAYMENT AS P ON P.LEASEID = L.LEASEID
                    GROUP BY L.TYPE'''
        data = self.execute_return(query)
        print(data)

    # THIS METHOD WILL CREATE A NEW LEASE
    def createLease(self):
        self.insert()

    # THIS METHOD WILL RETURN A PARTICULAR LEASE RECORD
    def returnCar(self):
        leaseID = int(input("Enter lease ID : "))
        data = self.select()
        for i in data:
            if i[0] == leaseID:
                return(i)
        else:
            try:
                raise LeaseNotFoundException
            except LeaseNotFoundException as e:
                print(e)
                return(e)

    # THIS METHOD WILL SHOW ALL THE ACTIVE LEASES
    def listActiveLeases(self):
        data = self.select()
        for i in data:
            if i[4] == None:
                print(i)

    # THIS METHOD WILL LIST THE LEASE HISTORY
    def listLeaseHistory(self):
        data = self.select()
        for i in data:
            print(i)


# PAYMENT HANDLING
class PaymentHandling(Payment):
    # THIS METHOD WILL RECORD A PAYMENT
    def recordPayment(self):
        self.insert()

    # THIS METHOD WILL SHOW PAYMENT HISTORY OF A PARTICULAR CUSTOMER
    def paymentHistory(self):
        id = int(input("Enter customer ID : "))
        query = f'''SELECT L.CUSTOMERID, PAYMENTID, PAYMENTDATE, AMOUNT FROM LEASE AS L 
                    INNER JOIN PAYMENT AS P ON P.LEASEID = L.LEASEID 
                    WHERE L.CUSTOMERID = {id}'''
        data = self.execute_return(query)
        for i in data:
            print(i)

    # THIS METHOD WILL SHOW THE TOTAL REVENUE
    def totalRevenue(self):
        query = '''SELECT SUM(AMOUNT) FROM PAYMENT'''
        data = self.execute_return(query)
        print(data)


customer = CustomerManagement()
car = CarManagement()
l = LeaseManagement()
p = PaymentHandling()
