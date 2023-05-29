import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int N = Integer.parseInt(sc.nextLine());
		int totalY = 0;
		int totalM = 0;

		for (int i = 0; i < N; i++) {

			int Ycash = 10;
			int Mcash = 15;
			int time = Integer.parseInt(sc.next());;

			totalY += (Ycash += time / 30 * 10);
			totalM += (Mcash += time / 60 * 15);
//			System.out.println(Ycash += time / 30 * 10);
//			System.out.println(Mcash += time / 60 * 15);
		}

		if (totalM == totalY) {
			System.out.print("Y M " + totalM);
		} else if (totalM > totalY) {
			System.out.print("Y " + totalY);
		} else {
			System.out.print("M " + totalM);
		}
		
		sc.close();
	}
}
