class Solution {
    public static String makeFancyString(String s) {
        int count = 0;
        char hold = s.charAt(0);
        StringBuilder s2 = new StringBuilder(s);
        int remove = 0;
//            System.out.println(s);
        for (int i = 1; i < s2.length(); i++) {

            if (s2.charAt(i) == (hold)) {
                count++;
            } else {
                hold = s2.charAt(i);
                count = 0;
            }
            if (count >= 2) {
                s2.deleteCharAt(i);
                // System.out.println("b");
//                remove++;
                i--;
            }
        }
        return s2 + "";
    }
}