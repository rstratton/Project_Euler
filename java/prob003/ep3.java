public class Ep3{
	static long testNum = 600851475143l;

	static boolean isPrime(long num){
		for(long i = 2; i < num/2; i++){
			System.out.println("     Checking: " + i);
			if(num % i == 0)
				return false;
		}
		return true;
	}

	static long largestPrimeFactor(long num){
		long largest = 0;
		if(isPrime(num))
			return num;
		for(long i = 2; i <= num/2; ++i){
			System.out.println("Checking: " + i);
			if(isPrime(i))
				if(num % i == 0)
					System.out.println(i);
					largest = i;
		}
		return largest;
	}

	public static void main(String[] args){
		System.out.println(largestPrimeFactor(testNum));
		
	}
}
