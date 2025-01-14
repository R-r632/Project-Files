#include<bits/stdc++.h>
using namespace std;

long long solve(int N, vector<int> nums) {
    long long total_performance = 0;
    long long max_days = 0;
    
    for (int i = 0; i < N; i++) {
        if (total_performance + nums[i] >= 0) {
            total_performance += nums[i];
            max_days++;
        }
    }
    
    return max_days;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i_nums = 0; i_nums < N; i_nums++) {
        cin >> nums[i_nums]; 
    }
    
    long long out_;
    out_ = solve(N, nums);
    cout << out_;
} 
