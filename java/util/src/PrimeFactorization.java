import java.util.*;
import java.lang.Math;

public class PrimeFactorization {
    private int number;
    private Map<Integer, Integer> factorMultiplicities;
    private static int primeSieveLimit = 1000000;
    private static PrimeSieve sieve = new PrimeSieve(primeSieveLimit);

    public PrimeFactorization(int number) {
        this.number = number;
        factorMultiplicities = factorize(number);
    }

    /*
     * Return a sorted list of this number's prime factors (duplicates are
     * included)
     */
    public List<Integer> getPrimeFactors() {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (Map.Entry<Integer, Integer> entry : factorMultiplicities.entrySet()) {
            for (int i = 0; i < entry.getValue(); ++i) {
                result.add(entry.getKey());
            }
        }
        Collections.sort(result);
        return result;
    }

    /*
     * Return a sorted list of this number's prime factors (duplicates are
     * excluded)
     */
    public List<Integer> getUniquePrimeFactors() {
        ArrayList<Integer> result = new ArrayList<Integer>(
                factorMultiplicities.keySet());
        Collections.sort(result);
        return result;
    }

    /*
     * Return the multiplicity of the argument in this number's prime
     * factorization (return 0 if the number is not a prime factor).
     */
    public int multiplicity(int factor) {
        if (factorMultiplicities.containsKey(factor)) {
            return factorMultiplicities.get(factor);
        } else {
            return 0;
        }
    }

    /*
     * Return the number of integers which evenly divide the number represented
     * by the PrimeFactorization (i.e. the number which the object was
     * constructed with) including 1 and the number itself.
     */
    public int divisorCount() {
        int result = 1;
        for (int multiplicity : factorMultiplicities.values()) {
            result *= multiplicity + 1;
        }
        return result;
    }

    public static void setPrimeSieveLimit(int limit) {
        sieve = new PrimeSieve(limit);
    }

    /*
     * Given an integer, return a Map which maps the integer's prime factors to
     * those factors' multiplicities.
     */
    public static Map<Integer, Integer> factorize(int number) {
        Map<Integer, Integer> multiplicities = new HashMap<Integer, Integer>();
        ArrayList<Integer> primes = sieve.getPrimes();
        int residual = number;
        for (Integer prime : primes) {
            while (residual % prime == 0) {
                residual /= prime;
                incrementMultiplicity(prime, multiplicities);
            }
        }
        return multiplicities;
    }

    /*
     * Given a number and a map which maps integers to their multiplicity
     * (count), increment the argument number's count in the map by one.
     */
    private static void incrementMultiplicity(int number,
            Map<Integer, Integer> multiplicities) {
        if (multiplicities.containsKey(number)) {
            int currentMultiplicity = multiplicities.get(number);
            multiplicities.put(number, currentMultiplicity + 1);
        } else {
            multiplicities.put(number, 1);
        }
    }
}
