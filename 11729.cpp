#include <iostream>
#include <vector>
#include  <cstdio>
using namespace std;

vector <pair <int,int> > cnt;


void move(int n, int a,int b,int c){
    if(n==1){
        cnt.push_back(make_pair(a,c));
    }
    else{
        move(n-1,a,c,b);
        cnt.push_back(make_pair(a,c));
        move(n-1,b,a,c);
    }
}

int main(){
    int n;
    cin >> n;
    move(n,1,2,3);
    printf("%d\n",cnt.size());
    for(int i=0;i<cnt.size();i++){
       printf("%d %d\n",cnt[i].first,cnt[i].second);
    }


}