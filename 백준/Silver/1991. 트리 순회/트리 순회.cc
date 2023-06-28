#include <stdio.h>
#include <stdlib.h>

typedef struct tree {
	char data;
	struct tree* left;
	struct tree* right;
}Tree;

Tree* getTree(char data) {
	Tree* node = (Tree*)malloc(sizeof(Tree));
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return node;
}

void insert(Tree** root, char rootData, char leftData, char rightData) {
	if (*root == NULL) {
		*root = getTree(rootData);
		(*root)->right = getTree(rightData);
		(*root)->left = getTree(leftData);
		return;
	}
	if ((*root)->data == rootData) {
		(*root)->left = getTree(leftData);
		(*root)->right = getTree(rightData);
		return;
	}
	if ((*root)->left) {
		insert(&(*root)->left, rootData, leftData, rightData);
	}
	if ((*root)->right) {
		insert(&(*root)->right, rootData, leftData, rightData);
	}
	
}

void preOrder(Tree* root) {
	if (root == NULL) {
		return;
	}

	if (root->data != '.') {
		printf("%c", root->data);
	}

	if (root->left) {
		preOrder(root->left);
	}

	if (root->right) {
		preOrder(root->right);
	}
}

void inOrder(Tree* root) {
	if (root == NULL) {
		return;
	}

	if (root->left) {
		inOrder(root->left);
	}
	if (root->data != '.') {
		printf("%c", root->data);
	}

	if (root->right) {
		inOrder(root->right);
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
	if (root->data != '.') {
		printf("%c", root->data);
	}
}

int main() {
	Tree* root = NULL;
	//insert(&root, 'A','B','C');
	//insert(&root, 'B', 'D', '.');
	//insert(&root, 'C', 'E', 'F');
	//insert(&root, 'E', '.', '.');
	//insert(&root, 'F', '.', 'G');
	//insert(&root, 'D', '.', '.');
	//insert(&root, 'G', '.', '.');

	int n = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char a, b, c;
		scanf(" %c", &a);
		scanf(" %c", &b);
		scanf(" %c", &c);
		insert(&root, a, b, c);
	}

	preOrder(root);
	printf("\n");
	inOrder(root);
	printf("\n");
	postOrder(root);
	printf("\n");


	return 0;
}