import java.math.*;
import java.lang.*;

public class Prob025 {
	static BigInteger prevTerm = new BigInteger("1");
	static BigInteger curTerm = new BigInteger("1");
	static BigInteger termNum = new BigInteger("2");
	
	public static void main(String[] args){
		while(numDigits(curTerm) < 1000){
			nextTerm();
			termNum = termNum.add(BigInteger.ONE);
		}
		System.out.println(termNum.toString());
	}
	
	static int numDigits(BigInteger a){                 
		return ((a.toString()).toCharArray()).length;
	}
	
	static void nextTerm(){
		BigInteger temp = new BigInteger(curTerm.toString());
		curTerm = curTerm.add(prevTerm);
		prevTerm = temp;
	}
	
}
