import java.util.*;
import java.lang.Math;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class PrimeSieveTest {

    @Test
    public void testCorrectness() {
        PrimeSieve sieve = new PrimeSieve(100000);
        for (int i = 1; i < 100000; ++i) {
            assertEquals(isPrime(i), sieve.isPrime(i));
        }
    }

    // Naive implementation to check correctness
    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < n; ++i) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
