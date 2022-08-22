#include <stdio.h>
#include <stdlib.h>

struct node{
	int data;
	struct node* next;
};

struct node* head;

void Insert(int data){
	struct node* temp1=malloc(sizeof(struct node));
	temp1->data=data;
	if(head==NULL){
		temp1->next = head;
		head = temp1;
		return;
	}
	temp1->next = NULL;
	struct node* temp2 = head;
	while(temp2->next != NULL){
		temp2 = temp2->next;
	}
	temp1->next = temp2->next;
	temp2->next = temp1;
}

void Print(){
	if(head==NULL){
		printf("List is empty");
		return;
	}
	printf("List->");
	struct node* temp = head;
	while(temp!=NULL){
	    printf("%d->", temp->data);
		temp = temp->next;
	}
	printf("NULL\n");
}


void Delete(struct node *l, int target){
	struct node* temp = l->next;
    struct node* prev = l;

    while((temp->data!=target && temp!=NULL)){

        prev = temp;
        temp = temp->next;

    }

    prev->next = temp->next;
}

void fun_delete(struct node *l, int target)
{
int n=target;
struct node* temp1 = l;
if(head==NULL)
{
printf("\nThe List is empty...");
}
else{
// printf("\nEnter an element to delete from the List...");
// scanf("%d",&n);
if(l->data==n)
{
head=l->next;
free(l);
// printf("\nEntered element deleted from the List...");
}
else
{
temp1=l;
l=l->next;
while((l->data!=n) && (l!=NULL))
{
temp1=l;
l=l->next;
}
if(l->data==n)
{
temp1->next=l->next;
free(l);
// printf("\nEntered element deleted from the List...");
}
else
printf("\nThe Element is not in the List.");
}
}
}

void deleteNode(struct node **head_ref, int key) 
{ 
    struct node* temp = *head_ref, *prev;  
    if (temp != NULL && temp->data == key) 
    { 
        *head_ref = temp->next;   
        free(temp);               
        return; 
    } 
    if (temp == NULL){
        printf("list is empty");
        return; 
    }
    while (temp != NULL && temp->data != key) 
    { 
        prev = temp; 
        temp = temp->next; 
    } 
    if (temp == NULL){
        printf("list is empty");
        return; 
    }
    prev->next = temp->next; 
    free(temp);  
}

int main(){
	head = NULL;
	int n;
	scanf("%d", &n);
	int arr[n];
    int target;
    scanf("%d", &target);

	for(int i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	for(int i=0;i<n;i++){
		Insert(arr[i]);
	}
	// Print();
	// printf("After Deletion\n");
    
	// Delete(head, target);
    // fun_delete(head, target);
    // deleteNode(&head, target);	
}