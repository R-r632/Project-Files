#include <bits/stdc++.h>
using namespace std;

long long solve(int N, vector<int> nums) {
    long long maxDays = 0;
    long long performance = 0;
    for (int i = 0; i < N; ++i) {
        if (performance + nums[i] >= 0) {
            performance += nums[i];
            maxDays++;
        }
    }
    return maxDays;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    long long out_;
    out_ = solve(N, nums);
    cout << out_;
    
    return 0;
}
