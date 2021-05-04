#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int n, tmp;
    double sum = 0;
    int max = 0;
    int index[2];
    double x;
    int x1;
    vector<int> v;
    vector<int> t;
    int checkarr[8001] = {0};
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());

    // 산술 평균
    for (int i = 0; i < n; i++)
    {
        sum += v[i];
        if (i != 0 && v[i] == v[i - 1])
        {
            t.push_back(i);
        }
        checkarr[4000 + v[i]]++;
    }

    x = double(sum) / double(n);
    x1 = int(round(x));
    printf("%d\n", x1);

    // 중앙값
    printf("%d\n", v[n / 2]);

    // 최빈값
    index[0] = v[0];
    index[1] = 0;

    for (int i = 0; i < 8001; i++)
    {
        if (checkarr[i] > max)
        {
            max = checkarr[i];
            index[0] = i - 4000;
            index[1] = 0;
        }
        else if (checkarr[i] == max)
        {
            if (index[1] == 0)
            {
                index[0] = i - 4000;
                index[1]++;
            }
        }
    }
    printf("%d\n", index[0]);

    // 범위

    printf("%d\n", v[n - 1] - v[0]);
    return 0;
}
