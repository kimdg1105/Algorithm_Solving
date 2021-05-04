#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N,M;
    cin >> N >> M;
    vector <int> marr;
    for(int i=0;i<M;i++){
        int num;
        cin >> num;
        marr.push_back(num);
    }
    vector <int> ans;
    int len;
    len = marr.size();

    for(int i=0;i<len;i++){
        int mul = 1;
        while(1){
            int temp = marr[i]*mul;
            if(temp <= N){
                if(find(ans.begin(),ans.end(),temp) != ans.end()){

                }
                else{
                 ans.push_back(temp);
                }
            }
            else{
                break;
            }
            mul++;
        }
    }
    int total =0;
    for(int i=0;i<ans.size();i++){
        cout << ans[i] << "  ";
        total += ans[i];
    }

    cout << total;



}