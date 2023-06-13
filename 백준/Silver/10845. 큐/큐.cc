#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int size = 0;

typedef struct Queue {
	int data;
	struct Queue* link;
} Queue;

Queue* getQueue(int data) {
	Queue* node = (Queue*)malloc(sizeof(Queue));
	node->data = data;
	node->link = NULL;
	size++;
	return node;
}

void push(Queue** front, Queue** rear, int data) {
	if (*front == NULL) {
		*front = getQueue(data);
		*rear = *front;
		return;
	}
	Queue* tmp = getQueue(data);
	(*rear)->link = tmp;
	*rear = (*rear)->link;
}

int pop(Queue** front) {
	if (*front == NULL) {
		return -1;
	}
	int data = (*front)->data;
	Queue* tmp = *front;
	*front = (*front)->link;
	free(tmp);
	size--;
	return data;
}

int getFront(Queue* front) {
	return front != NULL ? front->data : -1;
}

int getBack(Queue* front, Queue* rear) {
	return front != NULL ? rear->data : -1;
}

int main() {
	Queue* front = NULL;
	Queue* rear = NULL;

	char menu[10] = "";
	unsigned int count = 0;

	scanf("%u", &count);
	while (count != 0) {
		scanf("%s", menu);
		if (strcmp(menu, "push") == 0) {
			int data;
			scanf("%d", &data);
			push(&front, &rear, data);
			// printf("%d삽입 완료\n", data);
		}
		else if (strcmp(menu, "pop") == 0) {
			printf("%d\n", pop(&front));
		}
		else if (strcmp(menu, "size") == 0) {
			printf("%d\n", size);
		}
		else if (strcmp(menu, "empty") == 0) {
			printf("%d\n", size == 0 ? 1 : 0);
		}
		else if (strcmp(menu, "front") == 0) {
			printf("%d\n", getFront(front));
		}
		else if (strcmp(menu, "back") == 0) {
			printf("%d\n", getBack(front, rear));
		}
		count--;
	}

	// 모든 노드 제거
	Queue* current = front;
	while (current != NULL) {
		Queue* next = current->link;
		free(current);
		current = next;
	}

	return 0;
}
	