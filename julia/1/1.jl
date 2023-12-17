open("julia/1/input1.txt") do f
    sum_n = 0
    for line in eachline(f)
        list_digits = Vector{Int}()
        for char in line
            if isdigit(char)
                push!(list_digits, parse(Int, char))
            end
        end
        sum_n += list_digits[1] * 10 + list_digits[end]
    end
    println(sum_n)
end