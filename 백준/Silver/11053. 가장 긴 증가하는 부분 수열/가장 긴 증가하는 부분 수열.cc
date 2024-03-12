#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int dp[1001], series[1001];
	fill_n(dp, 1001, 1);
	int n, len = 0;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> series[i];
		for (int j = 1; j < i; j++)
		{
			if (series[i] > series[j])
				dp[i] = max(dp[i], dp[j] + 1);
		}
		len = max(len, dp[i]);
	}
	cout << len;
	return 0;
}