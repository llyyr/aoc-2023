use std::fs::File;
use std::io::{self, BufRead};

fn p1(inp: &str) -> i32 {
    let d: Vec<_> = inp.chars().filter(|c| c.is_digit(10)).collect();
    format!("{}{}", d[0], d[d.len() - 1]).parse().unwrap()
}

fn p2(inp: &str) -> i32 {
    let mut inp = inp.to_owned();
    let words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    for (i, n) in words.iter().enumerate().map(|(i, n)| (i + 1, *n)) {
        inp = inp.replace(n, &format!("{}{}{}", n.chars().next().unwrap(), i, n.chars().last().unwrap()));
    }

    p1(&inp)
}

fn main() {
    if let Ok(file) = File::open("01.txt") {
        let lines: Vec<_> = io::BufReader::new(file).lines().filter_map(Result::ok).collect();

        let mut sum1 = 0;
        let mut sum2 = 0;

        for line in &lines {
            sum1 += p1(line);
            sum2 += p2(line);
        }

        println!("{} {}", sum1, sum2);
    }
}
