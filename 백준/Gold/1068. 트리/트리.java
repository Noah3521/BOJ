import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {

	public static HashSet<Integer> findDelNode(int[][] tree, int n, int del) {
		
		// 지울노드 저장할 set
	    HashSet<Integer> set = new HashSet<Integer>();
	    
	    
	    for (int i = 0; i < n; i++) {
	    	// tree의 행이나 열에 del이 들어가기만 하면 됨
	    	// 해당 노드와 연결된 노드는 같은 열이나 행에 이어져있음
	        int data = tree[i][del];
	        // 노드가 999가 아닐때
	        if (data != 999) {
//	            System.out.println("지울거 : " + data);
	            // 지울 노드에 저장함
	            set.add(data);
	        }
	    }
	    
	    // 몇번 반복해야되는지 몰라서 그냥 n번함
	    for (int k = 0; k < n; k++) {
	    	// set 하나로 순회중에 set내용 바꾸니까 ConcurrentModificationException예외 발생해서 tmp만듬
	        HashSet<Integer> tmp = new HashSet<Integer>();
	        set.forEach(o -> {
	            for (int i = 0; i < n; i++) {
	                int data = tree[i][o];
	                if (data != 999) {
	                    tmp.add(data);
	                }
	            }
	        });
	        set.addAll(tmp);
	    }
	    return set;
	}

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		// 노드의 개수
		int n = Integer.parseInt(sc.nextLine());
		// 각 노드의 부모노드
		int[] node = Stream.of(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		// 지워야할 노드 (지운 노드의 자식노드들도 모두 제거함)
		int del = Integer.parseInt(sc.nextLine());
		
		for(int i = 0; i < node.length; i++) {
			if(node[i] == -1) {
				// -1을 인덱스에 넣으면 에러나니까 999로 바꿈
				node[i] = 999;
				break;
			}
		}
		
		// 전부 999로 초기화
		int[][] tree = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				tree[i][j] = 999;
			}
		}
		
		// 0 ~ n까지 채워넣을 배열
		int[] data = new int[n];
		for (int i = 0; i < n; i++) {
			data[i] = i;
		}

		// 트리에 삽입
		for (int i = 0; i < n; i++) {
			int value = data[i]; // 0~n
			int root = node[i] == 999 ? value : node[i]; // 노드가 루트 노드라면  
			tree[root][value] = i;						 // tree[i][j] == tree[i][j]인곳에 
			tree[value][root] = i;						 // i를 저장
		}

		boolean isRoot = false;
		if (tree[del][del] != 999) { // 지울 노드가 루트노드라면
			isRoot = true;			 
		}
		if (!isRoot) {				 // 지운 노드가 루트노드가 아닐 경우
			
			// 지울 번호를 set에 으로 반환
			HashSet<Integer> delArr = findDelNode(tree, n, del); 
			delArr.forEach(s -> {
				for (int i = 0; i < n; i++) {
					if (tree[i][s] != 999) {
//						System.out.println("지울거 : " + tree[i][s]);
						tree[i][s] = 999;
						tree[s][i] = 999;
					}
				}
			});

//			for (int i = 0; i < n; i++) {
//				for (int j = 0; j < n; j++) {
//					System.out.printf("%3d ", tree[i][j]);
//				}
//				System.out.println();
//			}
			
			// 리프노드 개수 저장할거임
			int leaf = 0;
			for (int i = 0; i < n; i++) {
				// i번째 자식노드의 개수 저장할거
				int count = 0;
				for (int j = 0; j < n; j++) {
					// 해당 노드가 빈 노드가 아니라면
					if (tree[i][j] != 999) {
						// 
						count++;
					}
				}
				if (count == 1) {
//					System.out.println("i : " + i);
					leaf++;
				}
			}
			System.out.println(leaf);
		}
		else {	// 루트노드를 지운 경우
			System.out.println(0);
		}
		sc.close();
	}
}
