/*
 * p0039
 * */
import java.util.*;
import java.util.HashSet;
import org.javatuples.Triplet;


public class P0039 {
	public static void main(String[] args){
		Set<Triplet<Integer, Integer, Integer>> s = new HashSet<>();
		int[] nbTri = new int[1001];

		// a+b+c <= 1000 and a >= b >= c
		for(int a = 1;a<999;a++)
			for(int c = 1;a+c<1000 && c <= a;c++){
				int b = (int) Math.sqrt(a*a-c*c);
				if(b<c)
					break;
				if(b*b+c*c == a*a){
					int p = a+b+c;
					if(p>1000)
						continue;
					s.add(new Triplet<Integer, Integer, Integer>(a, b, c));
				}
			}
		int ans = 0;
		for (Triplet<Integer, Integer, Integer> t : s) {
			int p = t.getValue0() + t.getValue1() + t.getValue2();
			nbTri[p]++;
		}
		int max = 0;
		for(int i=0;i<=1000;++i){
			if(max < nbTri[i]){
				max = nbTri[i];
				ans = i;
			}
		}
		System.out.println("Ans: " + ans);
	}
}
