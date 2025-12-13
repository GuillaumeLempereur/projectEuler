/*
 * p7
 */

fn main(){
    const LIM: usize = 10001;
    let mut primes = vec![];

    let mut n = 2;
    loop {
        let mut is_prime = true;
        for p in &primes{
            if n%p == 0 {
                is_prime = false;
                break
            }
        }
        if is_prime {
            primes.push(n);
            if primes.len() == LIM {
                println!("Ans: {}", n);
                break;
            }
        }
        n += 1;
    }
}
