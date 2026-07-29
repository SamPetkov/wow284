#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using i128 = __int128_t;

long long bareiss_det(const vector<vector<int>>& input, int mask) {
    vector<int> idx;
    for (int i = 0; i < (int)input.size(); ++i) if ((mask >> i) & 1) idx.push_back(i);
    int n = (int)idx.size();
    if (!n) return 1;
    vector<vector<long long>> a(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) a[i][j] = input[idx[i]][idx[j]];
    long long sign = 1, previous = 1;
    for (int k = 0; k < n - 1; ++k) {
        int pivot_row = k;
        while (pivot_row < n && a[pivot_row][k] == 0) ++pivot_row;
        if (pivot_row == n) return 0;
        if (pivot_row != k) { swap(a[pivot_row], a[k]); sign = -sign; }
        long long pivot = a[k][k];
        for (int i = k + 1; i < n; ++i) for (int j = k + 1; j < n; ++j) {
            i128 numerator = (i128)a[i][j] * pivot - (i128)a[i][k] * a[k][j];
            if (k) { assert(numerator % previous == 0); numerator /= previous; }
            a[i][j] = (long long)numerator;
        }
        previous = pivot;
        if (!previous) return 0;
    }
    return sign * a[n - 1][n - 1];
}

bool psd_all_principal_minors(const vector<vector<int>>& matrix) {
    int n = (int)matrix.size();
    for (int mask = 1; mask < (1 << n); ++mask) if (bareiss_det(matrix, mask) < 0) return false;
    return true;
}

array<pair<int,int>,10> pair_edges() {
    array<pair<int,int>,10> edges{}; int t = 0;
    for (int i = 0; i < 5; ++i) for (int j = i + 1; j < 5; ++j) edges[t++] = {i,j};
    return edges;
}
const auto PEDGES = pair_edges();
vector<array<int,10>> plus_labels;
int labels_work[10] = {}, vertex_sums[5] = {};

void generate_plus_labels(int position) {
    if (position == 10) {
        for (int value : vertex_sums) if (value < 1 || value > 3) return;
        array<int,10> item{}; copy(labels_work, labels_work + 10, item.begin()); plus_labels.push_back(item); return;
    }
    auto [left,right] = PEDGES[position];
    for (int value = -2; value <= 2; ++value) {
        labels_work[position] = value; vertex_sums[left] += value; vertex_sums[right] += value;
        bool feasible = true;
        for (int vertex : {left,right}) {
            int remaining = 0;
            for (int edge = position + 1; edge < 10; ++edge)
                if (PEDGES[edge].first == vertex || PEDGES[edge].second == vertex) ++remaining;
            if (vertex_sums[vertex] - 2 * remaining > 3 || vertex_sums[vertex] + 2 * remaining < 1) feasible = false;
        }
        if (feasible) generate_plus_labels(position + 1);
        vertex_sums[left] -= value; vertex_sums[right] -= value;
    }
}

vector<array<int,100>> signed_ten_outputs;
void enumerate_minus(const array<int,10>& plus, const array<int,5>& matching, int position, array<int,10>& minus) {
    if (position < 10) {
        int value = plus[position];
        if (abs(value) == 2) { minus[position] = 0; enumerate_minus(plus, matching, position + 1, minus); }
        else if (abs(value) == 1) for (int choice : {-1,1}) { minus[position] = choice; enumerate_minus(plus, matching, position + 1, minus); }
        else for (int choice : {-2,0,2}) { minus[position] = choice; enumerate_minus(plus, matching, position + 1, minus); }
        return;
    }
    vector<vector<int>> minus_gram(5, vector<int>(5));
    for (int i = 0; i < 5; ++i) minus_gram[i][i] = 2 - matching[i];
    for (int edge = 0; edge < 10; ++edge) {
        auto [i,j] = PEDGES[edge]; minus_gram[i][j] = minus_gram[j][i] = minus[edge];
    }
    if (!psd_all_principal_minors(minus_gram)) return;

    array<int,100> signed_matrix{};
    auto set_symmetric = [&](int i, int j, int value) { signed_matrix[10*i+j] = signed_matrix[10*j+i] = value; };
    for (int i = 0; i < 5; ++i) set_symmetric(2*i, 2*i+1, matching[i]);
    for (int edge = 0; edge < 10; ++edge) {
        auto [i,j] = PEDGES[edge]; int same = (plus[edge] + minus[edge]) / 2; int cross = (plus[edge] - minus[edge]) / 2;
        set_symmetric(2*i,2*j,same); set_symmetric(2*i+1,2*j+1,same);
        set_symmetric(2*i,2*j+1,cross); set_symmetric(2*i+1,2*j,cross);
    }
    vector<int> seen(10); queue<int> q; seen[0] = 1; q.push(0);
    while (!q.empty()) { int u=q.front(); q.pop(); for(int v=0;v<10;++v) if(signed_matrix[10*u+v] && !seen[v]) seen[v]=1,q.push(v); }
    if (count(seen.begin(),seen.end(),1) != 10) return;
    signed_ten_outputs.push_back(signed_matrix);
}

