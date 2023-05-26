#include <stdio.h>
#include<stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#pragma warning(disable:4996)
#define MAX 101 //최대 글자수

typedef struct node {
	struct node* link;
	char letter;
}node;

typedef struct Stack {
	struct node* top;
	int size;
}Stack;

Stack* init_stack() {
	Stack* new_stack = (Stack*)malloc(sizeof(Stack));
	new_stack->top = NULL;
	new_stack->size = 0;

	return new_stack;
}

void push(Stack* s, char ch) {
	node* new_node = (node*)malloc(sizeof(node));
	if (s->size == 0) {
		new_node->link = NULL;
	}
	else {
		new_node->link = s->top;
	}
	new_node->letter = ch;
	s->top = new_node;
	(s->size)++;
}

char pop(Stack* s) {
	if (s->size == 1) {
		char pop_item = s->top->letter;
		free(s->top);
		s->top = NULL;
		(s->size)--;
		return pop_item;
	}
	else {
		node* temp = s->top;
		char pop_item = temp->letter;
		s->top = temp->link;
		free(temp);
		(s->size)--;
		return pop_item;
	}

}



int palindrome(char in_str[]) {
	Stack* s;
	int i;
	char ch, chs;
	int len = strlen(in_str);
	// 스택을 초기화하라
	s = init_stack();
	for (i = 0; i < len; i++) {
		ch = in_str[i];
		// 만약 ch가 스페이스거나 구두점이면
		if (ch == ' ' || ch == '.') continue;
		ch = tolower(ch); // ch를 소문자로 변경
		push(s, ch); // 스택에 삽입한다.
	}
	for (i = 0; i < len; i++) {
		ch = in_str[i];
		// 만약 ch가 스페이스거나 구두점이면
		if (ch == ' ' || ch == '.') continue;
		ch = tolower(ch); // ch를 소문자로 변경  // ctype.h 헤더파일 사용
		chs = pop(s); // 스택에서 문자를 꺼낸다
		if (ch != chs) {
			free(s);
			return false; // 실패 // stdbool.h 헤더파일 사용
		}
	}
	free(s);
	return true; // 성공
}
int main() {
	char sentence[MAX];
	fgets(sentence, MAX, stdin);
	size_t len = strlen(sentence);
	if (len > 0 && sentence[len - 1] == '\n') {
		sentence[len - 1] = '\0';
	}
	bool result = palindrome(sentence);
	printf("%d", result);
}
