/*
 * p0030
 * */

public class P0030 {
	public static void main(String[] args){
		int ans = 0;

		/*
		 * largest number: n*(9**5) < 10**n
		 * 59049*n < 10**n
		 * log(59049*n) < n => n <= 5
		*/

		for(int n=2;n<1000000;++n){
			int t = n, sum = 0;
			while(t > 0){
				sum += Math.pow(t%10, 5);
				t /= 10;
			}
			if(sum > 1 && sum == n) // if sum = 1 : ignore
				ans += sum;
		}
		System.out.println("Ans: " + ans);
	}
}
