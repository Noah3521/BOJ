#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack {
    int data;
    struct stack* link;
}Stack;

Stack* getStack(int n) {
    Stack* node = (Stack*)malloc(sizeof(Stack));
    node->data = n;
    node->link = NULL;
    return node;
}

int size = 0;

void push(Stack** top, int n) {
    Stack* tmp = *top;
    *top = getStack(n);
    (*top)->link = tmp;
    //printf("%d추가\n", n);
    size++;
}

void pop(Stack** top) {
    if((*top)==NULL){
        printf("-1\n");
        return;
    }
    int data = -1;
    Stack* tmp = *top;
    data = (*top)->data;
    *top = tmp->link;
    printf("%d\n",data);
    free(tmp);
    size--;
}


void high(Stack* top) {
    if(top==NULL){
        printf("-1\n");
        return;
    }
    printf("%d\n", top->data);
}

int main()
{
    /*
    push x
    pop
    size
    empty
    top
    */
    Stack* top = NULL;
    char menu[6] = "";
    int N = 0;
    scanf("%d", &N);
    
    for(int i=0;i<N;i++) {
    scanf("%s", menu);
    if(strcmp(menu, "push")==0){
        int tmp = 0;
        scanf("%d", &tmp);
        push(&top, tmp);
    }
    else if(strcmp(menu, "pop")==0){
        pop(&top);
    }
    else if(strcmp(menu, "top")==0) {
        high(top);
    }
    else if(strcmp(menu, "empty")==0) {
        top==NULL ? printf("1\n") : printf("0\n");
    }
    else if(strcmp(menu, "size")==0) {
        printf("%d\n",size);
    }
    }
    return 0;
}

