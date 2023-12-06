#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <unordered_set>

int main() {
    int p1 = 0, p2 = 0;
    std::ifstream f("04.txt");
    std::string line;
    int card = 0;
    std::vector<int> copies(10, 1);
    std::unordered_set<std::string> wins;
    wins.reserve(10);

    while (std::getline(f, line)) {
        copies.push_back(1);
        wins.clear();
        int c = 0;
        std::string num;
        std::istringstream line_stream(line);
        std::getline(line_stream, num, ':');

        while (std::getline(line_stream, num, ' ')) {
            if (num.empty())
                continue;

            if (wins.count(num) > 0)
                c += 1;

            if (wins.size() < 10)
                wins.insert(num);
        }

        auto start = copies.begin() + card + 1;
        for (auto it = start; it != start + c; it++)
            *it += copies[card];

        p1 += 1 << (c - 1);
        p2 += copies[card++];
    }
    std::cout << "Part 1: " << p1 << "\nPart 2: " << p2 << std::endl;
    return 0;
}
