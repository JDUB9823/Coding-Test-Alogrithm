#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n, cnt = 0;
	cin >> n;
	vector<pair<int, int>>p(n);
	for (int i = 0; i < n; i++)
		cin >> p[i].second >> p[i].first;
	sort(p.begin(), p.end());
	int endtime = 0;
	for (int i = 0; i < n; i++)
		if (endtime <= p[i].second)
		{
			endtime = p[i].first;
			cnt++;
		}
	cout << cnt << "\n";
	return 0;
}