#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector < vector<int> > se;
    vector <pair<int,float> > cla;
    int T;
    cin >> T;
    int N;
    for(int i=0;i<T;i++){
        int num;
        cin >> num;
        for(int j=0;j<num;j++){
            int grad;
            float sco;
            cin >> grad >> sco;
            cla.push_back(make_pair(grad,sco));
        }
        float sum=0;
        int div = 0;
        for(int i=0;i<cla.size();i++){
            sum += cla[i].first * cla[i].second;
            div += cla[i].first;
        }
        cout.precision(2);
        cout << div << " " << sum/div << endl;
        cla.clear();

    }
}