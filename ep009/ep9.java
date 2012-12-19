// a < b < c
// a + b + c = 1000
// find a*b*c;

public class ep9{
	static int a = 0;
	static int b = 0;
	static int c = 0;
	
	public static void main(String[] args){
		calcTriplet();
		System.out.println(a*b*c);
	}
	
	static void calcTriplet(){
		for(int ci = 0; ci < 1000; ++ci){
			for(int bi = 0; bi < ci; ++bi){
				for(int ai = 0; ai < bi; ++ai){
					if(ai*ai + bi*bi == ci*ci && ai + bi + ci == 1000){
						a = ai;
						b = bi;
						c = ci;
					}
				}
			}
		}
		
	}
}
