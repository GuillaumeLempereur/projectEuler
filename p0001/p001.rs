/* 
 * p1
*/

fn main(){
    const LIM: u32 = 1000-1;
    let nb_mul_3: u32 = LIM/3;
    let nb_mul_5: u32 = LIM/5;
    let nb_mul_15: u32 = LIM/15;
    let ans = (nb_mul_3*(nb_mul_3+1)*3 + nb_mul_5*(nb_mul_5+1)*5 - nb_mul_15*(nb_mul_15+1)*15)/2;

    println!("Ans: {}", ans);
}
