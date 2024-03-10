#include <iostream>
using namespace std;
#define MAX 15

int pos[MAX];
int N, cnt = 0;

bool position_check(int col)
{
	for (int i = 0; i < col; i++)
		if (pos[col] == pos[i] || abs(pos[col] - pos[i]) == col - i)
			//pos[col]==pos[i]는 같은 라인에 있는지 확인
			//abs() == 는 대각선상에 있는지 확인
			return false;
	return true;
}

void NQueen(int col)
{
	if (col == N)
		cnt++;
	else
		for (int i = 0; i < N; i++)
		{
			pos[col] = i;
			if (position_check(col) == true)
				NQueen(col + 1);
		}
}

int main()
{
	cin >> N;
	NQueen(0);
	cout << cnt;
	return 0;
}