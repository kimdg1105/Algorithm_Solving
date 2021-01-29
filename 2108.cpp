#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main()
{
    int avg;         //산술평균
    int middle;      //중앙값
    int mostnum = 0; //최빈값
    int range;       //범위

    int N;
    cin >> N;

    //Setting
    int arr[N + 1];
    int cnt[10000];
    int sum = 0;
    for (int i = 0; i <= 8001; i++)
    {
        cnt[i] = 0;
    }

    //Input
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
        if (arr[i] >= 0)
        {
            cnt[4000 + arr[i]]++;
        }
        if (arr[i] < 0)
        {
            cnt[abs(arr[i]) - 1]++;
        }
        sum += arr[i];
    }

    //Avg

    cout << round(sum / (double)N) << endl;
    // TODO : 음수 반올림

    //Middle
    sort(arr, arr + N);
    cout << arr[N / 2] << endl;

    //mostnum
    int most = 0;
    for (int i = 0; i <= 8001; i++)
    {
        if (cnt[i] >= most)
        {
            most = cnt[i];
        }
    }

    int save1 = 0;
    int save2;
    int result = 0;
    int cntarr[10000];
    int idx = 0;
    for (int i = 0; i <= 8001; i++)
    {
        if (cnt[i] == most)
        {
            cntarr[idx] = i;
            idx++;
            cout << cntarr[idx] << " ";
        }
    }

    save1 = cntarr[0];
    save2 = cntarr[1];
    if (save1 <= 4000)
    {
        if (save2 < 4000)
        {
            result = -save1;
        }
        if (save2 > 4000)
        {
            result = save2 - 4000;
        }
    }
    if (save1 > 4000)
    {
        result = save1 - 4000;
    }

    cout << result << endl;

    //range
    range = abs(arr[N - 1] - arr[0]);
    cout << range << endl;
}