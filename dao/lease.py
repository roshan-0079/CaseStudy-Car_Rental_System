from util.dbPropertyUtil import DbConnUtil


# LEASE CLASS
class Lease(DbConnUtil):
    # CREATE METHOD TO CREATE THE TABLE
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS LEASE(
                    LEASEID INT PRIMARY KEY,
                    VEHICLEID INT, FOREIGN KEY(VEHICLEID) REFERENCES VEHICLE(VEHICLEID) ON DELETE CASCADE,
                    CUSTOMERID INT, FOREIGN KEY(CUSTOMERID) REFERENCES CUSTOMER(CUSTOMERID) ON DELETE CASCADE,
                    STARTDATE DATE,
                    ENDDATE DATE,
                    TYPE VARCHAR(50))'''
        self.execute(query)

    # INSERT METHOD TO INSERT DATA INTO THE TABLE
    def insert(self):
        leaseID = int(input("Enter lease ID : "))
        vehicleID = int(input("Enter vehicle id : "))
        customerID = int(input("Enter customer id : "))
        startDate = input("Enter start date(YYYY-MM-DD) : ")
        endDate = input("Enter end date(YYYY-MM--DD) : ")
        type = input("Enter the type(DAILY/MONTHLY) : ")
        query = f'''INSERT INTO LEASE VALUES({leaseID},{vehicleID},{customerID},'{startDate}','{endDate}','{type}')'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e)+'---LEASE ID EXISTS---')
        else:
            return [(leaseID, vehicleID, customerID, startDate, endDate, type)]

    # SELECT METHOD TO FETCH THE RECORDS
    def select(self):
        query = '''SELECT * FROM LEASE'''
        data = self.execute_return(query)
        return data

    # UPDATE METHOD TO UPDATE THE RECORDS
    def update(self):
        leaseID = int(input("Enter lease ID : "))
        vehicleID = input("Enter vehicle id : ")
        customerID = input("Enter customer id : ")
        startDate = input("Enter start date(YYYY-MM-DD) : ")
        endDate = input("Enter end date(YYYY-MM--DD) : ")
        type = input("Enter the type(DAILY/MONTHLY) : ")
        data=[(vehicleID, customerID, startDate, endDate, type, leaseID)]
        query = f'''UPDATE LEASE SET VEHICLEID=%s,CUSTOMERID=%s,STARTDATE=%s,ENDDATE=%s,TYPE=%s
                WHERE LEASEID =%s'''
        self.execute_many(query, data)

    # DELETE METHOD TO DELETE THE RECORDS
    def delete(self):
        leaseID = int(input("Enter Lease ID to delete the record : "))
        query = f'''DELETE FROM LEASE WHERE LEASEID={leaseID}'''
        self.execute(query)