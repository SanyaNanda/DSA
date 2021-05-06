#include <stdio.h> 
#include <stdlib.h> 

typedef struct Node { 
	int data; 
	struct Node* next; 
}node; 
void printList(node* n) 
{ 
    while (n != NULL) { 
        printf(" %d ", n->data); 
        n = n->next; 
    } 
} 

void push(node** head_ref, int new_data) 
{ 

	node* new_node = (node*) malloc(sizeof(node)); 
	new_node->data = new_data; 
	new_node->next = (*head_ref); 
	(*head_ref) = new_node; 
} 

void insertAfter(node* prev_node, int new_data) 
{ 
	
	if (prev_node == NULL) 
	{ 
	printf("the given previous node cannot be NULL");	 
	return; 
	} 
	node* new_node =(node*) malloc(sizeof(node)); 
	new_node->data = new_data; 
	new_node->next = prev_node->next; 
	prev_node->next = new_node; 
} 

void append(node** head_ref, int new_data) 
{ 
    
    node* new_node = (node*) malloc(sizeof(node)); 
    node *last = *head_ref;  
    new_node->data  = new_data; 
    new_node->next = NULL; 
    if (*head_ref == NULL) 
    { 
       *head_ref = new_node; 
       return; 
    }
    while (last->next != NULL) 
        last = last->next; 
    last->next = new_node; 
    return;     
} 

int count(node *head)
{
    int total = 0;
    node *current = head;
    do 
    {
        current = current->next;
        total++;
    } while (current != NULL);

    return total;
}
void deleteNodePos(node **head_ref, int position) 
{ 
   
   if (*head_ref == NULL) 
      return; 
  
    
   node* temp = *head_ref; 
    if (position == 0) 
    { 
        *head_ref = temp->next;   
        free(temp);               
        return; 
    } 
 
    for (int i=0; temp!=NULL && i<position-1; i++) 
         temp = temp->next; 

    if (temp == NULL || temp->next == NULL) 
         return; 

    node *next = temp->next->next; 
    free(temp->next);   
    temp->next = next;  
} 
void deleteNode(node **head_ref, int key) 
{ 
    
    node* temp = *head_ref, *prev;  
    if (temp != NULL && temp->data == key) 
    { 
        *head_ref = temp->next;   
        free(temp);               
        return; 
    } 
    while (temp != NULL && temp->data != key) 
    { 
        prev = temp; 
        temp = temp->next; 
    } 
    if (temp == NULL) return; 
    prev->next = temp->next; 
    free(temp);  
}

void search(node* head, int x) 
{ 
    node* current = head;
	int count=1,c=0;
    while (current != NULL) 
    { 
        if (current->data == x) {
	c=1;
	printf("Position of %d is %d\n",x,count);
	}
        current = current->next; 
	count++;
    } if(c==0) {printf("%d Not found", x);}
    
} 
