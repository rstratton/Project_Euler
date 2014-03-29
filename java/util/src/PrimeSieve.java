import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class PrimeSieve {
    private ArrayList<Integer> primesList;
    private Set<Integer> primesSet;

    /*
     * Populate 'primesList' and 'primesSet' with all prime numbers between
     * 0 and 'limit'
     */
    public PrimeSieve(int limit) {
        generatePrimes(limit);
    }

    public boolean isPrime(int n) {
        return primesSet.contains(n);
    }

    /*
     * Return a copy of the generated list of primes
     */
    public ArrayList<Integer> getPrimes() {
        return new ArrayList<Integer>(primesList);
    }

    /*
     * Return a list of all primes from 0 to 'limit'
     */
    public ArrayList<Integer> getPrimesUpTo(int limit) {
        ArrayList<Integer> result = new ArrayList<Integer>(1000);
        for (Integer prime : primesList) {
            if (prime > limit) {
                break;
            } else {
                result.add(prime);
            }
        }
        return result;
    }

    /*
     * Return a list of the first 'count' primes
     */
    public ArrayList<Integer> getPrimes(int count) {
        ArrayList<Integer> result = new ArrayList<Integer>(1000);
        for (int i = 0; i < result.size() && i <= count; ++i) {
            result.add(primesList.get(i));
        }
        return result;
    }

    /*
     * Discover all primes from 0 to 'limit' and save the results in
     * 'primesList' and 'primesSet'
     */
    private void generatePrimes(int limit) {
        int[] integers = getSequence(0, limit);
        integers[0] = 0;
        integers[1] = 0;
        primesList = new ArrayList<Integer>(1000);
        for (int i = 2; i < integers.length; ++i) {
            if (integers[i] != 0) {
                primesList.add(i);
                eliminateMultiples(i, limit + 1, integers);
            }
        }
        primesSet = new HashSet<Integer>(primesList);
    }

    /*
     * Eliminate all multiples of 'n' up to 'm' from 'integers' (where
     * 'integers' is an ordered sequence of the ints starting at 0
     */
    private void eliminateMultiples(int n, int m, int[] integers) {
        for (int i = 2*n; i < m; i += n) {
            integers[i] = 0;
        }
    }

    /*
     * Return an in-order array of integers starting at 'start' and ending at
     * 'stop'
     */
    private static int[] getSequence(int start, int stop) {
        int[] seq = new int[stop - start + 1];
        for (int i = 0; i < seq.length; ++i) {
            seq[i] = start + i;
        }
        return seq;
    }
}
