import java.util.*;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertArrayEquals;

public class PrimeFactorizationTest {
    @Test
    public void testCorrectness() {
        testCorrectnessFor(2, new Integer[] {2});
        testCorrectnessFor(3, new Integer[] {3});
        testCorrectnessFor(4, new Integer[] {2, 2});
        testCorrectnessFor(5, new Integer[] {5});
        testCorrectnessFor(6, new Integer[] {2, 3});
        testCorrectnessFor(7, new Integer[] {7});
        testCorrectnessFor(8, new Integer[] {2, 2, 2});
        testCorrectnessFor(9, new Integer[] {3, 3});
        testCorrectnessFor(10, new Integer[] {2, 5});
        testCorrectnessFor(11, new Integer[] {11});
        testCorrectnessFor(12, new Integer[] {2, 2, 3});
        testCorrectnessFor(24, new Integer[] {2, 2, 2, 3});
        testCorrectnessFor(64, new Integer[] {2, 2, 2, 2, 2, 2});
        testCorrectnessFor(100, new Integer[] {2, 2, 5, 5});
    }

    private void testCorrectnessFor(int num, Integer[] expectedFactors) {
        PrimeFactorization pf = new PrimeFactorization(num);
        assertEquals(divisorCount(num), pf.divisorCount());
        assertArrayEquals(expectedFactors, pf.getPrimeFactors().toArray());
    }

    // Naive but simple implementation to check correctness
    private Map<Integer, Integer> primeFactors(int n) {
        Map<Integer, Integer> multiplicities = new HashMap<Integer, Integer>();
        return multiplicities;
    }

    // Naive but simple implementation to check correctness
    private int divisorCount(int n) {
        return divisors(n).size();
    }

    // Naive but simple implementation to check correctness
    private List<Integer> divisors(int n) {
        List<Integer> divisors = new ArrayList<Integer>();
        for (int i = 1; i <= n; ++i) {
            if (n % i == 0) {
                divisors.add(i);
            }
        }
        return divisors;
    }
}
