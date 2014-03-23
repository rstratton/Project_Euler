/*Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.*/

public class Prob006 {	
	static long computeSumOfSquares(){
		long sumOfSquares = 0l;
		for(long i = 1l; i < 101l; ++i){
			sumOfSquares += i*i;
		}
		return sumOfSquares;
	}
	
	static long computeSquareOfSum(){
		long sum = 0;
		for(long i = 1; i < 101; ++i){
			sum += i;
		}
		return sum*sum;
	}
	
	public static void main(String[] args){
        System.out.println(computeSquareOfSum() - computeSumOfSquares());
	}	
}
