#include <iostream>
using namespace std;

int main()
{
	int n, cof;
	cin >> n;
	for (int i = n / 2; i < n; i++)
	{
		int temp = i;
		cof = i;
		while (temp > 0)
		{
			cof += temp % 10;
			temp /= 10;
		}
		if (cof == n)
		{
			cout << i << "\n";
			return 0;
		}
		cof = 0;
	}
	cout << "0\n";
	return 0;
}