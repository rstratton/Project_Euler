public class Prob007 {
	static boolean isPrime(long num){
		for(long i = 2; i < num/2 + 1; ++i){
			if(num % i == 0)
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		int primeCount = 0;
		long prime = 0l;
		for(long i = 2l; primeCount < 10001; i++){
			if(isPrime(i)){
				++primeCount;
				prime = i;
			}
		}
        System.out.println(prime);
	}
}

