#include <stdio.h> 
#include <stdlib.h> 
#include "Basic_operations.h"
int main() 
{ 
	node* head = NULL; 
	node* second = NULL; 
	node* third = NULL;
	node* fourth = NULL;
	node* fifth = NULL;
	 
	head = (node*)malloc(sizeof(node)); 
	second = (node*)malloc(sizeof(node)); 
	third = (node*)malloc(sizeof(node));
	fourth = (node*)malloc(sizeof(node));
	fifth = (node*)malloc(sizeof(node));
	
	head->data = 10; 
	head->next = second; 
	second->data = 20; 
	second->next = third; 
	third->data = 30; 
	third->next = fourth;
	fourth->data = 40;
	fourth->next=fifth;
	fifth->data= 50;
	fifth->next=NULL;
	printList(head);

	int a=0;
	do{
	printf("Menu\n");
	printf("1. Insertion\n");
	printf("2. Deletion\n");
	printf("3. Searching\n");
	printf("4. Display\n");
	printf("5. Quit\n");
	printf("Choose: \n");
	scanf("%d", &a);
	switch(a){
		case 1: {
			printf("Menu\n");
			printf("1. Add at starting\n");
			printf("2. Add in between\n");
			printf("3. Add in the end\n");
			printf("Choose: \n");
			int b;
			scanf("%d", &b);
			switch(b){
				case 1: {
					printf("Enter the number to be inserted\n");
					int n;
					scanf("%d", &n);
					push(&head,n);
					printList(head);
					break;
				}
				
				case 2: {
					printf("Enter the number to be inserted and its position\n");
					int n, m ;
					scanf("%d %d", &n, &m);
					node *temp = head;
					if(m!=1){
					for(int i = 1; i<n ; i++){
					temp = temp->next;
					}
					}
					insertAfter(temp,n);
					printList(head);
					break;
				}
				
				case 3: {
					printf("Enter the number to be inserted\n");
					int n;
					scanf("%d", &n);
					append(&head,n);
					printList(head);
					break;
				}
				
				default:
					printf("error\n");
					break;
				}
				
			}break;
		case 2:	{
			printf("Menu\n");
			printf("1. delete 1st node\n");
			printf("2. delete a node in between\n");
			printf("3. delete last node\n");
			printf("Choose: \n");
			int b;
			scanf("%d", &b);
			switch(b){
				case 1: {
					deleteNodePos(&head, 0);
					printList(head);
					break;
				}
				case 2: {
					printf("Enter the element to be deleted \n");
					int n;
					scanf("%d", &n);
					deleteNode(&head,n);
					printList(head);
					break;
				}
				case 3: {
					int n = count(head);
					n = n-1;
					deleteNodePos(&head, n);
					printList(head);
					break;
				}
				default:
					printf("error\n");
					break;
		}break;
		
		case 3:{
			printf("Enter the node to be searched\n");
			int n;
			scanf("%d", &n);
			search(head,n);
			break;
		}
		case 4:{
		printList(head);
		break;
		}
		case 5:{
		printf("exit");
		break;
		}
		
	default:
		printf("error\n");
		break;	
		}
		
	}
} while(a!=5);
}

