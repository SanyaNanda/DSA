#include <iostream>
using namespace std;
int main(){
    int n=5;
    for(int i=n;i>0;i--){
        for(int j=0;j<i;j++){
            cout<<j+1;
            cout<<" ";
        }
        cout<<endl;
    }
}

/* 
output: 

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

*/