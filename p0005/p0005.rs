/*
 * p5
 */

fn main(){
    const LIM: usize = 20;
    let mut primes = vec![];
    let mut ans: u32 = 1;

    for n in 2..=LIM {
        let mut is_prime = true;
        for p in &primes{
            if n%p == 0 {
                is_prime = false;
                break
            }
        }
        if is_prime {
            ans *= n as u32;
            primes.push(n);
        }
    }

    for p in primes {
        let exp = ((LIM as f64).log(p as f64).floor() - 1.0) as u32;
        if exp == 0 {
            break;
        }
        ans *= p.pow(exp) as u32;
    }

    println!("{}", ans);
}
