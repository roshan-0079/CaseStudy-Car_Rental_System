import mysql.connector as sql


class DbConnUtil:
    # THIS FUNCTION WILL GET THE CONNECTION
    def getConnection(self):
        try:
            self.conn = sql.connect(host='localhost', database='car_rental', user='root', password='Shaik@123')
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(str(e) + '---DATABASE NOT FOUND---')

    # THIS FUNCTION CLOSES THE CONNECTION
    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print(str(e))

    # THIS FUNCTION WILL EXECUTE A QUERY TAKING QUERY AS INPUT
    def execute(self, query):
        self.getConnection()
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(query)
        except Exception as e:
            print(str(e) + '---INVALID DATA---')
        else:
            self.conn.commit()
        finally:
            self.close()

    # THIS FUNCTION WILL TAKE QUERY AND DATA AS INPUT AND PERFORMS EXECUTEMANY OPERATION
    def execute_many(self, query, data):
        self.getConnection()
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(query, data)
        except Exception as e:
            print(str(e) + '---INVALID DATA---')
        else:
            self.conn.commit()
        finally:
            self.close()

    # THIS METHOD IS USED TO EXECUTE QUERY AND ALSO RETURN THE FETCHED DATA
    def execute_return(self, query):
        self.getConnection()
        self.stmt = self.conn.cursor()
        self.stmt.execute(query)
        data = self.stmt.fetchall()
        self.close()
        return data
