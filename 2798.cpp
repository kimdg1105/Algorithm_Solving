#include <iostream>
#include <cstdio>
using namespace std;



int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int card[n];

    for(int i=0;i<n;i++){
        int num;
        scanf("%d",&num);
        card[i] = num;
    }

    int sum =0;
    int ans = 0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
                sum = card[i] + card[j] + card[k];
                if(sum == m){
                    ans = sum;
                }
                else if(sum <= m){
                    if(ans <= sum){
                        ans = sum;
                    }

                }
            }
        }
    }
     printf("%d",ans);



}