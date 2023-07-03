#include <stdio.h>
#include <stdlib.h>

typedef struct tree {
	int data;
	struct tree* left;
	struct tree* right;
}Tree;

Tree* getTree(int data) {
	Tree* node = (Tree*)malloc(sizeof(Tree));
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return node;
}

void insert(Tree** root, int data) {
	if (*root == NULL) {
		*root = getTree(data);
		return;
	}

	// data가 root보다 클 경우 -> right
	if ((*root)->data < data) {
		insert(&(*root)->right, data);
	}

	// data가 root보다 작을 경우 -> left
	if ((*root)->data > data) {
		insert(&(*root)->left, data);
	}
}

void preOrder(Tree* root) {
	if (root == NULL) {
		return;
	}
	printf("%d ", root->data);
	if (root->left) {
		preOrder(root->left);
	}
	if (root->right) {
		preOrder(root->right);
	}
}

void postOrder(Tree* root) {
	if (root == NULL) {
		return;
	}
	if (root->left) {
		postOrder(root->left);
	}
	if (root->right) {
		postOrder(root->right);
	}
	printf("%d\n", root->data);
}

int main(void) {
	Tree* root = NULL;
	int remit = 10001;
	int n;
	int count = 0;
	while (scanf("%d", &n) != EOF && count < remit) {
		count++;
		insert(&root, n);
	}

	//insert(&root, 50);
	//insert(&root, 30);
	//insert(&root, 24);
	//insert(&root, 5);
	//insert(&root, 28);
	//insert(&root, 45);
	//insert(&root, 98);
	//insert(&root, 52);
	//insert(&root, 60);

	//preOrder(root);
	//printf("\n\n");
	postOrder(root);

	return 0;
}