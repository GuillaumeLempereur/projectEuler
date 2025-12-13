/*
 * p9
 */

fn main(){
    const LIM: i32 = 1000;

    for a in 1..LIM {
        for b in a..LIM {
            let c = 1000-a-b;
            if c <= 0 {
                break
            }
            if a*a+b*b == c*c {
                println!("Ans: {}", a*b*c);
                break
            }
        }
    }
}
