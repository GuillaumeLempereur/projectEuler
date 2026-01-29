/*
 * p0033
*/
import com.aziinod.Euler.Frac;

public class P0033 {

	public static void main(String[] args){
		int ans = 0;

		Frac f = new Frac(1,1);

		for(int n = 11;n<100;++n){ // numerator
			for(int d=11;d<100;++d){ // denominator
				int n2 = n/10, d2 = d%10;
				if(n%10 == d/10 && n2*d==n*d2 && n%10 != n2){
					f = f.mul(new Frac(n2, d2));
				}
			}
		}

		System.out.println("Ans: " + f.d);
	}
}
