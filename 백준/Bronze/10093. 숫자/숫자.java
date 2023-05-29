import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		long start = Long.parseLong(sc.next());
		long end = Long.parseLong(sc.next());
		
		if(start > end) {
			long tmp = start;
			start = end;
			end = tmp;
		}
		
		System.out.println(start==end ? 0 : end-start-1);
		
		for (Long i = start + 1; i <= end-1; i++) {
			System.out.print(i+" ");
		}

		sc.close();
	}
}
