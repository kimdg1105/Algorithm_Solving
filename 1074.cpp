#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N, r, c;
    cin >> N >> r >> c;

    int max = pow(2, N) * pow(2, N) - 1;
    cout << max;
}