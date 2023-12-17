parse_line(line) = parse.(Int, split(strip(line, ' '), r"\s+")) |> Set

open("julia/4/input1.txt") do f
    sum = 0
    for line in readlines(f)
        m = match(r"Card\s+\d+:([\d\s]+)\|([\d\s]+)", line)
        winners = m[1] |> parse_line
        yours = m[2] |> parse_line
        n_got = intersect(winners, yours) |> length
        if n_got > 0
            sum += 2 ^ (n_got - 1) 
        end
    end
    println(sum)
end