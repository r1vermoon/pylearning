import unittest
from test15 import formatted_name

class NameTestCase(unittest.TestCase):
    
    def test_name(self):
        full=formatted_name("xy","m")
        self.assertEqual(full,"xym")

    def test_name2(self):
        full=formatted_name("y","m","x")
        self.assertEqual(full,"yxm")
unittest.main()

print("Enter your name,enter 'q' to exist.")
while True:
    first_name=input("give me a first name:")
    if first_name=='q':
        break
    last_name=input("give me a last name:")
    if last_name=='q':
        break

    full=formatted_name(first_name,last_name)
    print(full)