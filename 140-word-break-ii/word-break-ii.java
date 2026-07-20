class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        return dfs(s, new HashSet<>(wordDict), new HashMap<>());
    }

    private List<String> dfs(String s, Set<String> set, Map<String, List<String>> memo) {
        if (memo.containsKey(s)) return memo.get(s);

        List<String> res = new ArrayList<>();

        if (s.isEmpty()) {
            res.add("");
            return res;
        }

        for (String w : set) {
            if (s.startsWith(w)) {
                for (String sub : dfs(s.substring(w.length()), set, memo))
                    res.add(w + (sub.isEmpty() ? "" : " " + sub));
            }
        }

        memo.put(s, res);
        return res;
    }
}