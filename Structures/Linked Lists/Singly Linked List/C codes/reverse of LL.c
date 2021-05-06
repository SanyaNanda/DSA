#include <stdio.h> 
#include <stdlib.h> 
struct Node { 
	int data; 
	struct Node* next; 
}; 
void printList(struct Node* n) 
{ 
    while (n != NULL) { 
        printf(" %d ", n->data); 
        n = n->next; 
    } 
} 
static void reverse(struct Node** head_ref) 
{ 
    struct Node* prev = NULL; 
    struct Node* current = *head_ref; 
    struct Node* next = NULL; 
    while (current != NULL) { 
        
        next = current->next; 

        current->next = prev; 
        prev = current; 
        current = next; 
    } 
    *head_ref = prev; 
} 

int main() 
{ 
	struct Node* head = NULL; 
	struct Node* second = NULL; 
	struct Node* third = NULL;
	struct Node* fourth = NULL;
	struct Node* fifth = NULL;
	struct Node* sixth = NULL;
	struct Node* seven = NULL; 
 
	head = (struct Node*)malloc(sizeof(struct Node)); 
	second = (struct Node*)malloc(sizeof(struct Node)); 
	third = (struct Node*)malloc(sizeof(struct Node));
	fourth = (struct Node*)malloc(sizeof(struct Node));
	fifth = (struct Node*)malloc(sizeof(struct Node));
	sixth = (struct Node*)malloc(sizeof(struct Node)); 
	seven = (struct Node*)malloc(sizeof(struct Node));


	head->data = 1; 
	head->next = second; 
	second->data = 2; 
	second->next = third; 
	third->data = 3; 
	third->next = fourth;
	fourth->data = 4;
	fourth->next=fifth;
	fifth->data= 5;
	fifth->next=sixth;
	sixth->data=6;
	sixth->next=seven;
	seven->data=7;
	seven->next=NULL;
	printList(head);
	printf("\n");
	reverse(&head);
	printList(head);
	return 0;
}
