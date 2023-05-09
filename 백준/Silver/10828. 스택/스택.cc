#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack {
	int data;
	struct stack* link;
}Stack;

Stack* getStack(int n)
{
	Stack* node = (Stack*)malloc(sizeof(Stack));
	node->data = n;
	node->link = NULL;
	return node;
}

int count = 0;

void push(Stack** top, int n)
{
	Stack* tmp = *top;
	*top = getStack(n);
	(*top)->link = tmp;
	count++;
}

void top1(Stack* top)
{
	if (top == NULL)
	{
		printf("%d\n", -1);
		return;
	}
	printf("%d\n", top->data);
}

void pop(Stack** top)
{
	if (*top == NULL)
	{
		printf("%d\n", -1);
		return;
	}

	int data = 0;
	Stack* tmp = *top;
	data = (*top)->data;
	(*top) = tmp->link;
	free(tmp);
	count--;
	printf("%d\n", data);
}

void empty(Stack* top)
{
	if (top == NULL)
		printf("%d\n", 1);
	else printf("%d\n", 0);
}

int main(void)
{
	Stack* top = NULL;
	char menu[6] = "";
	int remit = 0;
	scanf("%d", &remit);

	for (int i = 0; i < remit; i++)
	{
		scanf("%s", menu);
		if (strcmp(menu, "push") == 0)
		{
			int n = 0;
			scanf("%d", &n);
			push(&top, n);
		}

		else if (strcmp(menu, "pop") == 0)
			pop(&top);

		else if (strcmp(menu, "top") == 0)
			top1(top);

		else if (strcmp(menu, "size") == 0)
			printf("%d\n", count);

		else if (strcmp(menu, "empty") == 0)
			empty(top);

	}
	return 0;
}