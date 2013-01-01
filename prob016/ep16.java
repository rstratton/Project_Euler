import java.math.BigInteger;

public class ep16{
	public static void main(String[] args){
		BigInteger number = new BigInteger("2");
		for(int i = 2; i < 1001; ++i){
			number = number.multiply(new BigInteger("2"));
		}
		String product = number.toString();
		long sum = 0;
		for(int i = 0; i < product.length(); ++i){
			sum += product.charAt(i) - 48;
		}
		System.out.println(sum);
	}
}
