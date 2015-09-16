#!/usr/bin/python
# coding: utf-8

import unittest

class StringNumber:
    def __init__(self, str_number):
        if str_number:
            if str_number.startswith("-"):
                self.value = str_number[1:]
                self.negative = True
            else:
                self.value = str_number
                self.negative = False

            if not self.value.isdigit():
                raise ValueError("Invalid string number {0}".format(str_number))
        else:
            raise ValueError("None not allowed")

    def __repr__(self):
        if self.negative:
            return "-" + self.value
        else:
            return self.value

    def __sub__(self, other):
        comp = StringNumber.__compare(self, other)
        if comp == 1:
            return StringNumber.__subtract(self, other, False)
        elif comp == -1:
            return StringNumber.__subtract(other, self, True)
        else:
            return StringNumber("0")

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __len__(self):
        return len(self.value)

    @staticmethod
    def __compare(first, second):
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        else:
            for x in zip(first.value, second.value):
                f = int(x[0])
                s = int(x[1])
                if f > s:
                    return 1
                elif f < s:
                    return -1
            else:
                return 0 # they are equal



    @staticmethod
    def __subtract(minuend, subtrahend, sign_flip=False):
        """ Assuming we already know the minuend is a numeric value
        greater than the subtrahend
        """
        # Using Austrian method
        rev_minu = minuend.value[::-1]
        rev_subt = subtrahend.value.zfill(len(rev_minu))[::-1]

        answer_coll = []
        add_one_to_next = False
        for x in range(len(rev_subt)):
            m = int(rev_minu[x])
            s = int(rev_subt[x])
            if add_one_to_next:
                s = s + 1

            if s > m:
                add_one_to_next = True
                answer_coll.append(m + 10 - s)
            else:
                add_one_to_next = False
                answer_coll.append(m - s)

        answer_arr = [str(x) for x in answer_coll]
        answer_str = "".join(answer_arr)
        answer_str = answer_str[::-1].lstrip('0')
        if not answer_str: answer_str = '0'
        if sign_flip:
            answer_str = "-" + answer_str
        return StringNumber(answer_str)






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

    @unittest.skip("Out of scope for naive problem")
    def test_pos_neg_pos_subtraction(self):
        number = StringNumber("40") - StringNumber("-20")
        self.assertEqual("60", str(number))

    def test_pos_pos_neg_subraction(self):
        number = StringNumber("40") - StringNumber("100")
        self.assertEqual("-60", str(number))

    def test_pos_zero_pos_subtraction(self):
        number = StringNumber("40") - StringNumber("0")
        self.assertEqual("40", str(number))

    @unittest.skip("Out of scope for naive problem")
    def test_neg_pos_neg_subtraction(self):
        number = StringNumber("-40") - StringNumber("20")
        self.assertEqual("-60", str(number))

    @unittest.skip("Out of scope for naive problem")
    def test_neg_neg_neg_subtraction(self):
        number = StringNumber("-40") - StringNumber("-20")
        self.assertEqual("-20", str(number))

    @unittest.skip("Out of scope for naive problem")
    def test_neg_neg_zero_subtraction(self):
        number = StringNumber("-40") - StringNumber("-40")
        self.assertEqual("0", str(number))

    @unittest.skip("Out of scope for naive problem")
    def test_neg_neg_pos_subtraction(self):
        number = StringNumber("-40") - StringNumber("-60")
        self.assertEqual("20", str(number))

    @unittest.skip("Out of scope for naive problem")
    def test_neg_zero_neg_subtraction(self):
        number = StringNumber("-40") - StringNumber("0")
        self.assertEqual("-40", str(number))

    def test_zero_zero_zero_subtraction(self):
        number = StringNumber("0") - StringNumber("0")
        self.assertEqual("0", str(number))






if __name__ == "__main__":
    a = StringNumber("1")
    b = StringNumber("2")
    c = StringNumber("123")
    d = StringNumber("74")

    formatable_str = "{0} - {1} = {2}"

    print formatable_str.format(a, b, a - b)
    print formatable_str.format(b, a, b - a)
    print formatable_str.format(a, a, a - a)
    print formatable_str.format(c, d, c - d)
    print formatable_str.format(d, c, d - c)

