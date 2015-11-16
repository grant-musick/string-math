using System;
using System.Text.RegularExpressions;
using System.Text;


namespace HelloXamarin
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.WriteLine ("Hello World!");
		}
	}


	public class StringNumber
	{
		private string _value;

		public StringNumber(string value)
		{
			if (!Regex.IsMatch(value, "^[0-9]+")) 
			{
				throw new Exception ("Invalid input for StringNumber");
			}
			this._value = value;
		}

		public string Value { get { return this._value; } }

		public static StringNumber operator +(StringNumber sn1, StringNumber sn2)
		{
			return StringNumberAdder.add(sn1, sn2);
		}

		public static bool operator ==(StringNumber sn1, StringNumber sn2)
		{
			return sn1.Value == sn2.Value;
		}

		public static bool operator !=(StringNumber sn1, StringNumber sn2)
		{
			return sn1.Value != sn2.Value;
		}

		override public bool Equals(Object o)
		{
			if (o.GetType() == typeof(StringNumber)) {
				StringNumber temp = (StringNumber)o;
				return temp.Value == this.Value;
			} else {
				return false;
			}
		}

		override public int GetHashCode()
		{
			return base.GetHashCode ();
		}
	}


	public class StringNumberAdder
	{
		public static StringNumber add(StringNumber first, StringNumber second)
		{
			StringNumber temp_first;
			StringNumber temp_second;

			if (first.Value.Length > second.Value.Length) {
				temp_first = first;
				temp_second = new StringNumber (second.Value.PadLeft (first.Value.Length, '0'));
			} 
			else 
			{
				temp_first = new StringNumber(first.Value.PadLeft(second.Value.Length, '0'));
				temp_second = second;
			}

			UInt32 carry = 0;
			var sb = new StringBuilder ();
			for (int i = temp_first.Value.Length-1; i >= 0; i--) 
			{
				char elem1 = temp_first.Value [i];
				char elem2 = temp_second.Value [i];

				var val1 = UInt32.Parse (elem1.ToString());
				var val2 = UInt32.Parse (elem2.ToString());

				UInt32 total = val1 + val2 + carry;
				carry = total / 10;
				sb.Append ((total % 10).ToString ());
			}

			if (carry > 0) {
				sb.Append (carry.ToString ());
			}


			// This is fucked up if this is actually the state of the art for reversing strings
			// in C#. WTF?!?!?!

			char[] arr = sb.ToString().ToCharArray();
			Array.Reverse(arr);
			var value = new String(arr);
			return new StringNumber(value);
		}
	}



	public class StringNumberSubtracter {
		public static StringNumber subtract(StringNumber first, StringNumber second) {
			StringNumber minuend;
			StringNumber subtrahend;
			bool sign_flip = false;

			// Padd them out
			if (first.Value.Length > second.Value.Length) {
				second = new StringNumber (second.Value.PadLeft (first.Value.Length, '0'));
				minuend = first;
				subtrahend = second;
			} 
			else if (second.Value.Length > first.Value.Length) 
			{
				first = new StringNumber(first.Value.PadLeft(second.Value.Length, '0'));
				minuend = second;
				subtrahend = first;
			}
			else // same length
			{
				if (String.Compare(first.Value, second.Value) > 0) {
					minuend = first;
					subtrahend = second;
				} else {
					minuend = second;
					subtrahend = first;
				}
			}

			bool addOneToNext = false;
			StringBuilder sb = new StringBuilder();
			for(int i = minuend.Value.Length-1; i >= 0; i--) {				
				int m = Int32.Parse(minuend.Value[i].ToString());
				int s = Int32.Parse(subtrahend.Value[i].ToString());
				if (addOneToNext) {
					s += 1;
				}

				if (s > m) {
					addOneToNext = true;
					sb.Append(m+10-s);
				} else {
					addOneToNext = false;
					sb.Append(m-s);
				}
			}

			char[] chars = sb.ToString().ToCharArray();
			Array.Reverse(chars);
			return new StringNumber(new String(chars));
		}
	}
	/*
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
        return StringNumber(answer_str)	 */ 

}
