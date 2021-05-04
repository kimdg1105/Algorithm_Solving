
#include <cstdio>
#include <vector>
using namespace std;

bool visit[10];
vector <int> vec;
int n,m;



void bt(int cnt);

int main(){

    scanf("%d %d",&n,&m);
    bt(1);
}

void bt(int cnt){
    if(vec.size() == m){
        for(int i=0;i<m;i++){
            printf("%d ",vec[i]);
        }
        printf("\n");
        return;
    }

    for(int i=cnt;i<=n;i++){
        if(vec.size() < m){
            vec.push_back(i);

            bt(i+1);
            vec.pop_back();

        }
    }
}