function probability(n)
    not_one = false
    j = 0
    while (!not_one)
        j += 1
        for i in 1:n
            k = rand(1:6)
            if k == 1
                break
            end

            if i == n
                not_one = true
            end
        end
    end
    return j
end

function mult_prob(count, n)
    sum = 0
    for i in 1:count
        sum += probability(n)
    end
    return sum / count
end

@time mult_prob(1_000, 30)
print(answ)
            