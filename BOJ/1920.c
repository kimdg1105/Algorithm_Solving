#include <stdio.h>

int main(){
    int n,m;
    scanf("%d",&n);
    int narr[n+1];
    for(int i=0;i<n;n++){
        scanf("%d ",&narr[i]);
    }
    scanf("%d",&m);
    int marr[m+1];
    for(int i=0;i<n;n++){
        scanf("%d ",&marr[i]);
    }

    int flag[1000] = {0,};
    for(int i=0;i<m;i++){
        for(int j=0;j<m;j++){
            if(marr[i]==narr[j]){
                flag[i] = 1;
            }
        }
    }

    for(int i=0;i<m;i++){
        printf("%d\n",flag[i]);
    }



    return 0;
}