/*
 * p0026
 * */

import java.util.*;

public class P0026 {
	public static void main(String[] args){
		int recLen = 0, d = 1;
		for(int n=2;n<1000;++n){
			List<Integer> remainders = new ArrayList<>();
			int r = 1;
			for(int i=0;i<1000;++i){
				r = (10*r)%n;
				if(r==0) // no recurrence
					break;
				int idx;
				if((idx = remainders.indexOf(r)) >= 0){
					if(i-idx > recLen){
						recLen = i-idx;
						d = n;
					}
					break;
				}
				remainders.add(r);
			}
		}
		System.out.println("Ans: " + d);
	}
}
