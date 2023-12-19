# CUSTOM EXCEPTIONS

# WHEN A CAR IS NOT FOUND THEN THIS EXCEPTION WILL RAISE
class CarNotFoundException(Exception):
    def __init__(self, msg = "INVALID CAR ID/ CAR ID DOES NOT EXIST IN DATABASE"):
        super().__init__(msg)


# WHEN A LEASE IS NOT FOUND THEN THIS EXCEPTION WILL RAISE
class LeaseNotFoundException(Exception):
    def __init__(self, msg = "INVALID LEASE ID/ LEASE ID DOES NOT EXIST IN DATABASE"):
        super().__init__(msg)


# WHEN A CUSTOMER IS NOT FOUND THEN THIS EXCEPTION WILL RAISE
class CustomerNotFoundException(Exception):
    def __init__(self, msg = "INVALID CUSTOMER ID/ CUSTOMER ID DOES NOT EXIST IN DATABASE"):
        super().__init__(msg)
