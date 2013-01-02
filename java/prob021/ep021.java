public class ep021{
	public static int[] SOPD = new int[10001];
	public static boolean[] isAmicable = new boolean[10001];
	public static long sum = 0l;
	
	public static void main(String[] args){
		initializeArray();
		fillSOPD();
		fillIsAmicable();
		sumAmicable();
		System.out.println(sum);
	}
	
	public static void initializeArray(){
		for(int i = 0; i < 10001; ++i){
			isAmicable[i] = false;
		}
	}
	
	public static void fillSOPD(){
		for(int i = 1; i < 10001; ++i){
			SOPD[i] = sumOfProperDivisors(i);
		}
	}
	
	public static int sumOfProperDivisors(int num){
		int sum = 0;
		for(int i = 1; i < num/2 + 1; ++i){
			if(num % i == 0)
				sum += i;
		}
		return sum;
	}
	
	public static void fillIsAmicable(){
		for(int i = 1; i < 10001; ++i){
			if(SOPD[i] > 10000)
				continue;
			if(i == SOPD[SOPD[i]] && i != SOPD[i])
				isAmicable[i] = true;
		}
	}
	
	public static void sumAmicable(){
		for(int i = 1; i < 10001; ++i){
			if(isAmicable[i])
				sum += i;
		}
	}	
}
			
