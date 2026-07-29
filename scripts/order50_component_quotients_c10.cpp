#include <bits/stdc++.h>
using namespace std;

struct Solution {
    vector<int> sizes;
    vector<vector<int>> quotient;
};

constexpr int cell_count = 10;
long long search_nodes = 0;
long long complete_assignments = 0;
vector<Solution> solutions;
vector<int> sizes;
vector<int> remainder;
vector<int> target_triangle_sum;
vector<int> triangle_sum;
vector<vector<int>> quotient;
int pair_product_sum = 0;

void generate_partitions(
    int remainder_value,
    int parts,
    int minimum,
    vector<int>& current,
    vector<vector<int>>& output
) {
    if (parts == 0) {
        if (remainder_value == 0) output.push_back(current);
        return;
    }
    for (int value = minimum; value <= remainder_value / parts; ++value) {
        current.push_back(value);
        generate_partitions(
            remainder_value - value,
            parts - 1,
            value,
            current,
            output
        );
        current.pop_back();
    }
}

vector<pair<int, int>> pair_options(int left, int right) {
    const int left_size = sizes[left];
    const int right_size = sizes[right];
    const int common = gcd(left_size, right_size);
    const int left_unit = right_size / common;
    const int right_unit = left_size / common;
    const int maximum = min({
        6 / left_unit,
        6 / right_unit,
        remainder[left] / left_unit,
        remainder[right] / right_unit,
        right_size / left_unit,
        left_size / right_unit,
    });
    vector<pair<int, int>> output{{0, 0}};
    for (int multiplier = 1; multiplier <= maximum; ++multiplier) {
        const int left_value = left_unit * multiplier;
        const int right_value = right_unit * multiplier;
        const long long left_pairs =
            1LL * left_size * left_value * (left_value - 1);
        const long long right_capacity =
            1LL * right_size * (right_size - 1);
        const long long right_pairs =
            1LL * right_size * right_value * (right_value - 1);
        const long long left_capacity =
            1LL * left_size * (left_size - 1);
        if (left_pairs <= right_capacity && right_pairs <= left_capacity) {
            output.push_back({left_value, right_value});
        }
    }
    return output;
}

struct TriangleDelta {
    int first;
    int second;
    int third;
    int value;
};

void assign_pair(
    int left,
    int right,
    int left_value,
    int right_value,
    vector<TriangleDelta>& deltas
) {
    quotient[left][right] = left_value;
    quotient[right][left] = right_value;
    remainder[left] -= left_value;
    remainder[right] -= right_value;
    pair_product_sum += left_value * right_value;

    for (int third = 0; third < cell_count; ++third) {
        if (third == left || third == right) continue;
        if (quotient[left][third] < 0 || quotient[right][third] < 0) continue;
        const int value =
            quotient[left][right]
            * quotient[right][third]
            * quotient[third][left];
        if (value != 0) {
            triangle_sum[left] += value;
            triangle_sum[right] += value;
            triangle_sum[third] += value;
            deltas.push_back({left, right, third, value});
        }
    }
}

void unassign_pair(
    int left,
    int right,
    int left_value,
    int right_value,
    const vector<TriangleDelta>& deltas
) {
    for (const auto& delta : deltas) {
        triangle_sum[delta.first] -= delta.value;
        triangle_sum[delta.second] -= delta.value;
        triangle_sum[delta.third] -= delta.value;
    }
    pair_product_sum -= left_value * right_value;
    remainder[left] += left_value;
    remainder[right] += right_value;
    quotient[left][right] = -1;
    quotient[right][left] = -1;
}

int maximum_future_triangle_sum(int vertex) {
    long long maximum = triangle_sum[vertex];
    for (int left = 0; left < cell_count; ++left) {
        if (left == vertex || quotient[vertex][left] <= 0) continue;
        for (int right = left + 1; right < cell_count; ++right) {
            if (right == vertex || quotient[vertex][right] <= 0) continue;
            if (quotient[left][right] >= 0) continue;
            int best = 0;
            for (const auto& option : pair_options(left, right)) {
                best = max(
                    best,
                    quotient[vertex][left]
                    * option.first
                    * quotient[right][vertex]
                );
            }
            maximum += best;
        }
    }
    return static_cast<int>(maximum);
}

