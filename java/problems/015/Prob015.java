public class Prob015 {
    // NOTE: This problem can also be solved by evaluating "40 choose 20";
    // you have to take 40 discrete steps to get from the start point of the
    // grid to the end.  Half of those steps will be a downward movement, so
    // choosing 20 of the original 40 to be downward steps determines the entire
    // route, hence 40 choose 20

    public static void main(String[] args) {
        int gridSize = 20;

        // routeCount[i][j] represents the number of routes from position
        // (i, j) on the grid to the destination point (0, 0)
        long[][] routeCount = new long[gridSize + 1][gridSize + 1];

        // Initialize the lookup table with base cases (i.e. when there is only
        // one possible route)
        for (int i = 0; i < routeCount.length; ++i) {
            routeCount[i][0] = 1;
            routeCount[0][i] = 1;
        }

        // Populate the routeCount table using dynamic programming
        for (int i = 1; i < routeCount.length; ++i) {
            for (int j = 1; j < routeCount[i].length; ++j) {
                routeCount[i][j] = routeCount[i][j-1] + routeCount[i-1][j];
            }
        }

        System.out.println(routeCount[gridSize][gridSize]);
    }
}
