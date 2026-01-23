/*
 * p0029
 * */
import java.math.BigInteger;
import java.util.Set;
import java.util.HashSet;

public class P0029 {
	public static void main(String[] args){
		Set<BigInteger> s = new HashSet<>();
		for(int a=2;a<=100;++a){
			BigInteger n = BigInteger.valueOf(a);
			for(int b=2;b<=100;++b){
				s.add(n.pow(b));
			}
		}
		System.out.println("Ans: " + s.size());
	}
}
