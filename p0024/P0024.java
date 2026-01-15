/*
 * p0024
 * */
import java.util.ArrayList;

public class P0024 {
	public static int fac(int n){
		int f = 1;
		for(int i=1;i<=n;++i){
			f *= i;
		}
		return f;
	}

	public static void main(String[] args){
		int n = 0, lexi = 1000000;//-1;
		ArrayList<Integer> al = new ArrayList<>();
		for(int i=0;i<10;++i)
			al.add(i);

		System.out.print("Ans: ");
		for(int i=9;i>=0;--i){
			int nbPermut = fac(i);

			int id = (lexi-n)/nbPermut;
			if((lexi-n)%nbPermut == 0){
				System.out.print(al.get(id-1));
				al.remove(id-1);
				for(int idx=al.size()-1;idx>=0;--idx) // the last permutation possible
					System.out.print(al.get(idx));
				break;
			}
			System.out.print(al.get(id));
			al.remove(id);
			
			n += ((lexi-n)/nbPermut)*nbPermut;
		}
		System.out.println();
	}
}
