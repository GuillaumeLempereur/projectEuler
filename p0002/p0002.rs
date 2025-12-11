/* 
 * p2
*/

fn main(){
    const LIM: u32 = 4000000;

    let mut fib_1: u32 = 0;
    let mut fib_n: u32 = 1;

    let mut ans: u32 = 0;
    ans = loop {
        (fib_1, fib_n) = (fib_n, fib_1 + fib_n);

        if fib_n > LIM {
            break ans;
        }

        if fib_n%2 == 0 {
            ans += fib_n;
        }
    };

    println!("Ans: {}", ans);
}
