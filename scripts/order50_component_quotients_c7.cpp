#include <bits/stdc++.h>
using namespace std;

struct Solution {
    vector<int> sizes;
    vector<int> diagonal;
    vector<vector<int>> quotient;
};

constexpr int cell_count = 7;
constexpr int diagonal_sum = 2;
constexpr int target_trace_square = 64;
long long search_nodes = 0;
long long complete_row_sum_assignments = 0;
vector<Solution> solutions;

void generate_partitions(
    int remainder,
    int parts,
    int minimum,
    vector<int>& current,
    vector<vector<int>>& output
) {
    if (parts == 0) {
        if (remainder == 0) output.push_back(current);
        return;
    }
    for (int value = minimum; value <= remainder / parts; ++value) {
        current.push_back(value);
        generate_partitions(remainder - value, parts - 1, value, current, output);
        current.pop_back();
    }
}

void generate_diagonals(
    int index,
    int remainder,
    vector<int>& current,
    vector<vector<int>>& output
) {
    if (index == cell_count - 1) {
        current.push_back(remainder);
        output.push_back(current);
        current.pop_back();
        return;
    }
    for (int value = 0; value <= remainder; ++value) {
        current.push_back(value);
        generate_diagonals(index + 1, remainder - value, current, output);
        current.pop_back();
    }
}

vector<pair<int, int>> pair_options(
    int left_size,
    int right_size,
    int left_remainder,
    int right_remainder
) {
    vector<pair<int, int>> output{{0, 0}};
    const int common = gcd(left_size, right_size);
    const int left_unit = right_size / common;
    const int right_unit = left_size / common;
    const int maximum = min({
        6 / left_unit,
        6 / right_unit,
        left_remainder / left_unit,
        right_remainder / right_unit,
        right_size / left_unit,
        left_size / right_unit,
    });
    for (int multiplier = 1; multiplier <= maximum; ++multiplier) {
        const int left = left_unit * multiplier;
        const int right = right_unit * multiplier;
        // A biregular block in a graph without 4-cycles cannot make the same
        // pair of vertices have two common neighbours.
        const long long left_pairs =
            1LL * left_size * left * (left - 1);
        const long long right_capacity =
            1LL * right_size * (right_size - 1);
        const long long right_pairs =
            1LL * right_size * right * (right - 1);
        const long long left_capacity =
            1LL * left_size * (left_size - 1);
        if (left_pairs <= right_capacity && right_pairs <= left_capacity) {
            output.push_back({left, right});
        }
    }
    return output;
}

bool is_connected(const vector<vector<int>>& quotient) {
    vector<int> seen(cell_count, 0);
    queue<int> pending;
    seen[0] = 1;
    pending.push(0);
    while (!pending.empty()) {
        const int left = pending.front();
        pending.pop();
        for (int right = 0; right < cell_count; ++right) {
            if (left != right && quotient[left][right] > 0 && !seen[right]) {
                seen[right] = 1;
                pending.push(right);
            }
        }
    }
    return accumulate(seen.begin(), seen.end(), 0) == cell_count;
}

bool satisfies_cubic_identity(
    const vector<vector<int>>& quotient,
    const vector<int>& sizes
) {
    int square[10][10] = {{0}};
    int cube[10][10] = {{0}};
    for (int row = 0; row < cell_count; ++row) {
        for (int column = 0; column < cell_count; ++column) {
            for (int middle = 0; middle < cell_count; ++middle) {
                square[row][column] +=
                    quotient[row][middle] * quotient[middle][column];
            }
        }
    }
    for (int row = 0; row < cell_count; ++row) {
        for (int column = 0; column < cell_count; ++column) {
            for (int middle = 0; middle < cell_count; ++middle) {
                cube[row][column] +=
                    square[row][middle] * quotient[middle][column];
            }
        }
    }
    for (int row = 0; row < cell_count; ++row) {
        for (int column = 0; column < cell_count; ++column) {
            const int value =
                cube[row][column]
                + 2 * square[row][column]
                - 5 * quotient[row][column]
                - (row == column ? 8 : 0);
            if (value != 5 * sizes[column]) return false;
        }
    }
    return true;
}

bool satisfies_radius_two_inequalities(
    const vector<vector<int>>& quotient,
    const vector<int>& sizes
) {
    int square[10][10] = {{0}};
    for (int row = 0; row < cell_count; ++row) {
        for (int column = 0; column < cell_count; ++column) {
            for (int middle = 0; middle < cell_count; ++middle) {
                square[row][column] +=
                    quotient[row][middle] * quotient[middle][column];
            }
        }
    }
    for (int row = 0; row < cell_count; ++row) {
        for (int column = 0; column < cell_count; ++column) {
            const int left = square[row][column] - (row == column ? 6 : 0);
            const int right =
                sizes[column]
                - (row == column ? 1 : 0)
                - quotient[row][column];
            if (left > right) return false;
        }
    }
    return true;
}

