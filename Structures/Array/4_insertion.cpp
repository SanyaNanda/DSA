// importing required packages
#include <iostream>
using namespace std;

void insertion (int values[], int size, int pos, int item){
    // pushing all elements forward by 1 index in the array from the pos given as a parameter
    for ( int i = size; i >= pos; i-- ){
        values[i] = values[i-1];
    }
    // inserting the item at the given pos
    values[pos-1] = item;
}

// prints an array
void print(int values[], int size){
    for ( int i = 0; i < size; i++ ){
        cout << values[i] << " ";
    }
    cout << endl;
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
    print(values, size);

    // insertion of item at the specified pos
    int pos,item;
    cout << "Enter the position of insertion: ";
    cin >> pos;
    cout << "Enter the item to be inserted: ";
    cin >> item;
    insertion(values, size, pos, item);
    print(values, size+1);
}