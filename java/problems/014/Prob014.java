import java.util.*;

public class Prob014 {	
    public static Map<Long, Integer> chainLengthCache =
            new HashMap<Long, Integer>(1000000);

	public static void main(String[] args){
        int longestChainLength = 0;
        int longestChainStart = -1;
        for (int i = 1; i < 1000000; ++i) {
            int chainLength = collatzChainLength(i);
            if (chainLength > longestChainLength) {
                longestChainLength = chainLength;
                longestChainStart = i;
            }
        }
        System.out.println(longestChainStart);
    }

    // Get the length of the Collatz chain starting at "num"
    public static int collatzChainLength(int start) {
        int length = 1;
        for (long current = start; current != 1l; current = next(current)) {
            if (chainLengthCache.containsKey(current)) {
                length += chainLengthCache.get(current) - 1;
                break;
            }
            length++;
        }
        chainLengthCache.put((long) start, length);
        return length;
    }

    // Return the next number in the Collatz chain
    public static long next(long num) {
        if (num % 2 == 0) {
            return num / 2;
        } else {
            return 3 * num + 1;
        }
    }
}
