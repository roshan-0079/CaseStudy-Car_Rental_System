from util.dbPropertyUtil import DbConnUtil


# CUSTOMER CLASS
class Customer(DbConnUtil):
    # CREATE FUNCTION TO CREATE THE CUSTOMER TABLE
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS CUSTOMER(
                    CUSTOMERID INT PRIMARY KEY,
                    FIRST_NAME VARCHAR(50),
                    LAST_NAME VARCHAR(50),
                    EMAIL VARCHAR(50),
                    PHONE_NUMBER VARCHAR(50))'''
        self.execute(query)

    # INSERT FUNCTION TO INSERT NEW RECORDS
    def insert(self):
        customerID = int(input("Enter customer ID : "))
        firstName = input("Enter firstName : ")
        lastName = input("Enter lastName : ")
        email = input("Enter email : ")
        phoneNumber = input("Enter phone number : ")
        query = f'''INSERT INTO CUSTOMER VALUES({customerID},'{firstName}','{lastName}','{email}','{phoneNumber}')'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e)+'---CUSTOMER ID EXISTS---')
        else:
            return([(customerID, firstName, lastName, email, phoneNumber)])

    # SELECT FUNCTION TO FETCH RECORDS
    def select(self):
        query = '''SELECT * FROM CUSTOMER'''
        data = self.execute_return(query)
        return data

    # UPDATE FUNCTION TO UPDATE THE RECORDS
    def update(self):
        customerID = int(input("Enter customer ID : "))
        firstName = input("Enter firstName : ")
        lastName = input("Enter lastName : ")
        email = input("Enter email : ")
        phoneNumber = input("Enter phone number : ")
        data=[(firstName, lastName, email, phoneNumber, customerID)]
        query = f'''UPDATE CUSTOMER SET FIRSTNAME=%s,LASTNAME=%s,EMAIL=%s,PHONENUMBER=%s
                WHERE CUSTOMERID =%s'''
        self.execute_many(query, data)

    # DELETE FUNCTIONS TO DELETE THE RECORDS
    def delete(self):
        customerID = int(input("Enter Customer ID to delete the record : "))
        query = f'''DELETE FROM CUSTOMER WHERE CUSTOMERID={customerID}'''
        self.execute(query)
