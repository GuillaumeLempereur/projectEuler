/*
 * p0025
 * */
import java.math.BigInteger;

public class P0025 {
	public static void main(String[] args){
		BigInteger f_n, f_n_1, lim;
		f_n = BigInteger.valueOf(1);
		f_n_1 = BigInteger.valueOf(1);
		lim = BigInteger.TEN.pow(1000-1);

		for(int n=3;n<1000000;++n){
			BigInteger tmp = f_n;
			f_n = f_n.add(f_n_1);
			f_n_1 = tmp;
			if(f_n.compareTo(lim) >= 0){
				System.out.println("Ans: " + n);
				break;
			}
		}
	}
}
