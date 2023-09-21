import java.util.* ;
import java.io.*; 
public class Solution {
	
	public static void inplaceRotate(int[][] arr, int n) {
		for(int j = n-1 ; j>=0;j--){
			for(int i=0;i<n ; i++){
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}

	}

}
