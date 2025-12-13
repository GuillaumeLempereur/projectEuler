/*
 * p10
 */

fn main(){
    const LIM:u32 = 2000000;
    let mut primes = vec![2,3];

    let mut ans:u64 = 5;
    for n in (6..=LIM).step_by(6) {
        let mut is_prime = true;
        for p in &primes{
            if (n-1)%p == 0 {
                is_prime = false;
                break
            }
        }
        if is_prime {
            primes.push(n-1);
            ans += (n-1) as u64; // add every prime factor
        }

        let mut is_prime = true;
        for p in &primes{
            if (n+1)%p == 0 {
                is_prime = false;
                break
            }
        }
        if is_prime {
            primes.push(n+1);
            ans += (n+1) as u64; // add every prime factor
        }
    }

    println!("Ans: {}", ans);
}
