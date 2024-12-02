fn main() {
    let txt: String = std::fs::read_to_string("1.in").unwrap();
    let (left, right) = txt
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip::<i32, i32, Vec<i32>, Vec<i32>>();
    let right_counts = right.into_iter().collect::<counter::Counter<i32, i32>>();
    let ans = left.into_iter().map(|l| l * right_counts.get(&l).unwrap_or(&0)).sum::<i32>();
    println!("{:?}", ans);
}
