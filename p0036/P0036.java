/*
 * p0036
 * */
import java.lang.Math;

public class P0036 {
	public static void main(String[] args){
		int ans = 0;
		for(int i=1;i<1000000;++i){
			int n = i;
			boolean isPal = true;

			// check in base 10
			int nbDigit = (int) Math.ceil(Math.log10(n+1)), div = (int) Math.pow(10, nbDigit-1);
			for(int d=0;d<nbDigit/2;++d){
				if(n%10 != (n/div)%10){
					isPal = false;
					break;
				}
				n /= 10;
				div /= 100;
			}

			// check in binary
			n = i;
			nbDigit = (int) Math.ceil(Math.log(n+1)/Math.log(2));
			div = (int) Math.pow(2, nbDigit-1);
			for(int d=0;d<nbDigit/2;++d){
				if(n%2 != (n/div)%2){
					isPal = false;
					break;
				}
				n /= 2;
				div /= 4;
			}
			if(isPal)
				ans += i;
		}
		System.out.println("Ans: " + ans);
	}
}
