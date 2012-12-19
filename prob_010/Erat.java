public class Erat{
	public static long[] generateSieve(int size){
		long[] sieve = new long[size];
		fillSieve(sieve, size);
		sieve[0] = 0;
		sieve[1] = 0;
		int numPrimes = clearComposites(sieve, size);
		return sieve;
	}
	
	static void fillSieve(long[] sieve, int size){
		for(int i = 0; i < size; ++i){
			sieve[i] = i;
		}
	}
	
	static int clearComposites(long[] sieve, int size){
		int numPrimes = 0;
		for(int i = 2; i < size; ++i){
			if(sieve[i] != 0){
				++numPrimes;
				clearMultiples(sieve, size, i);
			}
		}
	}
	
	static void clearMultiples(long[] sieve, int size, int factor){
		for(int i = factor; i < size; i += factor){
			if(i == factor)
				continue;
			sieve[i] = 0;
		}
	}
}
