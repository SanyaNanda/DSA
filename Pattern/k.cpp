// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;

// Function to count K-length
// strings from first N alphabets
void waysToArrangeKLengthStrings(
	int N, int K)
{
	// To keep track of column sum in dp
	int column_sum[N + 1] = { 0 }, i, j;

	// Auxiliary 2d dp array
	int dp[K + 1][N + 1] = { 0 };

	// Initialize dp[0][i] = 1 and
	// update the column_sum
	for (i = 0; i <= N; i++) {
		dp[0][i] = 1;
		column_sum[i] = 1;
	}

	// Iterate for K times
	for (i = 1; i <= K; i++) {

		// Iterate for N times
		for (j = 1; j <= N; j++) {

			// dp[i][j]: Stores the number
			// of ways to form i-length
			// strings consisting of j letters
			dp[i][j] += column_sum[j - 1];

			// Update the column_sum
			column_sum[j] += dp[i][j];
		}
	}

	// Print number of ways to arrange
	// K-length strings with N alphabets
	cout << dp[K][N];
}

// Driver Code
int main()
{
	// Given N and K
	int N = 33, K = 4;

	// Function Call
	waysToArrangeKLengthStrings(N, K);

	return 0;
}
