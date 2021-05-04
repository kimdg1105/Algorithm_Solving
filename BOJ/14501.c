#include <stdio.h>
int max(int a,int b){
    return a>b ? a:b;
}

int main(){
    int d[100000];
    int n=0;
    scanf("%d",&n);
    int t[n+1];
    int p[n+1];

    for(int i=1;i<=n;i++){
        scanf("%d %d",&t[i],&p[i]);
    }

    for(int j=1;j<=n;j++){
        if(j+t[j]<=n){
            d[j+t[j]] = max(d[j+t[j]],d[j]+p[j]);
        }
    }

}