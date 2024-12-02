use  std::iter::zip;


fn main() {
    let txt: String = std::fs::read_to_string("1.in").unwrap();
    let (mut left, mut right) = txt
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip::<i32, i32, Vec<i32>, Vec<i32>>();
    left.sort_unstable();
    right.sort_unstable();
    let ans = zip(left, right).map(|(l, r)| (r - l).abs()).sum::<i32>();
    println!("{:?}", ans);
}
