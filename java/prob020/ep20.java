import java.math.BigInteger;

public class ep20{
	public static void main(String[] args){
		BigInteger number = new BigInteger("100");
		for(int i = 99; i > 0; --i){
			number = number.multiply(new BigInteger((new Long(i)).toString()));
		}
		String product = number.toString();
		long sum = 0;
		for(int i = 0; i < product.length(); ++i){
			sum += product.charAt(i) - 48;
		}
		System.out.println(sum);
	}
}