struct PairVariable {
    int left;
    int right;
    vector<pair<int, int>> options;
};

void search_for_sizes_and_diagonal(
    const vector<int>& sizes,
    const vector<int>& diagonal
) {
    vector<int> remainder(cell_count);
    for (int index = 0; index < cell_count; ++index) {
        remainder[index] = 6 - diagonal[index];
    }

    vector<PairVariable> variables;
    for (int left = 0; left < cell_count; ++left) {
        for (int right = left + 1; right < cell_count; ++right) {
            auto options = pair_options(
                sizes[left],
                sizes[right],
                remainder[left],
                remainder[right]
            );
            if (options.size() > 1) {
                variables.push_back({left, right, move(options)});
            }
        }
    }
    sort(
        variables.begin(),
        variables.end(),
        [](const PairVariable& first, const PairVariable& second) {
            if (first.options.size() != second.options.size()) {
                return first.options.size() < second.options.size();
            }
            return first.left + first.right < second.left + second.right;
        }
    );

    const int variable_count = static_cast<int>(variables.size());
    vector<array<int, 10>> suffix_maximum(variable_count + 1);
    for (auto& row : suffix_maximum) row.fill(0);
    vector<int> suffix_trace(variable_count + 1, 0);
    for (int position = variable_count - 1; position >= 0; --position) {
        suffix_maximum[position] = suffix_maximum[position + 1];
        const auto& variable = variables[position];
        int maximum_left = 0;
        int maximum_right = 0;
        int maximum_trace = 0;
        for (const auto& option : variable.options) {
            maximum_left = max(maximum_left, option.first);
            maximum_right = max(maximum_right, option.second);
            maximum_trace = max(
                maximum_trace,
                2 * option.first * option.second
            );
        }
        suffix_maximum[position][variable.left] += maximum_left;
        suffix_maximum[position][variable.right] += maximum_right;
        suffix_trace[position] =
            suffix_trace[position + 1] + maximum_trace;
    }
    for (int index = 0; index < cell_count; ++index) {
        if (suffix_maximum[0][index] < remainder[index]) return;
    }

    vector<vector<int>> quotient(
        cell_count,
        vector<int>(cell_count, 0)
    );
    int initial_trace = 0;
    for (int index = 0; index < cell_count; ++index) {
        quotient[index][index] = diagonal[index];
        initial_trace += diagonal[index] * diagonal[index];
    }

    function<void(int, int)> recurse = [&](int position, int trace_square) {
        ++search_nodes;
        if (trace_square > target_trace_square) return;
        if (trace_square + suffix_trace[position] < target_trace_square) return;
        for (int index = 0; index < cell_count; ++index) {
            if (remainder[index] < 0) return;
            if (remainder[index] > suffix_maximum[position][index]) return;
        }
        if (position == variable_count) {
            if (any_of(
                    remainder.begin(),
                    remainder.end(),
                    [](int value) { return value != 0; }
                )) {
                return;
            }
            if (trace_square != target_trace_square) return;
            ++complete_row_sum_assignments;
            if (!is_connected(quotient)) return;
            if (!satisfies_cubic_identity(quotient, sizes)) return;
            if (!satisfies_radius_two_inequalities(quotient, sizes)) return;
            solutions.push_back({sizes, diagonal, quotient});
            return;
        }

        const auto& variable = variables[position];
        for (const auto& option : variable.options) {
            const int left_value = option.first;
            const int right_value = option.second;
            if (left_value > remainder[variable.left]) continue;
            if (right_value > remainder[variable.right]) continue;
            quotient[variable.left][variable.right] = left_value;
            quotient[variable.right][variable.left] = right_value;
            remainder[variable.left] -= left_value;
            remainder[variable.right] -= right_value;
            recurse(
                position + 1,
                trace_square + 2 * left_value * right_value
            );
            remainder[variable.left] += left_value;
            remainder[variable.right] += right_value;
        }
        quotient[variable.left][variable.right] = 0;
        quotient[variable.right][variable.left] = 0;
    };

    recurse(0, initial_trace);
}

int main() {
    vector<vector<int>> partitions;
    vector<int> current;
    generate_partitions(50, cell_count, 1, current, partitions);
    vector<vector<int>> diagonals;
    current.clear();
    generate_diagonals(0, diagonal_sum, current, diagonals);

    for (const auto& sizes : partitions) {
        for (const auto& diagonal : diagonals) {
            bool feasible = true;
            for (int index = 0; index < cell_count; ++index) {
                if (diagonal[index] >= sizes[index]) feasible = false;
            }
            if (feasible) search_for_sizes_and_diagonal(sizes, diagonal);
        }
    }

    cout << "solutions " << solutions.size()
         << " nodes " << search_nodes
         << " leaves " << complete_row_sum_assignments
         << "\n";
    return solutions.empty() ? 0 : 1;
}
