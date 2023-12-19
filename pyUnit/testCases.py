import unittest
from dao.managementClass import *


class MyTestCase(unittest.TestCase):
    # FIRST TEST CASE - TO TEST CAR CREATED SUCCESSFULLY OR NOT
    def testCase1(self):
        data1 = car.insert()
        data2 = car.select()
        for i in data2:
            if i[0] == data1[0][0]:
                self.assertEqual(True, True)
                break
        else:
            self.assertEqual(True, False)

    # SECOND TEST CASE - TO TEST LEASE CREATED SUCCESSFULLY OR NOT
    def testCase2(self):
        data1 = l.insert()
        data2 = l.select()
        for i in data2:
            if i[0] == data1[0][0]:
                self.assertEqual(True, True)
                break
        else:
            self.assertEqual(True, False)

    # THIRD TEST CASE - TO TEST LEASE IS RETRIEVED SUCCESSFULLY OR NOT
    def testCase3(self):
        print("ENTER VALID CAR ID EXAMPLE - 1")
        data1 = l.returnCar()
        data2 = l.select()
        for i in data2:
            if data2[0] == data1:
                self.assertEqual(True, True)
                break
        else:
            self.assertEqual(True, False)

    # FOURTH TEST CASE - TO CHECK IF EXCEPTION IS THROWN CORRECTLY OR NOT
    def testCase4(self):
        print('ENTER INVALID ID LIKE CAR ID - 45678, CUSTOMER ID - 9876, LEASE ID - 123456789')
        self.assertEqual("INVALID CAR ID/ CAR ID DOES NOT EXIST IN DATABASE", str(car.findCarById()))
        self.assertEqual("INVALID CUSTOMER ID/ CUSTOMER ID DOES NOT EXIST IN DATABASE",
                         str(customer.findCustomerById()))
        self.assertEqual("INVALID LEASE ID/ LEASE ID DOES NOT EXIST IN DATABASE", str(l.returnCar()))


if __name__ == '__main__':
    unittest.main()
