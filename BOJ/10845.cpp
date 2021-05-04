#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;


    int arr[100001];
    int top=0;
    int n=0;
    int popcnt=0;
    int size=0;
    char inst[200005];
void queue(){
    int pushnum;

    cin >> inst;
    int arrlen;

    if(strcmp(inst,"push")==0){
        cin >> pushnum;
        arr[size] = pushnum;
        top++;
        size++;
    }
    if(strcmp(inst,"pop")==0){
        if(size>0){
            if(arr[0]>0){
                printf("%d\n",arr[0]);
                size--;
                memmove(arr,arr+1,size*sizeof(int));
            }
        }
        else{
            cout << "-1" << endl;
            size = 0;
        }
    }
    if(strcmp(inst,"size")==0){
        cout << size <<endl;
    }
    if(strcmp(inst,"empty")==0){
        if(size<=0){
            printf("1\n");
        }
        else{
            printf("0\n");
        }
    }
    if(strcmp(inst,"front")==0){
        if(size>0){
            printf("%d\n",arr[0]);
        }
        else{
            printf("-1\n");
        }
    }

    if(strcmp(inst,"back")==0){
        if(arr[size-1]!=0){
            printf("%d\n",arr[size-1]);
        }
        else{
            printf("-1\n");
        }
    }

}

int main(){
    cin >> n;
    for(int i=0;i<n;i++){
        queue();
    }
}