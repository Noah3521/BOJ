import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };
		int[] tmp = new int[20];

		for (int N = 0; N < 10; N++) {
			int start = Integer.parseInt(sc.next());
			int end = Integer.parseInt(sc.next());

			if(start==end)
				continue;
			
			for (int i = start - 1; i < end; i++) {
				tmp[i] = arr[i];
			}
//			System.out.println(Arrays.toString(tmp));
			int cnt = 0;
			for (int i = start - 1; i < end; i++) {
				arr[i] = tmp[end-cnt++-1];
			}
//			System.out.println(Arrays.toString(arr));
//			System.out.println();

		}
		String result = Arrays.toString(arr).replaceAll(",", "").replace("[", "").replace("]", "");
		System.out.println(result);

		 sc.close();
	}
}
