#!/usr/bin/python
# coding: utf-8

import unittest
import operator
from string_subtraction import StringNumber




# There are other ways to do this but thought it would be fun working out
# the problems of a class with dynamically created methods
class StringNumberEqualityTests(unittest.TestCase):
    """Shell class for dyanmically generated tests"""
    pass

    @classmethod
    def initialize_equality_tests(cls):
        zero = StringNumber("0")
        pos1 = StringNumber("1230")
        pos2 = StringNumber("456")
        neg1 = StringNumber("-345")
        neg2 = StringNumber("-11234")


        test_items = [
                    (zero, zero, operator.eq, True),
                    (zero, zero, operator.lt, False),
                    (zero, zero, operator.le, True),
                    (zero, zero, operator.gt, False),
                    (zero, zero, operator.ge, True),
                    (zero, zero, operator.ne, False),

                    (pos1, pos2, operator.eq, False),
                    (pos1, pos2, operator.lt, False),
                    (pos1, pos2, operator.le, False),
                    (pos1, pos2, operator.gt, True),
                    (pos1, pos2, operator.ge, True),
                    (pos1, pos2, operator.ne, True),
                    
                    (pos2, pos1, operator.eq, False),
                    (pos2, pos1, operator.lt, True),
                    (pos2, pos1, operator.le, True),
                    (pos2, pos1, operator.gt, False),
                    (pos2, pos1, operator.ge, False),
                    (pos2, pos1, operator.ne, True),

                    (pos1, neg1, operator.eq, False),
                    (pos1, neg1, operator.lt, False),
                    (pos1, neg1, operator.le, False),
                    (pos1, neg1, operator.gt, True),
                    (pos1, neg1, operator.ge, True),
                    (pos1, neg1, operator.ne, True),

                    (neg1, pos1, operator.eq, False),
                    (neg1, pos1, operator.lt, True),
                    (neg1, pos1, operator.le, True),
                    (neg1, pos1, operator.gt, False),
                    (neg1, pos1, operator.ge, False),
                    (neg1, pos1, operator.ne, True),

                    (neg1, neg2, operator.eq, False),
                    (neg1, neg2, operator.lt, False),
                    (neg1, neg2, operator.le, False),
                    (neg1, neg2, operator.gt, True),
                    (neg1, neg2, operator.ge, True),
                    (neg1, neg2, operator.ne, True),

                    (neg2, neg1, operator.eq, False),
                    (neg2, neg1, operator.lt, True),
                    (neg2, neg1, operator.le, True),
                    (neg2, neg1, operator.gt, False),
                    (neg2, neg1, operator.ge, False),
                    (neg2, neg1, operator.ne, True),

                    ]


        def my_generator(x, y, op, answer):
                def test(self):
                    self.assertEqual(op(x,y), answer, 
                        "{0} {1} {2} not {3}".format(x, op, y, answer))
                return test


        operator_nice_names = {
            operator.eq : "equals",
            operator.lt : "less than",
            operator.le : "less than or equal",
            operator.gt : "greater than",
            operator.ge : "greater than or equal",
            operator.ne : "not equal to"
        }

        for x, y, op, answer in test_items:
            test_name = "test_{0}_{2}_{1}_{3}".format(x, y,
                operator_nice_names[op].replace(" ", "_"),
                answer
                )
            test = my_generator(x, y, op, answer)
            setattr(StringNumberEqualityTests, test_name, test)


# Dynamically assign test methods to class on import
StringNumberEqualityTests.initialize_equality_tests()



class StringNumberTests(unittest.TestCase):

    def test_pos_short_number_construction(self):
        number = StringNumber("1")
        self.assertEqual("1", str(number))

    def test_neg_short_number_construction(self):
        number = StringNumber("-1")
        self.assertEqual("-1", str(number))

    def test_pos_number_construction(self):
        number = StringNumber("123")
        self.assertEqual("123", str(number))

    def test_neg_number_construction(self):
        number = StringNumber("-123")
        self.assertEqual("-123", str(number))

    def test_zero_number_construction(self):
        number = StringNumber("0")
        self.assertEqual("0", str(number))

    def test_neg_zero_number_construction(self):
        number = StringNumber("-0")
        self.assertEqual("-0", str(number))

    def test_bad_string_construction(self):
        with self.assertRaises(ValueError):
            StringNumber("12b")

    def test_empty_string_construction(self):
        with self.assertRaises(ValueError):
            StringNumber("12b")

    def test_none_construction(self):
        with self.assertRaises(ValueError):
            StringNumber(None)

    def test_pos_pos_pos_subtraction(self):
        number = StringNumber("40") - StringNumber("20")
        self.assertEqual("20", str(number))

    def test_pos_pos_zero_subtraction(self):
        number = StringNumber("40") - StringNumber("40")
        self.assertEqual("0", str(number))

    def test_pos_neg_pos_subtraction(self):
        number = StringNumber("40") - StringNumber("-20")
        self.assertEqual("60", str(number))

    def test_pos_pos_neg_subraction(self):
        number = StringNumber("40") - StringNumber("100")
        self.assertEqual("-60", str(number))

    def test_pos_zero_pos_subtraction(self):
        number = StringNumber("40") - StringNumber("0")
        self.assertEqual("40", str(number))

    def test_neg_pos_neg_subtraction(self):
        number = StringNumber("-40") - StringNumber("20")
        self.assertEqual("-60", str(number))

    def test_neg_neg_neg_subtraction(self):
#        import pdb
#        pdb.set_trace()
        number = StringNumber("-40") - StringNumber("-20")
        self.assertEqual("-20", str(number))

    def test_neg_neg_zero_subtraction(self):
        number = StringNumber("-40") - StringNumber("-40")
        self.assertEqual("0", str(number))

    def test_neg_neg_pos_subtraction(self):
        number = StringNumber("-40") - StringNumber("-60")
        self.assertEqual("20", str(number))

    def test_neg_zero_neg_subtraction(self):
        number = StringNumber("-40") - StringNumber("0")
        self.assertEqual("-40", str(number))

    def test_zero_zero_zero_subtraction(self):
        number = StringNumber("0") - StringNumber("0")
        self.assertEqual("0", str(number))

    def test_basic_addition(self):
        number = StringNumber("1") + StringNumber("2")
        self.assertEqual("3", str(number))

    def test_carryover(self):
        number = StringNumber("7") + StringNumber("8")
        self.assertEqual("15", str(number))

    def test_diff_length_numbers(self):
        number = StringNumber("4") + StringNumber("20")
        self.assertEqual("24", str(number))

    def test_zero_plus_one_addition(self):
        number = StringNumber("0") + StringNumber("1")
        self.assertEqual("1", str(number))

    def test_zero_addition(self):
        number = StringNumber("0") + StringNumber("0")
        self.assertEqual("0", str(number))



if __name__ == "__main__":
    unittest.main()
