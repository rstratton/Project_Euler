public class ep015{
	static final int GRID_SIZE = 21;
	static boolean[][] grid = new boolean[GRID_SIZE][GRID_SIZE];	//'true' indicates that node hasn't been travelled.
	static long pathCount = 0;
	static int x = 0;
	static int y = 0;
	
	public static void main(String[] args){
		initializeGrid();
		traverseGrid(0, 0);
		System.out.println(pathCount);
	}
	
	public static void traverseGrid(int xStart, int yStart){
		if(x == 0 && y == 0)
			grid[y][x] = false;
		if(x == GRID_SIZE - 1 && y == GRID_SIZE - 1){
			++pathCount;
			return;
		}
		if(checkDown()){
			++y;
			grid[y][x] = false;
			traverseGrid(xStart, yStart + 1);
			grid[y][x] = true;
			--y;
		}
		/*
		if(checkUp()){
			--y;
			grid[y][x] = false;
			traverseGrid(xStart, yStart - 1);
			grid[y][x] = true;
			++y;
		}
		*/
		if(checkRight()){
			++x;
			grid[y][x] = false;
			traverseGrid(xStart + 1, yStart);
			grid[y][x] = true;
			--x;
		}
		/*
		if(checkLeft()){
			--x;
			grid[y][x] = false;
			traverseGrid(xStart - 1, yStart);
			grid[y][x] = true;
			++x;
		}
		*/
		return;
	}
			
			
	
	public static void initializeGrid(){
		for(int i = 0; i < GRID_SIZE; ++i){
			for(int j = 0; j < GRID_SIZE; ++j){
				grid[i][j] = true;
			}
		}
	}
	
	public static boolean hasMove(){
		if(checkDown() || checkUp() || checkLeft() || checkRight())
			return true;
		else
			return false;
	}
	
	public static boolean checkDown(){
		if(y == GRID_SIZE - 1)
			return false;
		if(grid[y + 1][x] == true)
			return true;
		else
			return false;
	}
	
	public static boolean checkUp(){
		if(y == 0)
			return false;
		if(grid[y-1][x] == true)
			return true;
		else
			return false;
	}
	
	public static boolean checkRight(){
		if(x == GRID_SIZE - 1)
			return false;
		if(grid[y][x + 1] == true)
			return true;
		else
			return false;
	}
	
	public static boolean checkLeft(){
		if(x == 0)
			return false;
		if(grid[y][x - 1] == true)
			return true;
		else
			return false;
	}
}
		
