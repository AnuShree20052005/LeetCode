class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start, path):
            # If we have 4 parts
            if len(path) == 4:
                # If all digits are used
                if start == len(s):
                    result.append(".".join(path))
                return

            # Try segment lengths 1, 2, and 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Skip leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                # Skip values greater than 255
                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + length, path)
                path.pop()

        backtrack(0, [])
        return result