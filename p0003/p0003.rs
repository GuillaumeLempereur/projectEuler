/*
 * p0003
*/

fn main(){
    let mut n: u64 = 600851475143;
    let mut d: u64 = 1;

    while n > 1 {
        d = loop {
            d += 1;
            if n%d == 0 {
                break d;
            }
        };
        println!("\tprime factor: {}", d);
        while n%d == 0 {
            n /= d;
        }
    }
    println!("Ans: {}", d);
}
