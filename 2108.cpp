#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>
using namespace std;


int main() {
  int N;
  cin >> N;

  int sum=0;
  int numarr[N]={};
  int input=0;
  for(int i=0;i<N;i++){
      scanf("%d",&input);
      numarr[i] = input;
      sum += input;
  }//input

  //sort first
  sort(numarr, numarr+N);

  //avg
  double avg=0;
  avg  = sum / N;
  if(avg < 0){
      
  }
  printf("%1.f\n",avg);




  //middle
  int middle =0;
  middle = numarr[N/2];
  cout <<middle<< endl;

  //most
  int most = 0;
  int second=0;
  int caltmp=1;
  int idx=0;
  int sidx=0;
  for(int i=0;i<N;i++){
      for(int j =0;j<N;j++){
          if(numarr[j]==numarr[j+1]){
              caltmp ++;
              if(most < caltmp){
                  second = most;
                  sidx = j-1;
                  most = caltmp;
                  idx= j;
              }
          }
          else{

          }
      }
      caltmp =1;
  }
  if(most==second){
      idx = sidx;
  }
  cout <<fixed<<setprecision(0)<<numarr[idx]<< endl;

  //range
  int range =0;
  range = numarr[N-1] - numarr[0];
  cout << fixed << setprecision(0) << range <<endl;


  printf("ARRR: ");
for(int i=0;i<N;i++){
    printf("%d ",numarr[i]);
}
}


