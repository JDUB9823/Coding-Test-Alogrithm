#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n, int one, int two, int three)
{
	if (n == 1)
		cout << one << " " << three << "\n";
	else
	{
		hanoi(n - 1, one, three, two);
		cout << one << " " << three << "\n";
		hanoi(n - 1, two, one, three);
	}
}

int main()
{
	int n, cnt = 0;
	cin >> n;
	cout << (int)pow(2, n) - 1 << "\n";
	hanoi(n, 1, 2, 3);
	return 0;
}