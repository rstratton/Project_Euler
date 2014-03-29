import java.math.*;
import java.lang.*;

public class Prob048 {
	public static void main(String[] args){
        BigInteger sum = BigInteger.ZERO;

		for(int i = 1; i < 1001; ++i){
            BigInteger summand = BigInteger.valueOf(i).pow(i);
            sum = sum.add(summand);
		}

        String fullSum = sum.toString();
        int length = fullSum.length();
		System.out.println(fullSum.substring(length - 10, length));
	}
}
