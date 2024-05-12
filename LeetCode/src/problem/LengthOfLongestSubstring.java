package problem;

public class LengthOfLongestSubstring {
    public static void main(String[] args) {
        lengthOfLongestSubstring("pwwkew");
    }

    public static int lengthOfLongestSubstring(String s) {
        int length = s.length();
        int maxLength = 0;
        for (int i = 0; i < length; i++) {
            StringBuilder sub = new StringBuilder();
            int idx = i;
            while (idx < length) {
                if (!sub.toString().contains(String.valueOf(s.charAt(idx)))) {
                    sub.append(s.charAt(idx));
                } else {
                    break;
                }
                idx += 1;
            }
            System.out.println(sub);
            maxLength = Math.max(maxLength, sub.length());
        }
        return maxLength;
    }
}
