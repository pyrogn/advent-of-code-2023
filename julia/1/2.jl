str_num = Dict(
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9,
)

function replace_in_line(line)::String
    for (key, value) in str_num
        line = replace(line, key => key * string(value) * key)
    end
    return line
end

function cnt_in_line(line)::Int
    sum_n = 0
    list_digits = Vector{Int}()
    for char in line
        if isdigit(char)
            push!(list_digits, parse(Int, char))
        end
    end
    sum_n += list_digits[1] * 10 + list_digits[end]
end

open("julia/1/input1.txt") do f
    sum_n = 0
    for line in eachline(f)
        line = replace_in_line(line)
        sum_n += cnt_in_line(line)
    end
    println(sum_n)
end