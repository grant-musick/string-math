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

    def __add__(self, other):
        return StringNumber.__add(self, other)

    def __sub__(self, other):
        comp = StringNumber.__compare(self, other)
        if comp == 1:
            return StringNumber.__subtract(self, other, False)
        elif comp == -1:
            return StringNumber.__subtract(other, self, True)
        else:
            return StringNumber("0")

    def __cmp__(self, other):
        if len(self) > len(other):
            return 1
        elif len(self) < len(other):
            return -1
        else:
            for x in zip(self.value, other.value):
                f = int(x[0])
                s = int(x[1])
                if f > s:
                    return 1
                elif f < s:
                    return -1
            else:
                return 0 # they are equal


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
    def __add(first, second):
        rev_first = first.value.zfill(len(second))[::-1]
        rev_second = second.value.zfill(len(first))[::-1]

        answer_coll = []
        add_one_to_next = False;

        for x in range(len(rev_first)):
            f = int(rev_first[x])
            s = int(rev_second[x])
            if add_one_to_next:
                f = f + 1
            
            tot = f + s
            if tot > 10:
                add_one_to_next = True
                tot = tot - 10
            else:
                add_one_to_next = False

            answer_coll.append(tot)

        if add_one_to_next:
            answer_coll.append("1")

        answer_arr = [str(x) for x in answer_coll]
        answer_str = "".join(answer_arr)
        answer_str = answer_str[::-1].lstrip('0')
        if not answer_str: answer_str = '0'

        return StringNumber(str(answer_str))








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

