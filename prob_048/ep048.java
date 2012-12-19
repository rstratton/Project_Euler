import java.math.*;
import java.lang.*;

public class ep048{
	static BigInteger sum = new BigInteger("0");
	public static void main(String[] args){
		for(int i = 1; i < 1001; ++i){
			sum = sum.add((new BigInteger((new Integer(i)).toString())).pow(i));
		}
		System.out.println(sum.toString());
	}
}