void audit_signed_ten() {
    generate_plus_labels(0);
    assert(plus_labels.size() == 57464);
    long long plus_psd = 0;
    for (const auto& plus : plus_labels) {
        array<int,5> sums{}, matching{}; vector<vector<int>> plus_gram(5, vector<int>(5));
        for (int edge=0; edge<10; ++edge) { auto [i,j]=PEDGES[edge]; plus_gram[i][j]=plus_gram[j][i]=plus[edge]; sums[i]+=plus[edge]; sums[j]+=plus[edge]; }
        for(int i=0;i<5;++i){matching[i]=2-sums[i]; plus_gram[i][i]=matching[i]+2;}
        if(!psd_all_principal_minors(plus_gram)) continue;
        ++plus_psd; array<int,10> minus{}; enumerate_minus(plus, matching, 0, minus);
    }
    assert(plus_psd == 632); assert(signed_ten_outputs.size() == 1152);
    map<int,int> intersection_counts;
    for(const auto& matrix:signed_ten_outputs){
        int intersection=0; vector<int> degree(10); bool negative=false;
        for(int i=0;i<10;++i)for(int j=i+1;j<10;++j){int value=matrix[10*i+j]; if(value<0)negative=true; if(value){degree[i]++;degree[j]++;}}
        assert(!negative); for(int value:degree) assert(value==2);
        for(int pair=0;pair<5;++pair) intersection += matrix[10*(2*pair)+(2*pair+1)] == 1;
        intersection_counts[intersection]++;
    }
    { map<int,int> expected{{0,192},{2,960}}; assert(intersection_counts == expected); }
    cout << "SIGNED10 57464 632 1152 192 960\n";
}

array<int,10> cycle_row_shift(const array<int,10>& row, int direction) {
    array<int,10> result{};
    for(int j=0;j<10;++j) result[j] = row[(j-direction+10)%10];
    return result;
}

vector<array<int,100>> generate_cycle_intertwiners() {
    vector<array<int,100>> output;
    vector<array<int,10>> weight_two_rows;
    for(int a=0;a<10;++a)for(int b=a+1;b<10;++b){array<int,10> row{};row[a]=row[b]=1;weight_two_rows.push_back(row);}
    for(const auto& row0:weight_two_rows) for(const auto& row1:weight_two_rows) {
        array<array<int,10>,10> rows{}; rows[0]=row0; rows[1]=row1; bool valid=true;
        for(int i=1;i<9 && valid;++i){
            for(int j=0;j<10;++j){int value=rows[i][(j+9)%10]+rows[i][(j+1)%10]-rows[i-1][j]; if(value<0||value>1){valid=false;break;} rows[i+1][j]=value;}
            if(valid && accumulate(rows[i+1].begin(),rows[i+1].end(),0)!=2) valid=false;
        }
        if(!valid) continue;
        // periodic recurrence equations at rows 9 and 0
        for(int j=0;j<10;++j){
            if(rows[9][(j+9)%10]+rows[9][(j+1)%10]-rows[8][j] != rows[0][j]) valid=false;
            if(rows[0][(j+9)%10]+rows[0][(j+1)%10]-rows[9][j] != rows[1][j]) valid=false;
        }
        if(!valid) continue;
        for(int j=0;j<10;++j){int sum=0;for(int i=0;i<10;++i)sum+=rows[i][j];if(sum!=2)valid=false;}
        if(!valid) continue;
        array<int,100> matrix{};for(int i=0;i<10;++i)for(int j=0;j<10;++j)matrix[10*i+j]=rows[i][j];output.push_back(matrix);
    }
    sort(output.begin(),output.end()); output.erase(unique(output.begin(),output.end()),output.end());
    return output;
}

vector<array<int,10>> dihedral_permutations() {
    vector<array<int,10>> output;
    for(int shift=0;shift<10;++shift) for(int reflection=0;reflection<2;++reflection){array<int,10> p{};for(int i=0;i<10;++i)p[i]=(reflection?shift-i:shift+i)+20,p[i]%=10;output.push_back(p);}return output;
}

string rectangular_key(const array<int,100>& matrix,const array<int,10>& rows,const array<int,10>& columns){string key;key.reserve(100);for(int i=0;i<10;++i)for(int j=0;j<10;++j)key.push_back(char('0'+matrix[10*rows[i]+columns[j]]));return key;}

void audit_cycle_intertwiners(){
    auto matrices=generate_cycle_intertwiners(); assert(matrices.size()==140); auto perms=dihedral_permutations(); map<string,array<int,100>> reps;
    for(const auto& matrix:matrices){string best(100,'2');for(const auto& p:perms)for(const auto& q:perms)best=min(best,rectangular_key(matrix,p,q));reps.emplace(best,matrix);}
    assert(reps.size()==6);map<int,int> distribution;
    for(const auto& [key,matrix]:reps){vector<vector<int>> adj(20);for(int i=0;i<10;++i)for(int j=0;j<10;++j)if(matrix[10*i+j])adj[i].push_back(10+j),adj[10+j].push_back(i);vector<int>seen(20);int components=0;for(int s=0;s<20;++s)if(!seen[s]){components++;queue<int>q;q.push(s);seen[s]=1;while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(!seen[v])seen[v]=1,q.push(v);}}distribution[components]++;cout<<"LREP ";for(char c:key)cout<<c;cout<<"\n";}
    { map<int,int> expected{{1,2},{2,2},{5,2}}; assert(distribution==expected); } cout<<"LCOUNT 140 6 2 2 2\n";
}

int main(){audit_signed_ten();audit_cycle_intertwiners();cout<<"INDEPENDENT_CPP_PASS\n";}
