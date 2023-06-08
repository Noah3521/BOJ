import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String input = bf.readLine();	// N M 형태로 입력
		String[] tmp = input.split(" ");// arr[0] = N, arr[1] = M
		int N = Integer.parseInt(tmp[0]);// int N = arr[0]
		int M = Integer.parseInt(tmp[1]);// int M = arr[1]
		
		HashMap<Integer, String> map = new HashMap<Integer, String>();
		HashMap<String, Integer> map2 = new HashMap<String, Integer>();
		for (int i = 1; i < N + 1; i++) {
			String s = bf.readLine();
			map.put(i, s); // [1, s], [2, s] ...
			map2.put(s, i);// [s, 1], [s, 2] ...
		}
//		System.out.println(map);
		
		
		for (int i = 0; i < M; i++) {
			String s = bf.readLine();
			try {
				int n = Integer.parseInt(s);
				System.out.println(map.get(n));
			}catch (Exception e) {
				System.out.println(map2.get(s));
			}
		}		
	}
}