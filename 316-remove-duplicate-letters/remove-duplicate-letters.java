class Solution {
    public String removeDuplicateLetters(String s) {
        int[] lastIndex = new int[26];
        
        // Step 1: Store last occurrence of each character
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }
        
        boolean[] visited = new boolean[26];
        StringBuilder stack = new StringBuilder();
        
        // Step 2: Traverse string
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            // If already used, skip
            if (visited[ch - 'a']) continue;
            
            // Remove bigger characters if they appear later
            while (stack.length() > 0 &&
                   stack.charAt(stack.length() - 1) > ch &&
                   lastIndex[stack.charAt(stack.length() - 1) - 'a'] > i) {
                
                visited[stack.charAt(stack.length() - 1) - 'a'] = false;
                stack.deleteCharAt(stack.length() - 1);
            }
            
            // Add current character
            stack.append(ch);
            visited[ch - 'a'] = true;
        }
        
        return stack.toString();
    }
}