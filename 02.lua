local target = {red = 12, green = 13, blue = 14}
local sum, pwr = 0, 0

for id, games in io.open("02.txt"):read("*a"):gmatch("Game (%d+): (.-)\n") do
    local g, cur = true, {}

    for game in games:gmatch("[^;]+") do
        for n, color in game:gmatch("(%d+) (%w+)") do
            n = tonumber(n)
            cur[color] = math.max(cur[color] or 0, n)
            g = g and n <= target[color]
        end
    end

    sum = sum + (g and tonumber(id) or 0)
    pwr = pwr + cur.red * cur.green * cur.blue
end

print(sum, pwr)
