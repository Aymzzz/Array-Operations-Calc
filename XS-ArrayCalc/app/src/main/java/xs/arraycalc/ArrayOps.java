package xs.arraycalc;

import java.util.Arrays;
import javax.jws.WebService;

@WebService
public class ArrayOps {

    public int[] sortArray(int[] arrayIn){
        Arrays.sort(arrayIn);
        return arrayIn;
    }

    public int maxArray(int[] arrayIn){
        return Arrays.stream(arrayIn).max().getAsInt();
    }

    public int minArray(int[] arrayIn){
        return Arrays.stream(arrayIn).min().getAsInt();
    }

    public int[] sumArrays(int[] arrayIn1, int[] arrayIn2) {

        if (arrayIn1.length != arrayIn2.length) {
            throw new IllegalArgumentException("Arrays must be of equal length");
        }
    
        int[] result = new int[arrayIn1.length + arrayIn2.length];
        System.arraycopy(arrayIn1, 0, result, 0, arrayIn1.length);
        System.arraycopy(arrayIn2, 0, result, arrayIn1.length, arrayIn2.length);
    
        for (int i = 0; i < result.length; i++) {
            result[i] += (i < arrayIn1.length ? 0 : arrayIn2[i - arrayIn1.length]);
        }
    
        return result;
    }
    public int[] multiplyArrays(int[] arrayIn1, int[] arrayIn2) {
        if (arrayIn1.length != arrayIn2.length) {
            throw new IllegalArgumentException("Arrays must be of equal length");
        }

        int[] result = new int[arrayIn1.length];

        for (int i = 0; i < arrayIn1.length; i++) {
            result[i] = arrayIn1[i] * arrayIn2[i];
        }

        return result;
    }
}
