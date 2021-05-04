#include <iostream>
#include <cstring>
#define MAX 101
using namespace std;

int arr[1001][1001];

void snail(int n) {
	int y = n / 2 + 1;
	int x = n / 2 + 1;
	arr[y][x] = 1;

	int stamp = 2;
	int move = 0;
	while ( 1 ) {

	
		move++;

		for (int i = 0; i < move; i++) {
			y = y - 1;
			arr[y][x] = stamp;
			stamp++;
			if (stamp > n * n) break;
		}
		if (stamp > n * n) break;

		
		for (int i = 0; i < move; i++) {
			x = x + 1;
			arr[y][x] = stamp;
			stamp++;
		}

	
		move++;

		
		for (int i = 0; i < move; i++) {
			y = y + 1;
			arr[y][x] = stamp;
			stamp++;
		}

	
		for (int i = 0; i < move; i++) {
			x = x - 1;
			arr[y][x] = stamp;
			stamp++;
		}
	}
}


void printSnailAndFindNumPoint(int find, int size)
{

    int findNumPointY, findNumPointX;

    for (int i = 1; i <= size; i++)
    {
        for (int j = 1; j <= size; j++)
        {
            cout << arr[i][j] << " ";
            if (arr[i][j] == find)
            {
                findNumPointY = i;
                findNumPointX = j;
            }
        }
        cout << "\n";
    }

    cout << findNumPointY << " " << findNumPointX << "\n";
}

int main()
{
    int N;
    cin >> N;
    int find;
    cin >> find;

   
    snail(N);
    printSnailAndFindNumPoint(find, N);
}