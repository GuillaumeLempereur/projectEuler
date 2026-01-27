/*
 * p0031
 * */

public class P0031 {
	static int ans = 0;
	static int[] coins = {200, 100, 50, 20, 10, 5, 2, 1};

	//comb the current combination , nb of time the coin is taken
	static int[] comb = {0, 0, 0, 0, 0, 0, 0, 0};

	//i the index of the chosen coin
	//tot: total of the combination
	private static void rec(int i, int tot){
		if(i==8) // no more coin to take
			return;

		while(tot < 200){
			rec(i+1, tot); // take none at 1st iteration, then 1 more at each iteration
			tot += coins[i];
			comb[i]++;
			if(tot == 200){
				ans += 1;
				break;
			}
		}
		comb[i] = 0;
	}

	public static void main(String[] args){
		rec(0, 0);
		System.out.println("Ans: " + ans);
	}
}
