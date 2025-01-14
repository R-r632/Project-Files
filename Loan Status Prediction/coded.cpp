#include <bits/stdc++.h>
using namespace std;

long long solve(int N, vector<int> nums) {
    long long maxDays = 0;
    long long currentPerformance = 0;
    long long minPrefixSum = 0; // To track the minimum prefix sum

    for (int i = 0; i < N; ++i) {
        currentPerformance += nums[i];

        // Check if the current performance is valid
        if (currentPerformance - minPrefixSum >= 0) {
            maxDays++;
        } else {
            // Update the prefix sum to reset negative contributions
            minPrefixSum = currentPerformance;
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

    cout << solve(N, nums) << "\n";

    return 0;
}
