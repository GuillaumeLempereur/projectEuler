/*
 * p6
 */

fn main(){
    const LIM:u64 = 100;

    let mut sum_sq: u64 = 0;
    for n in 1..=LIM {
        sum_sq += n*n;
    }

    let mut sq_sum: u64 = 0;
    for n in 1..=LIM {
        sq_sum += n;
    }
    sq_sum *= sq_sum;

    println!("Ans: {}", sq_sum-sum_sq);
}
