#include <stdio.h>

int main(){
    int n;
    int input;
    int arr[12];
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 4;
    scanf("%d",&n);
    for(int i=0;i<n;i++){

        scanf("%d",&input);
        for(int j=3;j<input;j++){
            arr[j] = arr[j-1]+arr[j-2]+arr[j-3];
        }
        printf("%d\n",arr[input-1]);
    }

    return 0;
}