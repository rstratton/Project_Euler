public class Prob017 {
	static long sum = 0l;
	public static void main(String[] args){
		for(int i = 1; i < 1001; ++i){
			sum += countLetters(i);
		}
		System.out.println(sum);
	}
	
	public static int countLetters(int num){
		if(num < 10)
			return countUnder10(num);
		if(num < 20)
			return countUnder20(num);
		if(num < 100)
			return countUnder100(num);
		if(num < 1000)
			return countUnder1000(num);
		return 11;
	}
	
	public static int countUnder10(int num){
		if(num == 0)
			return 0;
		if(num == 1)
			return 3;
		if(num == 2)
			return 3;
		if(num == 3)
			return 5;
		if(num == 4)
			return 4;
		if(num == 5)
			return 4;
		if(num == 6)
			return 3;
		if(num == 7)
			return 5;
		if(num == 8)
			return 5;
		if(num == 9)
			return 4;
		return 0;
	}
	
	public static int countUnder20(int num){
		if(num == 10)
			return 3;
		if(num == 11)
			return 6;
		if(num == 12)
			return 6;
		if(num == 13)
			return 8;
		if(num == 14)
			return 8;
		if(num == 15)
			return 7;
		if(num == 16)
			return 7;
		if(num == 17)
			return 9;
		if(num == 18)
			return 8;
		if(num == 19)
			return 8;
		return 0;
	}
	
	public static int countUnder100(int num){
		int tens = (num - num % 10)/10;
		int ones = num % 10;
		if(tens == 0)
			return countUnder10(ones);
		if(tens == 1)
			return countUnder20(num);
		if(tens == 2)
			return 6 + countUnder10(ones);
		if(tens == 3)
			return 6 + countUnder10(ones);
		if(tens == 4)
			return 5 + countUnder10(ones);
		if(tens == 5)
			return 5 + countUnder10(ones);
		if(tens == 6)
			return 5 + countUnder10(ones);
		if(tens == 7)
			return 7 + countUnder10(ones);
		if(tens == 8)
			return 6 + countUnder10(ones);
		if(tens == 9)
			return 6 + countUnder10(ones);
		return 0;
	}
	
	public static int countUnder1000(int num){
		int ones = num % 10;
		int tens = ((num - ones) % 100)/10;
		int hundreds = (num - tens * 10 - ones)/100;
		if(hundreds == 1){
			if(tens == 0 && ones == 0)
				return 10;
			else
				return 13 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 2){
			if(tens == 0 && ones == 0)
				return 10;
			else
				return 13 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 3){
			if(tens == 0 && ones == 0)
				return 12;
			else
				return 15 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 4){
			if(tens == 0 && ones == 0)
				return 11;
			else
				return 14 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 5){
			if(tens == 0 && ones == 0)
				return 11;
			else
				return 14 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 6){
			if(tens == 0 && ones == 0)
				return 10;
			else
				return 13 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 7){
			if(tens == 0 && ones == 0)
				return 12;
			else
				return 15 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 8){
			if(tens == 0 && ones == 0)
				return 12;
			else
				return 15 + countUnder100(tens * 10 + ones);
		}
		if(hundreds == 9){
			if(tens == 0 && ones == 0)
				return 11;
			else
				return 14 + countUnder100(tens * 10 + ones);
		}
		return 0;
	}
}
