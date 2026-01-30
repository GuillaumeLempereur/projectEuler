/*
 * p0034
 * */

public class P0034 {
	public static int fac(int n){
		int f = 1;
		for(int i=1;i<=n;++i){
			f *= i;
		}
		return f;
	}

	public static void main(String[] args){
		int[] facs = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int ans = 0;
		for(int i=0;i<10;++i)
			facs[i] = fac(i);

		for(int i=3;i<10000000;++i){
			int t = i, s = 0;
			while(t>0){
				s += facs[t%10];
				t /= 10;
			}
			if(i == s)
				ans += s;
		}
		System.out.println("Ans: " + ans);
	}
}
