import java.util.*;
import java.lang.*;

public class EP3_1{
	static Long testNum = 600851475143l;
	
	static void factorize(long num, ArrayList<Long> factors){
		long lastPrimeFactor = 2l;
		while(num > 1){
			for(long i = lastPrimeFactor; i <= num; ++i){
				if(num % i == 0){
					factors.add(i);
					num /= i;
				}
			}
		}
	}
	
	public static void main(String[] args){
		ArrayList<Long> factors = new ArrayList<Long>();
		factorize(testNum, factors);
		System.out.println(factors.get(factors.size()-1));
	}
}
			
	