bool is_connected() {
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

bool satisfies_cubic_identity() {
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

bool satisfies_radius_two_inequalities() {
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

void process_row(int row);

void assign_row_edges(int row, const vector<int>& columns, int position) {
    ++search_nodes;
    if (position == static_cast<int>(columns.size())) {
        if (remainder[row] != 0) return;

        int diagonal_square = 0;
        for (int column = 0; column < cell_count; ++column) {
            if (column != row) {
                diagonal_square +=
                    quotient[row][column] * quotient[column][row];
            }
        }
        if (diagonal_square > sizes[row] + 5) return;
        const int target = 5 * sizes[row] + 8 - 2 * diagonal_square;
        if (target < 0 || target % 2 != 0) return;
        target_triangle_sum[row] = target / 2;
        if (triangle_sum[row] > target_triangle_sum[row]) return;
        if (maximum_future_triangle_sum(row) < target_triangle_sum[row]) return;
        if (pair_product_sum > 39) return;

        if (row == cell_count - 1) {
            ++complete_assignments;
            if (pair_product_sum != 39) return;
            if (any_of(
                    remainder.begin(),
                    remainder.end(),
                    [](int value) { return value != 0; }
                )) {
                return;
            }
            if (triangle_sum != target_triangle_sum) return;
            if (!is_connected()) return;
            if (!satisfies_cubic_identity()) return;
            if (!satisfies_radius_two_inequalities()) return;
            solutions.push_back({sizes, quotient});
            return;
        }

        process_row(row + 1);
        return;
    }

    const int column = columns[position];
    const auto options = pair_options(row, column);

    int minimum_left = 0;
    if (position > 0) {
        const int previous = columns[position - 1];
        bool interchangeable = sizes[column] == sizes[previous];
        if (interchangeable) {
            for (int earlier = 0; earlier < row; ++earlier) {
                if (quotient[earlier][column]
                    != quotient[earlier][previous]) {
                    interchangeable = false;
                }
            }
        }
        if (interchangeable) minimum_left = quotient[row][previous];
    }

    for (const auto& option : options) {
        const int left_value = option.first;
        const int right_value = option.second;
        if (left_value < minimum_left) continue;
        if (left_value > remainder[row]) continue;
        if (right_value > remainder[column]) continue;

        int maximum_remaining = 0;
        for (int next = position + 1;
             next < static_cast<int>(columns.size());
             ++next) {
            int local_maximum = 0;
            for (const auto& future : pair_options(row, columns[next])) {
                if (future.second <= remainder[columns[next]]) {
                    local_maximum = max(local_maximum, future.first);
                }
            }
            maximum_remaining += local_maximum;
        }
        if (remainder[row] - left_value > maximum_remaining) continue;

        vector<TriangleDelta> deltas;
        assign_pair(
            row,
            column,
            left_value,
            right_value,
            deltas
        );
        bool valid = true;
        for (int earlier = 0; earlier <= row; ++earlier) {
            if (target_triangle_sum[earlier] >= 0
                && triangle_sum[earlier] > target_triangle_sum[earlier]) {
                valid = false;
            }
        }
        if (valid) assign_row_edges(row, columns, position + 1);
        unassign_pair(
            row,
            column,
            left_value,
            right_value,
            deltas
        );
    }
}

void process_row(int row) {
    int fixed = 0;
    for (int column = 0; column < row; ++column) {
        fixed += quotient[row][column];
    }
    remainder[row] = 6 - fixed;
    if (remainder[row] < 0) return;

    vector<int> columns;
    for (int column = row + 1; column < cell_count; ++column) {
        columns.push_back(column);
    }
    assign_row_edges(row, columns, 0);
}

int main() {
    vector<vector<int>> partitions;
    vector<int> current;
    generate_partitions(50, cell_count, 1, current, partitions);

    for (const auto& candidate_sizes : partitions) {
        // The diagonal identity for a zero-diagonal quotient forces every cell
        // size to be even. This reduces 16,928 partitions to 164.
        if (any_of(
                candidate_sizes.begin(),
                candidate_sizes.end(),
                [](int value) { return value % 2 != 0; }
            )) {
            continue;
        }

        sizes = candidate_sizes;
        quotient.assign(
            cell_count,
            vector<int>(cell_count, -1)
        );
        for (int index = 0; index < cell_count; ++index) {
            quotient[index][index] = 0;
        }
        remainder.assign(cell_count, 6);
        target_triangle_sum.assign(cell_count, -1);
        triangle_sum.assign(cell_count, 0);
        pair_product_sum = 0;
        process_row(0);
    }

    cout << "solutions " << solutions.size()
         << " nodes " << search_nodes
         << " leaves " << complete_assignments
         << "\n";
    return solutions.empty() ? 0 : 1;
}
