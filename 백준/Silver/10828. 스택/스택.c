#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<string.h>
#pragma warning(disable:4996)
#define SIZE 12

typedef struct node {
	int data;
	struct node* link;
}node;

typedef struct stack {
	node* top;
	int size;
}stack;

void initStack(stack* s) {
	s->size = 0;
	s->top = NULL;
}

void empty(stack* s) {
	if (s->size == 0) {
		printf("1\n");
	}
	else {
		printf("0\n");
	}
}

void size(stack* s) {
	printf("%d\n", s->size);
}

void push(stack* s, int data) {
	node* new_node = (node*)malloc(sizeof(node));
	new_node->data = data;


	if (s->size == 0) {
		s->top = new_node;
		new_node->link = NULL;
	}
	else {
		node* temp = s->top;
		s->top = new_node;
		new_node->link = temp;
	}
	s->size++;

}

void pop(stack* s) {
	if (s->size == 0) {
		printf("-1\n");
		return;
	}
	node* temp = s->top;
	s->top = s->top->link;
	printf("%d\n", temp->data);
	free(temp);
	s->size--;

	return;
}


void top(stack* s) {
	if (s->size == 0){
		printf("-1\n");
		return;
	}
	printf("%d\n", s->top->data);
}

int main()
{
	int R;
	stack s;
	initStack(&s);

	scanf("%d", &R);
	getchar();


	for (int i = 0; i < R; i++)
	{
		char buffer[SIZE];
		
		gets(buffer);


		if (memcmp("pop", buffer, 3) == 0) {
			pop(&s);
		}
		else if (memcmp("size", buffer, 4) == 0) {
			size(&s);
		}
		else if (memcmp("empty", buffer, 5) == 0) {
			empty(&s);
		}
		else if (memcmp("top", buffer, 3) == 0) {
			top(&s);
		}
		else if (memcmp("push", buffer, 4) == 0) {
			int data;
			char* ptr = strtok(buffer," ");  // push
			ptr = strtok(NULL, " ");  //int
			data = atoi(ptr);
			push(&s, data);
		}
	}
	return 0;
}