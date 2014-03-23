import java.util.ArrayList;

public class Prob010 {
    public static void main(String[] args) {
        PrimeSieve sieve = new PrimeSieve(2000001);
        ArrayList<Integer> primesUnderTwoMillion = sieve.getPrimes();
        long sum = 0l;
        for (Integer prime : primesUnderTwoMillion) {
            sum += prime;
        }
        System.out.println(sum);
    }
}
