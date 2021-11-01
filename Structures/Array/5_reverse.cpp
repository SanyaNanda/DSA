// importing required packages
#include <iostream>
#include<cmath>
using namespace std;

void reverse (int values[], int size){
    int temp = 0;
    // pivot: round((size/2) - 1)

    // reversing the array
    for ( int i = 0; i <= round((size/2) - 1); i++ ){
        temp = values[i];
        values[i] = values[size - i - 1];
        values[size - i -1] = temp;
    }
}

// printing an array
void print(int values[], int size){
    for ( int i = 0; i < size; i++ ){
        cout << values[i] << " ";
    }
    cout << endl;
}

int main (){
    // taking user input for the array
    int s;
    cout << "Enter the size of the array: ";
    cin >> s;
    int values[ s ];
    for ( int i = 0; i < s; i++ ){
        cout << "Enter value " << i << ": ";
        cin >> values[ i ];
    }

    // reversing the array
    print(values, s);
    reverse(values, s);
    print(values, s);
}