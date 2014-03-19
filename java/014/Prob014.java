import java.util.Scanner;
import java.math.BigInteger;

public class Prob014 {	
	public static void main(String[] args){
		System.out.println(findLongestLength(1000000));
	}
	
	public static long collatzLength(BigInteger startNum){
		long pathLength = 1;
		if(startNum.compareTo(new BigInteger("1")) == 0 || startNum.compareTo(new BigInteger("0")) == 0)
			return pathLength;
		if(startNum.mod(new BigInteger("2")).compareTo(new BigInteger("0")) == 0){
			pathLength += collatzLength(startNum.divide(new BigInteger("2")));
			return pathLength;
		}
		else{
			pathLength += collatzLength(startNum.multiply(new BigInteger("3")).add(new BigInteger("1")));
			return pathLength;
		}
	}
	
	public static long findLongestLength(long max){
		long longestLength = 0;
		long number = 0;
		long length = 0;
		for(int i = 0; i <= max; ++i){
			length = collatzLength(new BigInteger(new Integer(i).toString()));
			if(length >= longestLength){
				number = i;
				longestLength = length;
			}
		}
		return number;
	}
}

		
