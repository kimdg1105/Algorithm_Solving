#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool b_search(int arr[], int start, int end, int num)
{
    int mid = (start + end) / 2;
    if (start > end)
    {
        return false;
    }
    if (arr[mid] == num)
    {
        return true;
    }
    else if (arr[mid] > num)
    {
        return b_search(arr, start, mid - 1, num);
    }
    else
    {
        return b_search(arr, mid + 1, end, num);
    }
}

int main()
{
    int N, M;

    cin >> N;
    int arr1[100001] = {
        0,
    };
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        arr1[i] = num;
    }

    cin >> M;
    int arr2[100001] = {
        0,
    };
    for (int j = 0; j < M; j++)
    {
        int num;
        cin >> num;
        arr2[j] = num;
    }

    sort(arr1, arr1 + N);

    for (int i = 0; i < M; i++)
    {
        bool flag;
        flag = b_search(arr1, 0, N - 1, arr2[i]);
        cout << flag << '\n';
    }
}