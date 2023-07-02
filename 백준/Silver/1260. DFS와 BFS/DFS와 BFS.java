import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void print(int[][] graph) {
		for (int i = 1; i < graph.length; i++) {
			for (int j = 1; j < graph.length; j++)
				System.out.print(graph[i][j] + " ");
			System.out.println();
		}
	}

	public static void setEdge(int[][] graph, int x, int y) {
		graph[x][y] = 1;
		graph[y][x] = 1;
	}

	public static void dfs(int[][] graph, int v, int[] visited) {

		for (int i = 1; i < graph[v].length; i++) {
//			System.out.println(v+"의 간선  " + i + " : " + graph[v][i]);
			if (graph[i][v] == 1 && visited[i] != 1) {
				visited[i] = 1;
//				System.out.println(graph[v][i] + " : " + i);
				System.out.print(i + " ");
//				System.out.println("\n\n그래프 : ");
//				print(graph);
				dfs(graph, i, visited);
			}
		}
	}

	public static void bfs(int[][] graph, int v, int[] visited) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(v);
		
		while(!queue.isEmpty()) {
			int tmp = queue.poll();
			
			for(int i = 1; i < graph[tmp].length; i++) {
				if(graph[i][tmp]==1 && visited[i]!=1) {
					visited[i] = 1;
					System.out.print(i + " ");
					queue.add(i);
				}
			}
		}
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String tmp = sc.nextLine();
		int n = Integer.parseInt(tmp.split(" ")[0]);
		int m = Integer.parseInt(tmp.split(" ")[1]);
		int v = Integer.parseInt(tmp.split(" ")[2]);

		int[][] graph = new int[n + 1][n + 1];		
		for (int i = 0; i < m; i++) {
			tmp = sc.nextLine();
			setEdge(graph, Integer.parseInt(tmp.split(" ")[0]), Integer.parseInt(tmp.split(" ")[1]));
		}
//		int n = 5;
//		int[][] graph = new int[n + 1][n + 1];		
//		int m = 5;
//		int v = 3;
//		setEdge(graph, 5, 4);
//		setEdge(graph, 5, 2);
//		setEdge(graph, 1, 2);
//		setEdge(graph, 3, 4);
//		setEdge(graph, 3, 1);


		int[] visited1 = new int[n + 1];
		visited1[v] = 1;
//		System.out.print("dfs" + v + " ");
		System.out.print(v + " ");
		dfs(graph, v, visited1);
		System.out.println();

		int[] visited2 = new int[n + 1];
		visited2[v] = 1;
//		System.out.print("bfs" + v + " ");
		System.out.print(v + " ");
		bfs(graph, v, visited2);
		System.out.println();

		sc.close();
	}
}
