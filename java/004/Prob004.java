

public class Prob004 {
	
	static boolean isPalindrome(Long num){
		String digits = num.toString();
		int numDigits = digits.length();
		for(int i = 0; i <= numDigits/2; ++i){
			if(digits.charAt(i) != digits.charAt(numDigits - 1 - i))
				return false;
		}
		return true;
	}
	
	public static void main(String[] args){
		long largest = 0l;
		for(long i = 100l; i < 1000l; ++i){
			for(long j = 100l; j < 1000l; ++j){
				if(isPalindrome(i*j))
					if(i*j > largest)
						largest = i*j;
			}
		}
		System.out.println(largest);
	}
}
