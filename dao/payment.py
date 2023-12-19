from util.dbPropertyUtil import DbConnUtil


# PAYMENT CLASS
class Payment(DbConnUtil):
    # CREATE METHOD TO CREATE THE TABLE
    def create(self):
        query = '''CREATE TABLE IF NOT EXISTS PAYMENT(
                    PAYMENTID INT PRIMARY KEY,
                    LEASEID INT, FOREIGN KEY(LEASEID) REFERENCES LEASE(LEASEID) ON DELETE CASCADE,
                    PAYMENTDATE DATE,
                    AMOUNT INT)'''
        self.execute(query)

    # INSERT METHOD TO INSERT A RECORD INTO THE TABLE
    def insert(self):
        paymentID = int(input("Enter payment ID : "))
        leaseID = int(input("Enter lease id : "))
        paymentDate = input("Enter payment date(YYYY-MM-DD) : ")
        amount = int(input("Enter amount : "))
        query = f'''INSERT INTO PAYMENT VALUES({paymentID},{leaseID},'{paymentDate}',{amount})'''
        try:
            self.execute(query)
        except Exception as e:
            print(str(e)+'---PAYMENT ID EXISTS---')

    # SELECT METHOD TO FETCH THE RECORDS FROM THE TABLE
    def select(self):
        query = '''SELECT * FROM PAYMENT'''
        data = self.execute_return(query)
        return data

    # UPDATE METHOD TO UPDATE THE RECORDS IN THE TABLE
    def update(self):
        paymentID = int(input("Enter payment ID : "))
        leaseID = int(input("Enter lease id : "))
        paymentDate = input("Enter payment date(YYYY-MM-DD) : ")
        amount = int(input("Enter amount : "))
        data=[(leaseID, paymentDate, amount, paymentID)]
        query = f'''UPDATE PAYMENT SET LEASEID=%s,PAYMENTDATE=%s,AMOUNT=%s
                WHERE PAYMENTID =%s'''
        self.execute_many(query, data)

    # DELETE METHOD TO DELETE THE RECORDS FROM THE TABLE
    def delete(self):
        paymentID = int(input("Enter Payment ID to delete the record : "))
        query = f'''DELETE FROM PAYMENT WHERE PAYMENTID={paymentID}'''
        self.execute(query)
