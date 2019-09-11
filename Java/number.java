import java.util.Random;
public class number{
	public static void main(String args[]){
	Random rand = new Random();

	int n = rand.nextInt(1000000)+1;
	System.out.println(n);
	}
}
