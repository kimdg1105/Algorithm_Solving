#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector <int> vec;

vector <int> dp1(int n, vector <int> vec);
vector <int> dp2(int n, vector <int> vec);

int main(){
    int N;
    cin >> N;
    for(int i=0;i<N;i++){
        int num;
        cin >> num;
        vec.push_back(num);
    }

    vector <int> r1;
    vector <int> r2;
    r1 = dp1(N,vec);
    r2 = dp2(N,vec);
    int ans = 0;
    for(int i=0;i<N;i++){
        int temp = r1[i]+r2[i]-1;

        ans = max(temp,ans);
    }

    cout << ans;
}

vector <int> dp1(int n, vector <int> vec){
    int len = vec.size();
    vector <int> dp(1001);
    int ans=0;
    for(int i=0;i<len;i++){
        dp[i] = 1;
        for(int j=0;j<i;j++){
            if(vec[i]>vec[j]){
                dp[i] = max(dp[i],dp[j]+1);
            }
        }
        ans = max(ans,dp[i]);
    }
    return dp;
}
vector <int> dp2(int n, vector <int> vec){
    int len = vec.size();
    vector <int> rdp(1001);
    int ans=0;
    for(int i=len-1;i>=0;i--){
        rdp[i] = 1;
        for(int j=len-1;j>i;j--){
            if(vec[i]>vec[j]){
                rdp[i] = max(rdp[i],rdp[j]+1);
            }
        }
        ans = max(ans,rdp[i]);
    }
    return rdp;
}