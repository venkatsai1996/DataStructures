import java.util.* ;
import java.io.*; 
public class Solution {

	public static int arrayEquilibriumIndex(int[] arr){  
		//Your code goes here
		int final_val = 0;
		if(arr.length < 3){
				final_val = -1;
				return final_val;
			}
		boolean allEqual = arr.length == 1 || Arrays.stream(arr).allMatch(t -> t == 0);
        if(allEqual == true){
			return 0;
		}
		
		for(int i = 1; i< arr.length - 1 ; i++){
			if(arr.length < 3){
				final_val = -1;
				break;
			}
			int sum_left = 0;
			for(int j= 0 ; j< i ; j++){
				sum_left += arr[j];
			}
			//System.out.println(sum_left);
			int sum_right = 0;
			for(int j= i+1 ; j< arr.length   ; j++){
				sum_right += arr[j];
			}
			if(sum_left == sum_right){
				final_val =  i;
				break;
			}

			if(i == arr.length - 2){
				final_val = -1;
			}
		}
		return 	final_val;
	}

	}
