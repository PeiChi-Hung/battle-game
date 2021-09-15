"""
Testing file for Question 3 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from unittest import mock

class TestTask3(unittest.TestCase):
    SINGLE = False

    def setUp(self):
        self.verificationErrors = []
        self.MaxDiff = None

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    ## 2021-04-21 - Removed residual '@mock.patch' tests.

    def test__correct_army_given(self):
        t1 = Army()

        # Test if a (low) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(1,1,1), msg = "Stack test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # put your __correct_army tests here
        try:
            self.assertFalse(t1._Army__correct_army_given(0,0,11), msg = "Stack test 0,0,11 should fail")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(t1._Army__correct_army_given(10,10,0), msg = "Stack test 10,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        
        try:
            self.assertFalse(t1._Army__correct_army_given(10,20,0), msg = "Stack test 10,20,0 should fail")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        

    def test__str__(self):
        sold = "Soldier's life = 3 and experience = 0"
        arch = "Archer's life = 3 and experience = 0"
        cav = "Cavalry's life = 4 and experience = 0"
        t1 = Army()

        # Test if the string representation of the army matches expected output for low unit values
        t1._Army__assign_army("t1",1,1,1,0)
        try:
            self.assertEqual(str(t1.force),sold+","+arch+","+cav, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # put your __str__ tests here
        t1._Army__assign_army("t1",2,1,1,0)
        try:
            self.assertEqual(str(t1.force),sold+","+sold+","+arch+","+cav, msg = "String test 2,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        t1._Army__assign_army("t1",0,1,1,0)
        try:
            self.assertEqual(str(t1.force),arch+","+cav, msg = "String test 0,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        
        t1._Army__assign_army("t1",0,0,2,0)
        try:
            self.assertEqual(str(t1.force),cav +","+ cav, msg = "String test 0,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)

