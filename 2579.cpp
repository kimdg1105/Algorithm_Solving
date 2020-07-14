#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int floor;
    cin >> floor;
    int score[floor+1] = {0};
    int dp[1000] = {0};
    dp[0] = 0;
    int step =1;
    for(int i=1;i<=floor;i++){
        cin >> score[i];
    }
    dp[1] = score[1];
    dp[2] = score[1] + score[2];

    for(int i=3;i<=floor;i++){
        dp[i] = max(score[i]+score[i-1]+dp[i-3],score[i]+dp[i-2]);
    }



    cout << dp[floor] << endl;
    return 0;

}