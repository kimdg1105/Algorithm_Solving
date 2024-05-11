package problem;

import java.util.Arrays;

public class LengthOfLastWord {
    public static void main(String[] args) {
        lengthOfLastWord("   fly me   to   the moon  ");
    }

    public static int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        int lastIdx = words.length - 1;
        Arrays.stream(words).forEach(System.out::println);
        return words[lastIdx].length();
    }
}
