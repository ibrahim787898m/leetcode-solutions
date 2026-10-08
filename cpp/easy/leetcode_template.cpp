#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
	// Replace the signature and implementation for the selected problem.
	int solve(vector<int>& nums) {
		// TODO: implement the solution.
		return 0;
	}
};

// For local testing: input n followed by n integers.
// Remove main() before submitting to LeetCode, which provides its own test harness.
int main() {
	int n;
	if (!(cin >> n)) return 0;

	vector<int> nums(n);
	for (int& num : nums) cin >> num;

	Solution solution;
	cout << solution.solve(nums) << '\n';
	return 0;
}

// LeetCode version
// #include <bits/stdc++.h>
// using namespace std;

// class Solution {
//     public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         unordered_map<int, int> seen;

//         for (int i = 0; i < nums.size(); i++) {
//             int complement = target - nums[i];
//             if (seen.find(complement) != seen.end()) {
//                 return {seen[complement], i};
//             } else {
//                 seen[nums[i]] = i;
//             }
//         }
//         return {};
//     }
// };

// int main() {
//     Solution sol;
//     vector<int> nums = {2, 7, 11, 15};
//     int target = 9;

//     vector<int> res = sol.twoSum(nums, target);

//     cout << res[0] << " " << res[1] << endl;

//     return 0;
// }