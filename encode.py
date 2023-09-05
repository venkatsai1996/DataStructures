import java.util.*;
import java.io.*;
public class Solution {
    public static String encode(String message) { // Write your code here. 
    int n=message.length();  
    String ans="";  
    for(int i=0;i<n;i++)  {   
        char curChar=message.charAt(i);   
        int charfreq=1;   
        while(i+1<n && message.charAt(i+1)==curChar)  
        {    i++;    charfreq++;   }   ans=ans+curChar+charfreq;  
        
    }  return ans; 
        
    } 
    
}
