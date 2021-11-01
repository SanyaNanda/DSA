// importing required packages
#include <iostream>
using namespace std;

int avgArray (int values[], int size){
    int sum = 0;

    // summing all elements of the array
    for ( int i = 0; i < size; i++ ){
        sum += values[ i ];
    }
    // dividing the sum by the size of the array and returning the average
    return sum /size;
}

int main (){
    // taking user input for the values of the array
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int values[ size ];
    for ( int i = 0; i < size; i++ ){
        cout << "Enter value " << i << ": ";
        cin >> values[ i ];
    }

    // printing the average
    cout << avgArray( values, size ) << endl;
}