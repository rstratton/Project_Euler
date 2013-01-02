public class Erat{
	public static int[] generateSieve(int size){
		int[] sieve = new int[size];
		fillSieve(sieve, size);
		sieve[0] = 0;
		sieve[1] = 0;
		clearComposites(sieve, size);
		sieve = compactSieve(sieve, size);
		return sieve;
	}
	
	static void fillSieve(int[] sieve, int size){
		for(int i = 0; i < size; ++i){
			sieve[i] = i;
		}
	}
	
	static void clearComposites(int[] sieve, int size){
		for(int i = 2; i < size; ++i){
			if(sieve[i] != 0){
				clearMultiples(sieve, size, i);
			}
		}
	}
	
	static void clearMultiples(int[] sieve, int size, int factor){
		for(int i = 2*factor; i < size; i += factor){
			sieve[i] = 0;
		}
	}
	
	static int[] compactSieve(int[] sieve, int size){
		int numEntries = 0;
		for(int i = 0; i < size; ++i){
			if(sieve[i] != 0)
				++numEntries;
		}
		int[] compactSieve = new int[numEntries];
		int j = 0;
		for(int i = 0; i < size; ++i){
			if(sieve[i] != 0){
				compactSieve[j] = sieve[i];
				++j;
			}
		}
		return compactSieve;
	}			
}
