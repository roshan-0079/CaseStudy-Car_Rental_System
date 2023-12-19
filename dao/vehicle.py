from util.dbPropertyUtil import DbConnUtil


# VEHICLE CLASS
class Vehicle(DbConnUtil):
    # METHOD TO CREATE VEHICLE TABLE
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS VEHICLE(VEHICLEID INT PRIMARY KEY,MAKE VARCHAR(50),MODEL VARCHAR(50),
                    YEAR INT,DAILYRATE INT,STATUS INT,PASSENGERCAPACITY INT,ENGINECAPACITY INT)'''
        self.execute(query)

    # METHOD TO INSERT DATA INTO VEHICLE TABLE
    def insert(self):
        vehicleID = int(input("Enter vehicle ID : "))
        make = input("Enter make : ")
        model = input("Enter model : ")
        year = int(input("Enter year : "))
        dailyRate = int(input("Enter daily rate : "))
        status = int(input("Enter 0 if not available and 1 if available : "))
        passengerCapacity = int(input("Enter passenger capacity : "))
        engineCapacity = int(input("Enter engine capacity : "))
        query = f'''INSERT INTO VEHICLE VALUES({vehicleID},'{make}','{model}',{year},{dailyRate},{status},
                    {passengerCapacity},{engineCapacity})'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e)+'---VEHICLE ID EXISTS---')
        else:
            return([(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)])

    # SELECT METHOD TO FETCH THE RECORDS
    def select(self):
        query = '''SELECT * FROM VEHICLE'''
        data = self.execute_return(query)
        return data

    # METHOD TO UPDATE THE DATA
    def update(self):
        vehicleID = int(input("Enter vehicle ID : "))
        make = input("Enter make : ")
        model = input("Enter model : ")
        year = int(input("Enter year : "))
        dailyRate = int(input("Enter daily rate : "))
        status = int(input("Enter 0 if not available and 1 if available : "))
        passengerCapacity = int(input("Enter passenger capacity : "))
        engineCapacity = int(input("Enter engine capacity : "))
        data=[(make, model, year, dailyRate, status, passengerCapacity, engineCapacity, vehicleID)]
        query = f'''UPDATE VEHICLE SET MAKE=%s,MODEL=%s,YEAR=%s,DAILYRATE=%s,
                STATUS=%s,PASSENGERCAPACITY=%s,ENGINECAPACITY=%s
                WHERE VEHICLEID =%s'''
        self.execute_many(query, data)

    # METHOD TO DELETE THE DATA
    def delete(self):
        vehicleID = int(input("Enter Vehicle ID to delete the record : "))
        query = f'''DELETE FROM VEHICLE WHERE VEHICLEID={vehicleID}'''
        self.execute(query)