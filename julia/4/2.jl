parse_line(line) = parse.(Int, split(strip(line, ' '), r"\s+")) |> Set

open("julia/4/input1.txt") do f
    copies = Dict()
    for line in readlines(f)
        m = match(r"Card\s+(\d+):([\d\s]+)\|([\d\s]+)", line)
        game = parse(Int, m[1])
        winners = m[2] |> parse_line
        yours = m[3] |> parse_line
        n_got = intersect(winners, yours) |> length

        if !haskey(copies, game) # original 
            copies[game] = 1
        else
            copies[game] += 1
        end
        for w in (game+1):(game+n_got) # add copies
            val_add = get(copies, game, 0) # every ticket
            if !haskey(copies, w)
                copies[w] = val_add
            else
                copies[w] += val_add
            end
        end
    end
    println(copies |> values |> sum)
end
