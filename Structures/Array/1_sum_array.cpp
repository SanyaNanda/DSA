// importing required packages
#include <iostream>
using namespace std;

int sumArray (int values[], int size){
    int sum = 0;
    // adding values of each element of the array in a variable
    for ( int i = 0; i < size; i++ ){
        sum += values[ i ];
    }
    return sum;
}

int main (){
    // taking user input for the array
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int values[ size ];
    for ( int i = 0; i < size; i++ ){
        cout << "Enter value " << i << ": ";
        cin >> values[ i ];
    }
    // printing the sum of the elements of the array
    cout << sumArray( values, size ) << endl;
}