import java.lang.*;
import java.math.*;

class Prob012 {
	public static final int MAX = 1000000;
	public static int[] sieve = Erat.generateSieve(MAX);
	
	public static void main(String[] args){
		int triNumber = 0;
		for(int i = 1; i < MAX; ++i){
			triNumber += i;
			if(numFactors(triNumber) > 500)
				System.out.println(triNumber);
		}
	}
	
	public static int numFactors(int num){
		int[] primeFactorsCount = primeFactorsCount(num, null);
		int primeCombos = 1;
		for(int i = 0; i < primeFactorsCount.length; ++i){
			primeCombos *= primeFactorsCount[i];
		}
		return primeCombos;
	}
	
	public static int[] primeFactorsCount(int num, int[] primeFactorsCount){
		if(primeFactorsCount == null){
			primeFactorsCount = new int[sieve.length];
			for(int i = 0; i < primeFactorsCount.length; ++i){ //Fill occurrences array with 1's
				primeFactorsCount[i] = 1;
			}
		}
		if(num == 1){
			return primeFactorsCount;
		}
		for(int i = 0; i < num && i < sieve.length; ++i){
			if(num % sieve[i] == 0){
				++(primeFactorsCount[i]);
				primeFactorsCount(num / sieve[i], primeFactorsCount);
				break;
			}
		}
		return primeFactorsCount;		
	}
}
