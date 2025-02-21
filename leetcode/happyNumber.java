
/*
 * Happy Number
 * https://leetcode.com/problems/happy-number/
 * Needs to be optimized!
*/
import java.util.*;

public class happyNumber {
    public static boolean isHappy(int n) {
        // Convert n to String
        String nString = String.valueOf(n);
        double ans = 0;
        HashMap<Double, Integer> hp = new HashMap<>();
        while (ans != 1) {
            ans = 0;
            // Iterate through nString and sum the power of each character
            for (int i = 0; i < nString.length(); i++) {
                ans += Math.pow(Integer.parseInt(nString.substring(i, i + 1)), 2);
            }
            if (ans == 1) {
                return true;
            } else {
                // Return false if ans in hp (cycle detected)
                if (hp.containsValue(ans)) {
                    return false;
                } else {
                    // Otherwise, add ans to hp
                    hp.put(ans, 1);
                    // Return false if size of hp greater than 7
                    if (hp.size() > 7) {
                        return false;
                    }
                }
                // Convert ans to String
                nString = String.valueOf(ans);
                // Remove decimal values
                nString = nString.substring(0, nString.length() - 2);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isHappy(19)); // true
        System.out.println(isHappy(2)); // false
    }
}