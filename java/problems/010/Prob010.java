public class Prob010 {
	
	public static void main(String[] args){
		int size = 2000000;
		long sum = 0l;
		//long[] sieve = Erat.generateSieve(size);
		for(int i = 0; i < size; ++i){
			if(isPrime(i)){
				sum += i;
				System.out.println(i);
			}
		}
		System.out.println(sum);
	}
	
	public static boolean isPrime(int num){
		if(num % 2 == 0 || num % 3 == 0)
			return false;
		for(int i = 6; i < num; i += 6){
			if ((num % (i - 1)) == 0 || (num % (i + 1)) == 0){
				return false;
			}
		}
		return true;
	}
}
