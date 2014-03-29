import java.util.*;
import java.lang.Integer;

public class Prob012 {
	public static void main(String[] args){
        for (Integer triangleNumber : new TriangleNumberList()) {
            PrimeFactorization pf = new PrimeFactorization(triangleNumber);
            if (pf.divisorCount() > 500) {
                System.out.println(triangleNumber);
                break;
            }
        }
	}

    static class TriangleNumberList implements Iterable<Integer> {
        @Override
        public Iterator<Integer> iterator() {
            return new Iterator<Integer>() {
                private int lastTriangleNumber = 0;
                private int nextAddition = 1;

                @Override
                public Integer next() {
                    lastTriangleNumber += nextAddition++;
                    return new Integer(lastTriangleNumber);
                }

                @Override
                public boolean hasNext() { return true; }

                @Override
                public void remove() {}
            };
        }
    }
}
