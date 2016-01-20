#!/usr/bin/python
# coding: utf-8


# The math for these can be broken down into a matrix 
# based on the negative/postive value of each operand
# 
# operator and sign and sign => operation
# + and +x and +y => add(x,y)
# + and -x and +y => sub(y,x)
# + and +x and -y => sub(x,y)
# + and -x and -y => -add(x,y)
#
# - and +x and +y => sub(x,y)
# - and -x and +y => -add(x,y)
# - and +x and -y => add(x,y)
# - and -x and -y => sub(y,x)
#
# Then if we are doing subtraction,
# need to figure out which number is bigger
# so we can flip again, if necessary




class StringNumber:
    """Strings that represent numbers (instead of native numeric types)
    """

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
        sval = self.value
        oval = other.value
        if not self.negative and not other.negative:
            return self.__add_process(sval, oval, False)
        elif self.negative and not other.negative:
            return self.__sub_process(oval, sval)
        elif not self.negative and other.negative:
            return self.__sub_process(sval, oval)
        else:
            return self.__add_process(sval, oval, True)

    def __sub__(self, other):
        sval = self.value
        oval = other.value
        if not self.negative and not other.negative:
            return self.__sub_process(sval, oval)
        elif self.negative and not other.negative:
            return self.__add_process(sval, oval, True)
        elif not self.negative and other.negative:
            return self.__add_process(sval, oval, False)
        else:
            return self.__sub_process(oval, sval)

    def __add_process(self, val1, val2, flip=False):
        retval = StringNumber.__add(val1, val2)
        retval.negative = flip
        return retval

    def __sub_process(self, val1, val2):
        comp_val = StringNumber.__compare(val1, val2)
        sign_flip = False
        retval = None
        if comp_val > 0:
            retval = StringNumber.__subtract(val1, val2)
            sign_flip = False
        elif comp_val < 0:
            retval = StringNumber.__subtract(val2, val1)
            sign_flip = True
        else:
            retval = StringNumber("0")
        if sign_flip:
            retval.negative = True
        return retval




    def __cmp__(self, other):
        """Basic cases:
        Both positive then just compare strings
        Both negative then just compare strings and reverse answer
        Both zero then they are equal
        Different signs then figure out which one is negative and it is smallest"""

        if not self.value.lstrip('0') and not other.value.lstrip('0'):
            return 0
        elif self.negative and other.negative:
            return -(StringNumber.__compare(self.value, other.value))
        elif not self.negative and not other.negative:
            return StringNumber.__compare(self.value,other.value)
        else:
            if self.negative:
                return -1
            else:
                return 1

    def __len__(self):
        return len(self.value)

    @staticmethod
    def __compare(first, second):
        """Values are both strings"""
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        else:
            for x in zip(first, second):
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
        rev_first = first.zfill(len(second))[::-1]
        rev_second = second.zfill(len(first))[::-1]

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
    def __subtract(minuend, subtrahend):
        """ Assuming we already know the minuend is a numeric value
        greater than the subtrahend
        """
        # Using Austrian method
        rev_minu = minuend[::-1]
        rev_subt = subtrahend.zfill(len(rev_minu))[::-1]

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
        return StringNumber(answer_str)





if __name__ == "__main__":
    """Canary in the coal mine versions just to make things even sort of work
    before going into test framework
    """
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

