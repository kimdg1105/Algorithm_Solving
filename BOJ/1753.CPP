#include <iostream>
using namespace std;
int INF = 10000000;

// bool visit[V]; //방문 노드
// int dist[V]; // 최소거리


// int getsmallidx(){
//     int min = INF;
//     int index = 0;
//     for(int i=0;i<V;i++){
//         if(dist[i] < min && !visit[i]){
//             min = d[i];
//             index = i;
//         }
//     }
//     return index;
// }


int main(){
    int V,E;
    cin >> V >> E;
    //V:정점의 개수 E: 간선의 개수
    int start;
    cin >> start;//시작점
    int arr[V][V]={};

    for(int i=0;i<V;i++){
        for(int j=0;i<V;j++){
            arr[i][j] = INF;
            if(i==j){
                arr[i][j] = 0;
            }
        }
    }

    for(int q=0;q<E;q++){
        int a,b,w;
        //a > b 의 가중치
        cin >> a >> b >> w;
        arr[a][b] = w;
    }


    for(int i=0;i<V;i++){
        for(int j=0;i<V;j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    //전체그래프 초기화


}