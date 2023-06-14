#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int size = 0;

typedef struct Deque {
	int data;
	struct Deque* link;
}Deque;

Deque* getDeque(int data) {
	Deque* node = (Deque*)malloc(sizeof(Deque));
	node->data = data;
	node->link = NULL;
	size++;
	return node;
}

void push_front(Deque** front, Deque** rear, int data) {
	if (*front == NULL) {
		*front = getDeque(data);
		*rear = *front;
		return;
	}
	Deque* tmp = getDeque(data);
	(*front)->link = tmp;
	*front = (*front)->link;
}

void push_rear(Deque** front, Deque** rear, int data) {
	if (*rear == NULL) {
		*rear = getDeque(data);
		*front = *rear;
		return;
	}
	Deque* tmp = getDeque(data);
	tmp->link = *rear;
	*rear = tmp;
}

void printDeque(Deque* rear) {
	while (rear != NULL) {
		printf("%d -> ", rear->data);
		rear = rear->link;
	}
	printf("\b\b\b  \n");
}

Deque* findBeforeFront(Deque* front, Deque* rear) {
	if (rear == front) {
		return NULL;
	}
	else if (rear->link == front) {
		return rear;
	}
	return findBeforeFront(front, rear->link);
}

int pop_front(Deque** front, Deque** rear) {
	if (*front == NULL || *rear==NULL) {
		return -1;
	}

	int data = (*front)->data;


	*front = findBeforeFront(*front, *rear);
	if (*front == NULL) {
		*front = NULL;
		*rear = NULL;
		size--;
		return data;
	}
	/*printf("동적할당 해제할 덱의 데이터 : %d\n", (*front)->link->data);*/
	(*front)->link = NULL;
	free((*front)->link);
	size--;
	if (*front == NULL) {
		*rear = NULL;
	}
	return data;
}

int pop_rear(Deque** front, Deque** rear) {
	if (*front == NULL || *rear == NULL) {
		return -1;
	}

	int data = (*rear)->data;

	Deque* tmp = (*rear)->link;
	*rear = (*rear)->link;
	tmp = NULL;
	free(tmp);
	size--;
	if (*rear == NULL) {
		*front = NULL;
	}
	return data;
}

int getSize() {
	return size;
}

int isEmpty() {
	return size == 0 ? 1 : 0;
}

int	getData(Deque* node) {
	return node!=NULL ? node->data : -1;
}

int main(void) {
	Deque* front = NULL;
	Deque* rear = NULL;

	int N;
	scanf("%d", &N);

	char menu[20] = "";
	int data = 0;

	for (int i = 0; i < N; i++) {
		scanf("%s", menu);

		if (strcmp(menu, "push_front") == 0) {
			scanf("%d", &data);
			push_front(&front, &rear, data);
		}
		else if (strcmp(menu, "push_back") == 0) {
			scanf("%d", &data);
			push_rear(&front, &rear, data);
		}
		else if (strcmp(menu, "pop_front") == 0) {
			printf("%d\n", pop_front(&front, &rear));
		}
		else if (strcmp(menu, "pop_back") == 0) {
			printf("%d\n", pop_rear(&front, &rear));
		}
		else if (strcmp(menu, "size") == 0) {
			printf("%d\n", getSize());
		}
		else if (strcmp(menu, "empty") == 0) {
			printf("%d\n", isEmpty());
		}
		else if (strcmp(menu, "front") == 0) {
			printf("%d\n", getData(front));
		}
		else if (strcmp(menu, "back") == 0) {
			printf("%d\n", getData(rear));
		}

		//printf("현재 덱 : ");
		//printDeque(rear);
		//printf("현재 front : %d\n", getData(front));
		//printf("현재 rear : %d\n\n\n", getData(rear));
	}

	return 0;
}