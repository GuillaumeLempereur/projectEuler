/*
 * p0032
 * there are 623530 pandigital numbers
 * 1 digit: 1 to 9
 * 2 digits: 12 to 98 : 9*8 = 9!/7!
 * 3 digits: 123 to 987 : 9*8*7 = 9!/6!
 *
 * a * b = c
 * c_nb_digit >= b_nb_digit + a_nb_digit ; A * BBBB >= CCCC or AA * BBB >= CCCC
 * c is 4 digits minimun, a is 1 or 2 digts and b is 4 or 3 digits
 * */
import java.util.Set;
import java.util.HashSet;

public class P0032 {
	public static int fac(int n){
		int f = 1;
		for(int i=1;i<=n;++i){
			f *= i;
		}
		return f;
	}
	
	public static void main(String[] args){
		int ans = 0;
		Set<Integer> s = new HashSet<>();

		//enumerate all 4 digits pandigital => c c1 c2 c3 c4 : c4 is 2, 4, 6, 8
		for(int c = 1234;c<=9876;++c){
			if(c%2!=0)
				continue;
			int c1 = c/1000, c2 = (c/100)%10, c3 = (c/10)%10, c4 = c%10;
			if(c1*c2*c3*c4*(c1-c2)*(c1-c3)*(c1-c4)*(c2-c3)*(c2-c4)*(c3-c4) == 0)
				continue;
			//enumerate all 1 to 2 digits pandigital => a c1 or c1
			for(int a1=1;a1<=9;++a1){
				if((c1-a1)*(c2-a1)*(c3-a1)*(c4-a1)==0)
					continue;
				for(int a2=0;a2<=9;++a2){
					if((c1-a2)*(c2-a2)*(c3-a2)*(c4-a2)==0)
						continue;
					if(a1 != a2){
						int a = a2*10+a1;
						if(c%a==0){
							int b = c/a;
							if(a<10 && b>1000 && b < 10000){
								int b1 = b/1000, b2 = (b/100)%10, b3 = (b/10)%10, b4 = b%10;
								if((b1-b2)*(b1-b3)*(b1-b4)*(b2-b3)*(b2-b4)*(b3-b4)==0)
									continue;
								if(b1*b2*b3*b4*(a1-b1)*(a1-b2)*(a1-b3)*(a1-b4)==0)
									continue;
								if((c1-b1)*(c1-b2)*(c1-b3)*(c1-b4)*(c2-b1)*(c2-b2)*(c2-b3)*(c2-b4)*(c3-b1)*(c3-b2)*(c3-b3)*(c3-b4)*(c4-b1)*(c4-b2)*(c4-b3)*(c4-b4)==0)
									continue;
								//System.out.println(a + " " + b + " " + c);
								if(!s.contains(c))
									ans += c;
								s.add(c);
							}else if(a>10 && b>100 && b < 1000){
								int b1 = b/100, b2 = (b/10)%10, b3 = b%10;
								if((b1-b2)*(b1-b3)*(b2-b3)==0)
									continue;
								if(b1*b2*b3*(a1-b1)*(a1-b2)*(a1-b3)*(a2-b1)*(a2-b2)*(a2-b3)==0)
									continue;
								if((c1-b1)*(c1-b2)*(c1-b3)*(c2-b1)*(c2-b2)*(c2-b3)*(c3-b1)*(c3-b2)*(c3-b3)*(c4-b1)*(c4-b2)*(c4-b3)==0)
									continue;
								//System.out.println(a + " " + b + " " + c);
								if(!s.contains(c))
									ans += c;
								s.add(c);
							}
						}
					}
				}
			}
		}

		System.out.println("Ans: " + ans);
	}
}
