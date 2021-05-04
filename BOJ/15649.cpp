
#include <cstdio>
#include <vector>
using namespace std;

bool visit[10];
vector <int> vec;
int n,m;



void bt(int cnt);

int main(){

    scanf("%d %d",&n,&m);
    bt(0);
}

void bt(int cnt){
    if(cnt == m){
        for(int i=0;i<cnt;i++){
            printf("%d ",vec[i]);
        }
        printf("\n");
        return;
    }

    for(int i=1;i<=n;i++){
        if(!visit[i]){
            vec.push_back(i);
            visit[i] = true;
            bt(cnt+1);
            vec.pop_back();
            visit[i] = false;

        }
    }
}