import sys
sys.setrecursionlimit(10**5)


def preorder(start_in, end_in, start_post, end_post): 
    root = postorder[end_post]

    # print(start_in, end_in, start_post, end_post)

    if start_in > end_in or start_post > end_post: # 방문한 노드라면 return
        return

    print(root, end = ' ') # 현재 범위의 루트노드

    p = inorder.index(root)

    size = p - start_in

    # 왼쪽
    preorder(start_in, p - 1, start_post, start_post + size - 1)
    # 오른쪽
    preorder(p + 1, end_in, start_post + size, end_post - 1)
    
n = int(input())
inorder   =   list(map(int, input().split()))
postorder =   list(map(int, input().split()))
visited = [0 * i for i in range(n+1)]
preorder(0, n-1, 0, n-1)