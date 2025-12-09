/*
 * p4
 */

fn main(){
    let mut max_pal = 0;
    // Try all combination of product of 2 3-digit number
    for n1 in 100..1000{
        for n2 in 100..1000{
            let n = n1*n2;
            let n_str = n.to_string();
            let l = n_str.len();
            let mut is_pal = true;

            for i in 0..=l/2{
                if n_str.as_bytes()[i] != n_str.as_bytes()[l-i-1]{
                    is_pal = false;
                    break;
                }
            }
            if is_pal{
                if max_pal < n{
                    max_pal = n;
                }
            }
        }
    }

    println!("Ans: {}", max_pal);
}
