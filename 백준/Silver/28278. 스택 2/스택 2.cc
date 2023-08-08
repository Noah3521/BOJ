#include <stdio.h>
#include <stdlib.h>

int size = 0;

typedef struct stack {
	int data;
	struct stack* link;
}Stack;

Stack* getStack(int data) {
	++size;
	Stack* node = (Stack*)malloc(sizeof(Stack));
	node->data = data;
	node->link = NULL;
	return node;
}

void push(Stack** top, int data) {
	if (*top == NULL) {
		*top = getStack(data);
		return;
	}
	Stack* tmp = getStack(data);
	tmp->link = *top;
	*top = tmp;
}

int pop(Stack** top) {
	if (*top == NULL) {
		return -1;
	}
	int data = (*top)->data;
	Stack* tmp = *top;
	*top = (*top)->link;
	tmp = NULL;
	free(tmp);
	--size;
	return data;
}

int getSize() {
	return size;
}

int isEmpty() {
	return size == 0 ? 1 : 0;
}

int printTop(Stack* top) {
	if (top == NULL) {
		return -1;
	}
	return top->data;
}

void printStack(Stack* top) {
	if (top == NULL) {
		return;
	}
	printf("%d ", top->data);
	printStack(top->link);
}

int main() {
	Stack* top = NULL;
	
	int n = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		/*printStack(top);*/

		int menu = 0;
		int num = 0;
		scanf("%d", &menu);
		switch (menu) {
		case 1:
			scanf("%d", &num);
			push(&top, num);
			break;
		case 2:
			printf("%d\n", pop(&top));
			break;
		case 3:
			printf("%d\n", getSize());
			break;
		case 4:
			printf("%d\n", isEmpty());
			break;
		case 5:
			printf("%d\n", printTop(top));
			break;
		default:
			break;
		}
	}

	return 0;
}