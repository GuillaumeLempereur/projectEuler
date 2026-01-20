/*
 * p0028
 * */

public class P0028 {
	public static void main(String[] args){
		int s = 1;
		for(int n=1;n<=500;++n){
			s += (2*n+1)*(2*n+1)*4-12*n;
		}
		System.out.println("Ans: " + s);
	}
}
