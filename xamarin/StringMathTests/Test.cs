using NUnit.Framework;
using System;
using HelloXamarin;


namespace HelloXamarinTest
{
	[TestFixture ()]
	public class Test
	{
		[Test ()]
		public void BasicInstantiation ()
		{
			var testval = new StringNumber ("123");	
			Assert.AreEqual ("123", testval.Value);
		}

		[Test ()]
		[ExpectedException(typeof(Exception))]
		public void EmptyString() 
		{
			new StringNumber ("");
		}

		[Test ()]
		[ExpectedException(typeof(Exception))]
		public void AlphaNumeric()
		{
			new StringNumber ("abc123");
		}

		[Test ()]
		[ExpectedException(typeof(Exception))]
		public void NonNumeric()
		{
			new StringNumber ("-123");
			// TODO: This should pass in the future once we deal with negative numbersds
		}


		[Test ()]
		public void TestAddFirstNumberIsLonger ()
		{
			var val1 = new StringNumber ("987654321");
			var val2 = new StringNumber ("1234");
			var retval = StringNumberAdder.add (val1, val2);
			Assert.IsNotNull (retval);
			Assert.AreEqual ("987655555", retval.Value); 
		}


		[Test ()]
		public void TestAddSecondNumberIsLonger ()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("12345567");
			var retval = StringNumberAdder.add (val1, val2);
			Assert.IsNotNull (retval);
			Assert.AreEqual ("12345690", retval.Value); 
		}


		[Test ()]
		public void TestAddNumbersOfSameLength()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("987");
			var retval = StringNumberAdder.add (val1, val2);
			Assert.AreEqual ("1110", retval.Value);
		}

		[Test ()]
		public void TestOverloadedAddOperator()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("987");
			Assert.AreEqual ("1110", (val1 + val2).Value);
		}

		[Test ()]
		public void TestOverloadedEqualsOperatorSame()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("123");
			Assert.IsTrue (val1 == val2);
		}

		[Test ()]
		public void TestOverloadedEqualsOperatorNotSame()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("987");
			Assert.IsFalse (val1 == val2);
		}


		[Test ()]
		public void TestOverloadedNotEqualsOperatorSame()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("123");
			Assert.IsFalse (val1 != val2);
		}

		[Test ()]
		public void TestOverloadedNotEqualsOperatorNotSame()
		{
			var val1 = new StringNumber ("123");
			var val2 = new StringNumber ("987");
			Assert.IsTrue (val1 != val2);
		}

		[Test ()]
		public void TestEqualsMethodEqualObject()
		{
			var val1 = new StringNumber ("123");
			Assert.IsTrue (val1.Equals (new StringNumber ("123")));
		}

		[Test ()]
		public void TestEqualsMethodNotEqualObjects()
		{
			var val1 = new StringNumber ("123");
			Assert.IsFalse (val1.Equals (new StringNumber ("456")));
		}

		[Test ()]
		public void TestEqualsMethodDifferentObjects()
		{
			var val1 = new StringNumber ("123");
			Assert.IsFalse (val1.Equals ("123"));
		}

		[Test ()]
		public void TestSubtraction()
		{
			var val1 = new StringNumber ("456");
			var val2 = new StringNumber ("123");
			var retval = StringNumberSubtracter.subtract (val1, val2);
			Assert.AreEqual ("333", retval.Value);
		}

		[Test ()]
		public void TestCompareFunctionality() 
		{
			Assert.IsTrue (String.Compare ("123", "456") < 0);
			Assert.IsTrue (String.Compare ("456", "123") > 0);
			Assert.IsTrue (String.Compare ("333", "333") == 0);
			Assert.IsTrue (String.Compare ("1234", "4560") < 0);
			Assert.IsTrue (String.Compare ("1235", "0000") > 0);
			Assert.IsTrue (String.Compare ("1234", "0456") > 0); // Works with proper padding
			Assert.IsTrue (String.Compare ("1234", "456") > 0); // Example of string comparison not being same as numeric
			Assert.IsTrue (String.Compare ("1234", "12345") < 0);
		}
	}
}

