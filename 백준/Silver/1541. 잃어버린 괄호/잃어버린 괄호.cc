#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	int sum = 0, temp = 0, digit = 1;
	getline(cin, s);
	for (int i = s.length() - 1; i >= 0; i--)
	{
		if (s[s.length() - 1] == '-' || s[s.length() - 1] == '+' || s[0] == '-' || s[0] == '+')
			abort();
		if (s[i] == '-')
		{
			sum -= temp;
			temp = 0, digit = 1;
		}
		else if (s[i] == '+')
		{
			digit = 1;
			continue;
		}
		else
		{
			if (digit == 1)
				temp += s[i] - 48;
			else
			{
				temp += (s[i] - 48) * digit;
			}
			digit *= 10;
		}
		if (i == 0)
			sum+=temp;
	}
	cout << sum << "\n";
	return 0;
}