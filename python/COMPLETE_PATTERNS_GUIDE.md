# 🚀 COMPLETE LEETCODE PATTERNS & SOLUTIONS GUIDE

**Last Updated:** December 2, 2025  
**Total Problems:** 20 (17 Easy, 3 Medium)  
**Perfect Solutions:** 6 ✓✓  
**Near-Optimal:** 5 ✓

---

## 📚 TABLE OF CONTENTS

### EASY PROBLEMS (17)
1. [Add Digits](#1-add-digits-leetcode-258)
2. [Count Vowel Strings in Range](#2-count-vowel-strings-in-range-leetcode-2586)
3. [FizzBuzz](#3-fizzbuzz-leetcode-412)
4. [Palindrome Number](#4-palindrome-number-leetcode-9)
5. [Valid Anagram](#5-valid-anagram-leetcode-242)
6. [Remove Duplicates from Sorted List](#6-remove-duplicates-from-sorted-list-leetcode-83)
7. [Valid Palindrome](#7-valid-palindrome-leetcode-125)
8. [Longest Common Prefix](#8-longest-common-prefix-leetcode-14)
9. [Is Subsequence](#9-is-subsequence-leetcode-392)
10. [Valid Parentheses](#10-valid-parentheses-leetcode-20)
11. [Group Anagrams](#11-group-anagrams-leetcode-49)
12. [String Compression](#12-string-compression-leetcode-443)
13. [Two Sum](#13-two-sum-leetcode-1)
14. [Move Zeroes](#14-move-zeroes-leetcode-283)
15. [Majority Element](#15-majority-element-leetcode-169)
16. [Intersection of Two Arrays](#16-intersection-of-two-arrays-leetcode-349)
17. [Best Time to Buy and Sell Stock](#17-best-time-to-buy-and-sell-stock-leetcode-121)

### MEDIUM PROBLEMS (3)
18. [Reverse Integer](#18-reverse-integer-leetcode-7)
19. [Remove Minimum and Maximum From Array](#19-remove-minimum-and-maximum-from-array-leetcode-2091)
20. [Rotate Array](#20-rotate-array-leetcode-189)

---

## 📖 EASY PROBLEMS

### 1. Add Digits (LeetCode #258)

**🎯 Pattern:** Mathematical Invariant (Digital Root)

#### Your Approach
```python
class Solution(object):
    def addDigits(self, num):
        while True:
            old = num
            new = 0
            for digit in map(int, str(old)):
                new += digit
            if new < 10:
                break
            else:
                num = new
        return new
```

**Algorithm:**
- Loop until single digit remains
- Convert to string, sum digits each iteration
- Break when result < 10

**Complexity:**
- **Time:** O(d) where d = number of digits (few iterations)
- **Space:** O(d) - string conversion each loop

**How It Works:**
```
38 → "38" → 3 + 8 = 11
11 → "11" → 1 + 1 = 2
Return 2
```

#### ✨ Optimal Approach

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
```

**Algorithm:**
- Use digital root formula: `1 + (num - 1) % 9`
- Mathematical property: digital root follows pattern based on modulo 9

**Complexity:**
- **Time:** O(1) - single calculation
- **Space:** O(1) - no extra space

**Why It Works:**
- Digital root has a mathematical pattern
- For any number n: digital_root(n) = 1 + (n-1) % 9
- Examples: 38 → 1 + 37%9 = 1 + 1 = 2 ✓

**Key Learnings:**
- ✅ Math formulas can eliminate loops entirely
- ✅ Look for invariant patterns in repetitive operations
- ✅ O(d) → O(1) is significant improvement

---

### 2. Count Vowel Strings in Range (LeetCode #2586)

**🎯 Pattern:** Set-Based Membership Testing

#### Your Approach
```python
class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
        return count
```

**Algorithm:**
- List of vowels for membership check
- Loop through range, check first and last character
- Count matches

**Complexity:**
- **Time:** O(n) where n = words in range
- **Space:** O(1) - fixed vowels list

**How It Works:**
```
words = ["are","amy","u"], left=0, right=2
"are": a in vowels ✓, e in vowels ✓ → count = 1
"amy": a in vowels ✓, y in vowels ✗ → count = 1
"u": u in vowels ✓, u in vowels ✓ → count = 2
Return 2
```

#### ✨ Optimal Approach

```python
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        return sum(word[0] in vowels and word[-1] in vowels 
                   for word in words[left:right+1])
```

**Algorithm:**
- Use set() for O(1) lookup instead of list O(k)
- List comprehension for conciseness
- sum() on boolean generator

**Complexity:**
- **Time:** O(n) - same asymptotic complexity
- **Space:** O(1) - set is constant size

**Key Learnings:**
- ✅ Set membership is O(1) vs List O(k)
- ✅ Generator expressions save memory
- ✅ Already near-optimal, minor improvement only

---

### 3. FizzBuzz (LeetCode #412)

**🎯 Pattern:** Boolean Multiplication + String Concatenation

#### Your Approach
```python
class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))
        return res
```

**Algorithm:**
- Check divisibility in order (15, 5, 3)
- Append corresponding string
- Convert number to string for else case

**Complexity:**
- **Time:** O(n) - loop n times
- **Space:** O(n) - result list

**How It Works:**
```
n = 5:
1 → not divisible → "1"
2 → not divisible → "2"
3 → divisible by 3 → "Fizz"
4 → not divisible → "4"
5 → divisible by 5 → "Buzz"
```

#### ✨ Optimal Approach

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i) 
                for i in range(1, n + 1)]
```

**Algorithm:**
- Boolean multiplication: `True * "String"` = "String", `False * "String"` = ""
- Concatenate Fizz and Buzz based on divisibility
- `or str(i)` provides fallback when both False (empty string)

**Complexity:**
- **Time:** O(n) - same complexity
- **Space:** O(n) - same space

**Why It Works:**
```
i=3: "Fizz"*(True) + "Buzz"*(False) = "Fizz" + "" = "Fizz"
i=5: "Fizz"*(False) + "Buzz"*(True) = "" + "Buzz" = "Buzz"
i=15: "Fizz"*(True) + "Buzz"*(True) = "Fizz" + "Buzz" = "FizzBuzz"
i=1: "" + "" = "" → or "1" = "1"
```

**Key Learnings:**
- ✅ Boolean multiplication enables elegant conditional strings
- ✅ `or` operator provides fallback for empty strings
- ✅ More Pythonic, same complexity

---

### 4. Palindrome Number (LeetCode #9)

**🎯 Pattern:** Mathematical Reversal (Half-Number Technique)

#### Your Approach
```python
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = s[::-1]
        if s == rev:
            return True
        else:
            return False
```

**Algorithm:**
- Convert to string
- Reverse using slicing
- Compare original and reversed

**Complexity:**
- **Time:** O(d) where d = number of digits
- **Space:** O(d) - two string copies

**How It Works:**
```
121 → "121" → reverse = "121" → equal ✓
-121 → "-121" → reverse = "121-" → not equal ✗
```

#### ✨ Optimal Approach

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        
        return x == rev or x == rev // 10
```

**Algorithm:**
- Early return for negatives and numbers ending in 0
- Reverse only half the number mathematically
- Compare original half with reversed half

**Complexity:**
- **Time:** O(d) - still linear in digits
- **Space:** O(1) - no string allocation

**How It Works:**
```
x = 1221:
  rev = 0, x = 1221
  rev = 1, x = 122
  rev = 12, x = 12
  x == rev → True

x = 12321:
  rev = 0, x = 12321
  rev = 1, x = 1232
  rev = 12, x = 123
  rev = 123, x = 12
  x == rev // 10 → 12 == 12 → True
```

**Key Learnings:**
- ✅ Avoid string operations when pure math works
- ✅ Only need to reverse half (middle digit doesn't matter)
- ✅ Math operations don't allocate memory

---

### 5. Valid Anagram (LeetCode #242)

**🎯 Pattern:** Frequency Counting with Hash Map

#### Your Approach
```python
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

**Algorithm:**
- Early return if lengths differ
- Sort both strings
- Compare sorted versions

**Complexity:**
- **Time:** O(n log n) - sorting dominates
- **Space:** O(n) - sorted copies

**How It Works:**
```
s = "anagram", t = "nagaram"
sorted(s) = ['a','a','a','g','m','n','r']
sorted(t) = ['a','a','a','g','m','n','r']
Equal ✓
```

#### ✨ Optimal Approach

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
```

**Alternative (Using Counter):**
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

**Algorithm:**
- Count frequency of each character in first string
- Decrement counts while iterating second string
- If any char missing or count goes negative, not anagram

**Complexity:**
- **Time:** O(n) - two linear passes
- **Space:** O(1) - fixed character set (26 letters)

**How It Works:**
```
s = "anagram"
count = {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}

t = "nagaram"
'n' → count['n']=0
'a' → count['a']=2
'g' → count['g']=0
'a' → count['a']=1
'r' → count['r']=0
'a' → count['a']=0
'm' → count['m']=0
All zero ✓
```

**Key Learnings:**
- ✅ Hash maps beat sorting for frequency problems
- ✅ O(n log n) → O(n) is significant improvement
- ✅ Counter class is built for this pattern

---

### 6. Remove Duplicates from Sorted List (LeetCode #83)

**🎯 Pattern:** Two-Pointer In-Place Modification

#### Your Approach ✓✓
```python
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```

**Algorithm:**
- Single pointer traversal
- If current value equals next, skip next node
- Otherwise, move to next

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - in-place modification

**How It Works:**
```
1 → 1 → 2 → 3 → 3

current=1, next=1 → skip
1 → 2 → 3 → 3

current=1, next=2 → move
current=2, next=3 → move
current=3, next=3 → skip
1 → 2 → 3
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Key Learnings:**
- ✅ In-place linked list modification saves space
- ✅ Pointer manipulation is the standard pattern
- ✅ Perfect solution for this problem

---

### 7. Valid Palindrome (LeetCode #125)

**🎯 Pattern:** Two-Pointer with In-Place Filtering

#### Your Approach
```python
class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
```

**Algorithm:**
- Filter non-alphanumeric characters first
- Convert to lowercase
- Two-pointer comparison from both ends

**Complexity:**
- **Time:** O(n) - filtering + comparison
- **Space:** O(n) - filtered string copy

**How It Works:**
```
"A man, a plan, a canal: Panama"
→ filter → "AmanaplanacanalPanama"
→ lower → "amanaplanacanalpanama"
→ two-pointer check → palindrome ✓
```

#### ✨ Optimal Approach

```python
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
```

**Algorithm:**
- Two pointers on original string
- Skip non-alphanumeric characters on-the-fly
- Compare lowercase characters

**Complexity:**
- **Time:** O(n) - same asymptotic
- **Space:** O(1) - no intermediate string

**How It Works:**
```
"A man, a plan, a canal: Panama"
 ↑                              ↑
 A (alnum) == a (alnum) ✓
   ↑                          ↑
   skip spaces
     ↑                      ↑
     m == m ✓
     Continue...
```

**Key Learnings:**
- ✅ Don't create intermediate filtered structures
- ✅ Skip invalid characters during traversal
- ✅ Process on-the-fly instead of preprocessing

---

### 8. Longest Common Prefix (LeetCode #14)

**🎯 Pattern:** Vertical Scanning with Slicing

#### Your Approach
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        
        for i in range(len(strs[0])):
            first = strs[0][i]
            
            for char in strs[1:]:
                if i >= len(char) or char[i] != first:
                    return prefix
                    
            prefix += first
        
        return prefix
```

**Algorithm:**
- Iterate through each character position in first string
- Check if all other strings have same character at that position
- Build prefix by concatenating characters

**Complexity:**
- **Time:** O(S) where S = sum of all characters
- **Space:** O(m) - prefix grows with each concatenation

**How It Works:**
```
["flower", "flow", "flight"]
i=0: f==f==f ✓ → prefix="f"
i=1: l==l==l ✓ → prefix="fl"
i=2: o==o==i ✗ → return "fl"
```

#### ✨ Optimal Approach

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            char = strs[0][i]
            if any(s[i] != char for s in strs):
                return strs[0][:i]
        
        return strs[0][:min_len]
```

**Alternative (Pythonic with zip):**
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        
        return min(strs, key=len)
```

**Algorithm:**
- Pre-calculate minimum length to avoid index errors
- Use `any()` for early exit on mismatch
- Single slice at return instead of concatenation

**Complexity:**
- **Time:** O(S) - same asymptotic
- **Space:** O(1) - only final slice, not growing

**How zip approach works:**
```
zip(*["flower", "flow", "flight"])
→ [('f','f','f'), ('l','l','l'), ('o','o','i')]
i=0: set('f','f','f') = 1 element ✓
i=1: set('l','l','l') = 1 element ✓
i=2: set('o','o','i') = 2 elements ✗ → return strs[0][:2] = "fl"
```

**Key Learnings:**
- ✅ Slicing once is better than repeated concatenation
- ✅ Pre-calculate bounds to avoid index errors
- ✅ Vertical scanning better than horizontal for early termination
- ✅ `zip(*strs)` transposes strings elegantly

---

### 9. Is Subsequence (LeetCode #392)

**🎯 Pattern:** Two-Pointer (Greedy)

#### Your Approach ✓✓
```python
class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        
        return i == len(s)
```

**Algorithm:**
- Single pointer tracking position in subsequence `s`
- Iterate through main string `t`
- Advance pointer when characters match
- Check if all of `s` was matched

**Complexity:**
- **Time:** O(n) where n = len(t)
- **Space:** O(1) - single pointer

**How It Works:**
```
s = "abc", t = "ahbgdc"
i=0, char='a': s[0]='a' ✓ → i=1
i=1, char='h': s[1]='b' ✗
i=1, char='b': s[1]='b' ✓ → i=2
i=2, char='g': s[2]='c' ✗
i=2, char='d': s[2]='c' ✗
i=2, char='c': s[2]='c' ✓ → i=3
i==3==len(s) ✓
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Alternative (Pythonic):**
```python
def isSubsequence(self, s, t):
    it = iter(t)
    return all(char in it for char in s)
```

**Follow-up (Multiple Queries):**
If you need to check multiple `s` against same `t`:
```python
from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s, t):
        # Preprocess t: char → [positions]
        char_indices = defaultdict(list)
        for i, char in enumerate(t):
            char_indices[char].append(i)
        
        current_pos = -1
        for char in s:
            if char not in char_indices:
                return False
            # Binary search for next position > current_pos
            indices = char_indices[char]
            idx = bisect.bisect_right(indices, current_pos)
            if idx == len(indices):
                return False
            current_pos = indices[idx]
        
        return True
```

**Complexity for multiple queries:**
- Preprocessing: O(t)
- Per query: O(s log t)
- k queries: O(t + k × s log t) vs O(k × t) for greedy

**Key Learnings:**
- ✅ Greedy approach is optimal for single query
- ✅ Can't do better than O(n) time
- ✅ For multiple queries: preprocess with binary search

---

### 10. Valid Parentheses (LeetCode #20)

**🎯 Pattern:** Stack-Based Matching

#### Your Approach
```python
class Solution(object):
    def isValid(self, s):
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in mapping.values():  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
        
        return not stack
```

**Algorithm:**
- Use dictionary to map closing to opening brackets
- Stack to track opening brackets
- For opening: push to stack
- For closing: check if top matches

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(n) - worst case stack holds all opening brackets

**How It Works:**
```
s = "([])"
'(' → opening → stack = ['(']
'[' → opening → stack = ['(', '[']
']' → closing → pop '[', mapping[']']='[' ✓ → stack = ['(']
')' → closing → pop '(', mapping[')']='(' ✓ → stack = []
Empty stack ✓
```

#### ✨ Optimal Approach

```python
class Solution(object):
    def isValid(self, s):
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in mapping:  # O(1) - closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return not stack
```

**Algorithm:**
- Flip logic: check `char in mapping` (dict keys) first
- This is O(1) lookup vs O(3) for checking values
- Same logic, more efficient

**Complexity:**
- **Time:** O(n) - same asymptotic, better constant
- **Space:** O(n) - same

**Key Learnings:**
- ✅ Dict key lookup is O(1) vs dict values lookup is O(k)
- ✅ Just flip the conditional logic for efficiency
- ✅ Stack is the standard pattern for bracket matching
- ✅ Near-optimal - minor constant factor improvement

---

### 11. Group Anagrams (LeetCode #49)

**🎯 Pattern:** Character Frequency as Hash Key

#### Your Approach ✓✓
```python
class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(word)
        
        return list(anagrams.values())
```

**Algorithm:**
- Create frequency array [0]*26 for each word
- Count occurrences of each character (a-z)
- Convert array to tuple (hashable) as dictionary key
- Group words with same frequency pattern

**Complexity:**
- **Time:** O(n × k) where n = number of strings, k = max length
- **Space:** O(n × k) - storing all strings in groups

**How It Works:**
```
["eat", "tea", "tan", "ate", "nat", "bat"]

"eat" → [1,0,0,0,1,0...19:1...] → key1
"tea" → [1,0,0,0,1,0...19:1...] → key1 (same!)
"tan" → [1,0,0,...13:1...19:1...] → key2
"ate" → key1
"nat" → key2
"bat" → [1,1,0,...19:1...] → key3

Result: {
  key1: ["eat","tea","ate"],
  key2: ["tan","nat"],
  key3: ["bat"]
}
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Alternative (Sorted String as Key):**
```python
def groupAnagrams(self, strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
```

**Complexity:** O(n × k log k) - simpler but slower

**Key Learnings:**
- ✅ Character frequency tuple is optimal for anagram grouping
- ✅ Avoids sorting overhead (O(k) vs O(k log k) per word)
- ✅ Tuple is hashable, list is not
- ✅ Perfect approach for this problem type

---

### 12. String Compression (LeetCode #443)

**🎯 Pattern:** Two-Pointer In-Place Modification

#### Your Approach ✓✓
```python
class Solution(object):
    def compress(self, chars):
        i = 0
        write = 0
        
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write
```

**Algorithm:**
- Read pointer (`i`) and write pointer (`write`)
- Count consecutive identical characters
- Write character, then count digits (if > 1)
- Modify array in-place

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - in-place modification

**How It Works:**
```
["a","a","b","b","c","c","c"]
      ↑
      i=0, write=0

char='a', count=2
chars[0]='a', write=1
chars[1]='2', write=2
i=2

char='b', count=2
chars[2]='b', write=3
chars[3]='2', write=4
i=4

char='c', count=3
chars[4]='c', write=5
chars[5]='3', write=6
i=7

Result: ["a","2","b","2","c","3"]
Return: 6
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Edge Cases Handled:**
```python
# Multi-digit counts
["a"]*12 → ["a","1","2"] ✓

# Single character (no count)
["a"] → ["a"] (not ["a","1"]) ✓

# No compression needed
["a","b","c"] → ["a","b","c"] ✓
```

**Key Learnings:**
- ✅ Two-pointer for in-place array modification
- ✅ Correctly handles multi-digit counts with `str(count)`
- ✅ Only write count if > 1
- ✅ Perfect solution for in-place compression

---

### 13. Two Sum (LeetCode #1)

**🎯 Pattern:** Hash Map for Complement Lookup

#### Your Approach
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
```

**Algorithm:**
- Nested loops to check all pairs
- Return indices when sum equals target

**Complexity:**
- **Time:** O(n²) - nested loops
- **Space:** O(1) - no extra space

**How It Works:**
```
nums = [2,7,11,15], target = 9
i=0, j=1: 2+7=9 ✓ → return [0,1]
```

#### ✨ Optimal Approach

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i
        return []
```

**Algorithm:**
- Use hash map to store seen numbers and their indices
- For each number, check if its complement exists in map
- Single pass through array

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(n) - hash map storage

**How It Works:**
```
nums = [2,7,11,15], target = 9
i=0, num=2: comp=7, map={} → add 2:0
i=1, num=7: comp=2, map={2:0} → found! return [0,1]
```

**Key Learnings:**
- ✅ Hash maps eliminate nested loops
- ✅ O(n²) → O(n) is major improvement
- ✅ Trade space for time: O(1) → O(n) space saves O(n) time
- ✅ Classic pattern for pair-finding problems

---

### 14. Move Zeroes (LeetCode #283)

**🎯 Pattern:** Two-Pointer In-Place Swap

#### Your Approach
```python
class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums
```

**Algorithm:**
- Iterate through array
- Remove zeros and append at end
- Modify in-place

**Complexity:**
- **Time:** O(n²) - `remove()` is O(n) inside loop
- **Space:** O(1) - in-place modification

**Issues:**
```
[0,1,0,3,12]
Remove first 0 → [1,0,3,12,0]
Skip second 0 (iteration issue) ❌
```

#### ✨ Optimal Approach

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0  # Pointer for next non-zero position
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
```

**Algorithm:**
- Two pointers: `i` for write position, `j` for read position
- When non-zero found, swap with position `i` and increment `i`
- All non-zeros move to front, zeros naturally move to back

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - in-place swaps

**How It Works:**
```
[0,1,0,3,12]
j=0, nums[0]=0: skip
j=1, nums[1]=1: swap(0,1) → [1,0,0,3,12], i=1
j=2, nums[2]=0: skip
j=3, nums[3]=3: swap(1,3) → [1,3,0,0,12], i=2
j=4, nums[4]=12: swap(2,4) → [1,3,12,0,0], i=3
```

**Key Learnings:**
- ✅ Avoid `remove()` in loops - causes O(n²)
- ✅ Two-pointer swap is standard for element rearrangement
- ✅ Preserve relative order of non-zero elements
- ✅ In-place modification without creating new array

---

### 15. Majority Element (LeetCode #169)

**🎯 Pattern:** Boyer-Moore Voting Algorithm

#### Your Approach
```python
class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_key = max(count, key=count.get)
        return max_key
```

**Algorithm:**
- Hash map to count all occurrences
- Find element with maximum count

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(n) - hash map for all unique elements

**How It Works:**
```
[2,2,1,1,1,2,2]
count = {2:4, 1:3}
max(count) → 2
```

#### ✨ Optimal Approach

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
```

**Algorithm:**
- Boyer-Moore Voting Algorithm
- Maintain candidate and count
- Increment count for candidate, decrement for others
- When count reaches 0, switch candidate
- Majority element (>n/2) will be final candidate

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - two variables only

**How It Works:**
```
[2,2,1,1,1,2,2]
candidate=2, count=1 (num=2)
candidate=2, count=2 (num=2)
candidate=2, count=1 (num=1)
candidate=2, count=0 (num=1)
candidate=1, count=1 (num=1)
candidate=1, count=0 (num=2)
candidate=2, count=1 (num=2)
Return: 2 ✓
```

**Key Learnings:**
- ✅ Boyer-Moore eliminates need for hash map
- ✅ O(n) space → O(1) space is significant
- ✅ Works only when majority element guaranteed to exist
- ✅ Clever algorithm based on cancellation principle

---

### 16. Intersection of Two Arrays (LeetCode #349)

**🎯 Pattern:** Set Operations

#### Your Approach ✓
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        res = set()
        
        for num in nums2:
            if num in seen:
                res.add(num)
        
        return list(res)
```

**Algorithm:**
- Convert first array to set
- Iterate through second array
- Add common elements to result set

**Complexity:**
- **Time:** O(n + m) - optimal
- **Space:** O(n) - for sets

**How It Works:**
```
nums1 = [1,2,2,1], nums2 = [2,2]
seen = {1,2}
num=2: in seen → res={2}
num=2: in seen → res={2} (no duplicate)
Return [2]
```

#### ✨ Optimal Approach

```python
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
```

**Algorithm:**
- Use built-in set intersection operator `&`
- Convert both arrays to sets
- Return intersection as list

**Complexity:**
- **Time:** O(n + m) - same complexity
- **Space:** O(n) - same space

**Key Learnings:**
- ✅ Your solution is near-optimal
- ✅ Set intersection operator is more Pythonic
- ✅ Both approaches have same complexity
- ✅ Set automatically handles duplicates

---

### 17. Best Time to Buy and Sell Stock (LeetCode #121)

**🎯 Pattern:** Greedy Single Pass (Kadane's Variant)

#### Your Approach ✓✓
```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
```

**Algorithm:**
- Track minimum price seen so far
- Calculate profit at each step
- Update maximum profit

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - two variables

**How It Works:**
```
[7,1,5,3,6,4]
price=7: min=7, profit=0
price=1: min=1, profit=0
price=5: min=1, profit=4
price=3: min=1, profit=4
price=6: min=1, profit=5
price=4: min=1, profit=5
Return 5
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Alternative (More Pythonic):**
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
```

**Key Learnings:**
- ✅ Greedy approach works perfectly here
- ✅ Track running minimum for optimal buy point
- ✅ Single pass is optimal - can't do better than O(n)
- ✅ Similar to maximum subarray problem (Kadane's algorithm)
- ✅ Perfect solution on first try!

---

## 📖 MEDIUM PROBLEMS

### 18. Reverse Integer (LeetCode #7)

**🎯 Pattern:** Mathematical Digit Manipulation

#### Your Approach
```python
class Solution:
    def reverse(self, x):
        if x < 0:
            s = (str(x)[1:])
            rev = s[::-1]
            res = int(rev) * -1
        else:
            res = int(str(x)[::-1])
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
```

**Algorithm:**
- Convert to string
- Reverse string (handle sign separately)
- Convert back to integer
- Check for 32-bit overflow

**Complexity:**
- **Time:** O(log n) where n = absolute value of x
- **Space:** O(log n) - string representation

**How It Works:**
```
123 → "123" → "321" → 321
-123 → "123" (strip -) → "321" → -321
120 → "120" → "021" → 21
```

#### ✨ Optimal Approach

```python
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x:
            res = res * 10 + x % 10
            x //= 10
        
        res *= sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
```

**Algorithm:**
- Extract sign, work with absolute value
- Build reversed number digit by digit
  - Get last digit: `x % 10`
  - Add to result: `res * 10 + digit`
  - Remove last digit: `x //= 10`
- Apply sign and check overflow

**Complexity:**
- **Time:** O(log n) - still linear in digits
- **Space:** O(1) - no string allocation

**How It Works:**
```
x = 123, sign = 1
res = 0, x = 123

res = 0*10 + 123%10 = 3, x = 12
res = 3*10 + 12%10 = 32, x = 1
res = 32*10 + 1%10 = 321, x = 0

res = 321 * 1 = 321
```

**Key Learnings:**
- ✅ String conversion is slower than math operations
- ✅ Handle sign with multiplication, not separate logic
- ✅ Build reversed number digit by digit with modulo

---

### 19. Remove Minimum and Maximum From Array (LeetCode #2091)

**🎯 Pattern:** Index-Based Optimization (Greedy Choice)

#### Your Approach
```python
class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        max_value = max(nums)
        min_value = min(nums)
        max_index = max(nums.index(max_value), nums.index(min_value))
        min_index = min(nums.index(max_value), nums.index(min_value))
        
        # from front
        front = max_index + 1
        
        # from back
        back = n - min_index
        
        # from both sides
        mix1 = (min_index + 1) + (n - max_index)
        mix2 = (max_index + 1) + (n - min_index)
        
        return min(front, back, mix1, mix2)
```

**Algorithm:**
- Find min and max values
- Find their indices (two O(n) scans with `.index()`)
- Calculate 4 deletion scenarios:
  1. Delete from front up to farther element
  2. Delete from back up to closer element
  3. Delete from both sides (min from left, max from right)
  4. Delete from both sides (max from left, min from right)
- Return minimum

**Complexity:**
- **Time:** O(n) - multiple O(n) operations
- **Space:** O(1) - constant variables

**How It Works:**
```
[2,10,7,5,4,1,8,6]
min=1 (index 5), max=10 (index 1)

Scenarios:
1. Front: delete 0-5 → 6 deletions
2. Back: delete 1-7 → 7 deletions
3. Both (min left, max right): (5+1) + (8-1) = 6 + 7 = 13
4. Both (max left, min right): (1+1) + (8-5) = 2 + 3 = 5 ✓

Return 5
```

#### ✨ Optimal Approach

```python
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index, max_index = 0, 0
        
        # Find both indices in single pass
        for i, val in enumerate(nums):
            if val < nums[min_index]:
                min_index = i
            if val > nums[max_index]:
                max_index = i
        
        left, right = min(min_index, max_index), max(min_index, max_index)
        
        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)
        
        return min(front, back, both)
```

**Algorithm:**
- Find min and max indices in **single pass**
- Avoid `.index()` which scans entire array
- Calculate only 3 scenarios (fourth is redundant)

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - constant space

**Why 3 scenarios (not 4):**
```
left = min(min_idx, max_idx)
right = max(min_idx, max_idx)

Scenarios:
1. Delete from front: 0 to right (includes both)
2. Delete from back: left to n-1 (includes both)
3. Delete from both: 0 to left AND right to n-1

Note: "max from left, min from right" and "min from left, max from right" 
give same result when simplified, so only need one "both" calculation.
```

**Key Learnings:**
- ✅ Combine min/max finding with index tracking
- ✅ Single pass is better than multiple O(n) operations
- ✅ Consider all deletion strategies (front, back, both)
- ✅ Simplify scenarios to avoid redundant calculations

---

### 20. Rotate Array (LeetCode #189)

**🎯 Pattern:** Array Reversal Technique

#### Your Approach ✓✓
```python
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        
        nums[:] = nums[::-1]
        
        nums[:k] = nums[:k][::-1]
        
        nums[k:] = nums[k:][::-1]
        
        return nums
```

**Algorithm:**
- Normalize k using modulo (handle k > n)
- Reverse entire array
- Reverse first k elements
- Reverse remaining elements

**Complexity:**
- **Time:** O(n) - three reversals
- **Space:** O(1) - in-place modification

**How It Works:**
```
[1,2,3,4,5,6,7], k=3

Step 1: Reverse all
[7,6,5,4,3,2,1]

Step 2: Reverse first k (3)
[5,6,7,4,3,2,1]

Step 3: Reverse rest
[5,6,7,1,2,3,4] ✓
```

**Optimal:** **ALREADY OPTIMAL!** ✓✓

**Why This Works:**
```
Original: [1,2,3,4,5,6,7], k=3
Want: [5,6,7,1,2,3,4]

Think of it as: [5,6,7] [1,2,3,4]
               (last k) (first n-k)

Reversal trick:
1. Reverse all → reverses both parts AND their order
2. Reverse each part back → correct element order
```

**Alternative Approaches:**
```python
# Using extra space (not optimal)
def rotate(self, nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]  # O(n) space

# Using cyclic replacements (complex)
def rotate(self, nums, k):
    n = len(nums)
    k %= n
    count = 0
    start = 0
    while count < n:
        current = start
        prev = nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            if start == current:
                break
        start += 1
```

**Key Learnings:**
- ✅ Reversal technique is elegant and optimal
- ✅ Three reversals achieve rotation in-place
- ✅ O(1) space is better than O(n) with slicing
- ✅ Remember to normalize k with modulo
- ✅ Perfect solution on first try!

---

## 📊 PATTERN CATEGORIES SUMMARY

### 1. 🧮 Mathematical Optimization (3 problems)
- **Add Digits:** Digital root formula
- **Palindrome Number:** Reverse half mathematically
- **Reverse Integer:** Digit manipulation with modulo/division

**Core Principle:** Replace loops/strings with math formulas  
**Benefit:** O(1) or O(log n) instead of O(n) with strings

---

### 2. 💾 Space Optimization (4 problems)
- **Valid Palindrome:** In-place filtering
- **Palindrome Number:** No string allocation
- **Longest Common Prefix:** Slicing vs concatenation
- **Majority Element:** Boyer-Moore voting

**Core Principle:** Avoid creating intermediate data structures  
**Benefit:** O(1) space instead of O(n)

---

### 3. 🗺️ Hash Map Optimization (3 problems)
- **Valid Anagram:** Frequency counting
- **Group Anagrams:** Character frequency as key
- **Two Sum:** Complement lookup

**Core Principle:** Hash maps beat sorting for counting/lookup  
**Benefit:** O(n) instead of O(n²) or O(n log n)

---

### 4. ↔️ Two-Pointer Technique (6 problems)
- **Remove Duplicates from Sorted List:** Linked list
- **Valid Palindrome:** String traversal
- **Longest Common Prefix:** Vertical scanning
- **Is Subsequence:** Greedy tracking
- **String Compression:** In-place modification
- **Move Zeroes:** In-place swap

**Core Principle:** In-place modification with dual pointers  
**Benefit:** O(1) space, single pass, efficient

---

### 5. 🏗️ Data Structure Selection (3 problems)
- **Count Vowel Strings:** Set vs List
- **Valid Parentheses:** Stack for matching
- **Intersection of Two Arrays:** Set operations

**Core Principle:** Choose right data structure for operations  
**Benefit:** O(1) operations instead of O(n), optimal matching

---

### 6. 🐍 Python Idioms (1 problem)
- **FizzBuzz:** Boolean multiplication

**Core Principle:** Leverage Python's expressive syntax  
**Benefit:** Cleaner, more Pythonic code

---

### 7. 🔄 Single-Pass Optimization (2 problems)
- **Remove Min/Max from Array:** Combined operations
- **Best Time to Buy and Sell Stock:** Greedy tracking

**Core Principle:** Minimize number of array traversals  
**Benefit:** Better constants, fewer cache misses

---

### 8. 🔁 Array Rotation/Reversal (1 problem)
- **Rotate Array:** Triple reversal technique

**Core Principle:** Use reversals for in-place rotation  
**Benefit:** O(1) space vs O(n) with extra array

---

## 📈 COMPLEXITY COMPARISON CHART

| Problem | Your Solution | Optimal Solution | Improvement |
|---------|--------------|------------------|-------------|
| Add Digits | O(d) time, O(d) sp | O(1) time, O(1) sp | ⚡ Time & Space |
| Count Vowels | O(n) time, O(1) sp | O(n) time, O(1) sp | ✨ Minor |
| FizzBuzz | O(n) time, O(n) sp | O(n) time, O(n) sp | ✨ Style |
| Palindrome Number | O(d) time, O(d) sp | O(d) time, O(1) sp | ⚡ Space |
| Valid Anagram | O(n log n), O(n) sp | O(n) time, O(1) sp | ⚡⚡ Time & Space |
| Remove Dups (List) | O(n) time, O(1) sp | O(n) time, O(1) sp | ✅ Perfect |
| Valid Palindrome | O(n) time, O(n) sp | O(n) time, O(1) sp | ⚡ Space |
| Longest Common Prefix | O(S) time, O(m) sp | O(S) time, O(1) sp | ⚡ Space |
| Is Subsequence | O(n) time, O(1) sp | O(n) time, O(1) sp | ✅ Perfect |
| Valid Parentheses | O(n) time, O(n) sp | O(n) time, O(n) sp | ✨ Minor |
| Group Anagrams | O(nk) time, O(nk) sp | O(nk) time, O(nk) sp | ✅ Perfect |
| String Compression | O(n) time, O(1) sp | O(n) time, O(1) sp | ✅ Perfect |
| Two Sum | O(n²) time, O(1) sp | O(n) time, O(n) sp | ⚡⚡ Time (Major) |
| Move Zeroes | O(n²) time, O(1) sp | O(n) time, O(1) sp | ⚡⚡ Time (Major) |
| Majority Element | O(n) time, O(n) sp | O(n) time, O(1) sp | ⚡ Space |
| Intersection Arrays | O(n+m) time, O(n) sp | O(n+m) time, O(n) sp | ✨ Minor |
| Best Time Stock | O(n) time, O(1) sp | O(n) time, O(1) sp | ✅ Perfect |
| Reverse Integer | O(d) time, O(d) sp | O(d) time, O(1) sp | ⚡ Space |
| Remove Min/Max | O(n) time, O(1) sp | O(n) time, O(1) sp | ✨ Constant |
| Rotate Array | O(n) time, O(1) sp | O(n) time, O(1) sp | ✅ Perfect |

**Legend:**
- ✅ Perfect - Already optimal
- ⚡⚡ Major - Significant complexity improvement
- ⚡ Moderate - Space or time improvement
- ✨ Minor - Constant factor or style improvement

---

## 🎯 KEY ALGORITHMIC PATTERNS LEARNED

### PATTERN 1: Mathematical Formulas > Loops
**When to use:** Problems with mathematical invariants  
**Examples:** Digital root, modulo arithmetic  
**Benefit:** O(1) time instead of O(n) loops

### PATTERN 2: Hash Maps > Sorting for Frequency
**When to use:** Counting/frequency problems  
**Examples:** Anagrams, character counts  
**Benefit:** O(n) instead of O(n log n)

### PATTERN 3: Two-Pointer Technique
**When to use:** Arrays, strings, linked lists, subsequences  
**Examples:** Palindromes, removing duplicates, compression  
**Benefit:** O(1) space, single pass, in-place modification

### PATTERN 4: In-Place Modification
**When to use:** When input can be mutated  
**Examples:** Linked list operations, array modifications  
**Benefit:** O(1) space instead of O(n)

### PATTERN 5: Single-Pass Optimization
**When to use:** Multiple metrics needed from same data  
**Examples:** Finding min and max simultaneously  
**Benefit:** Better constants, fewer cache misses

### PATTERN 6: Avoid String Conversion
**When to use:** Number manipulation problems  
**Examples:** Reversing, palindromes, digit operations  
**Benefit:** O(1) space, faster execution

### PATTERN 7: Choose Right Data Structure
**When to use:** Membership testing, lookups, matching  
**Examples:** Set vs List, Dict vs Array, Stack for parentheses  
**Benefit:** O(1) operations instead of O(n)

---

## 🐍 PYTHON-SPECIFIC TIPS

### 1. List Comprehensions
```python
# Before
result = []
for item in items:
    if condition(item):
        result.append(transform(item))

# After
result = [transform(item) for item in items if condition(item)]
```

### 2. Boolean Multiplication
```python
# Trick: Boolean acts as 0 or 1
"String" * True = "String"
"String" * False = ""

# Use case
"Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i)
```

### 3. Built-in Functions
- **Counter:** For frequency counting
- **set():** For O(1) membership
- **enumerate():** For index + value
- **zip():** For parallel iteration
- **any()/all():** For early exit conditions

### 4. Early Return
```python
# Check edge cases first
if not array:
    return 0
if len(array) == 1:
    return array[0]
# Main logic here
```

### 5. Generator Expressions
```python
# Memory efficient
sum(x**2 for x in range(1000000))  # Don't create list
```

---

## ✅ COMMON OPTIMIZATION STRATEGIES

### Space Optimization:
- ✅ Process on-the-fly instead of creating intermediate structures
- ✅ Use pointers instead of creating new arrays/strings
- ✅ Math operations instead of string conversions
- ✅ In-place modification when possible

### Time Optimization:
- ✅ Hash maps for O(1) lookups
- ✅ Single pass instead of multiple iterations
- ✅ Mathematical formulas instead of loops
- ✅ Avoid nested loops when possible
- ✅ Early exit conditions

### Code Quality:
- ✅ List comprehensions for clarity
- ✅ Early returns for edge cases
- ✅ Descriptive variable names
- ✅ Type hints for clarity
- ✅ Comments only where needed

---

## 📚 DIFFICULTY PROGRESSION

### EASY (You've mastered 17) ✓
- ✅ String manipulation basics (compression, prefix, palindrome)
- ✅ Two-pointer fundamentals (subsequence, compression, scanning, move zeroes)
- ✅ Basic hash maps (anagrams, frequency counting, two sum)
- ✅ Linked list basics (remove duplicates)
- ✅ Stack operations (bracket matching)
- ✅ In-place array modification
- ✅ Set operations (intersection)
- ✅ Greedy algorithms (stock profit)

### MEDIUM (You've done 3) ✓
- ✅ Mathematical optimizations
- ✅ Index manipulation
- ✅ Multiple scenario analysis
- ✅ Array rotation techniques

### HARD (Next challenge) 🎯
- → Dynamic programming
- → Graph algorithms (BFS/DFS)
- → Advanced data structures (Trie, Segment Tree)
- → Complex optimization problems

---

## 🎯 NEXT STEPS & GOALS

### IMMEDIATE PRACTICE:
1. More medium problems with hash maps
2. Two-pointer on arrays (not just strings)
3. Sliding window technique
4. Binary search variations
5. Basic dynamic programming

### SKILL GAPS TO FILL:
1. Dynamic programming fundamentals
2. Graph traversal (BFS/DFS)
3. Tree algorithms (traversal, BST operations)
4. Backtracking
5. Greedy algorithms

### OPTIMIZATION CHECKLIST:
Before coding, ask yourself:
- □ Can I use math instead of strings?
- □ Can I use a hash map instead of sorting?
- □ Can I do this in one pass?
- □ Can I avoid creating new data structures?
- □ Is there a mathematical pattern or formula?
- □ Can I use two pointers?
- □ What's the optimal data structure for this operation?
- □ What's the theoretical optimal complexity?

---

## 💭 PERFORMANCE MINDSET

### ALWAYS ASK:
1. What's the bottleneck? (Time or Space?)
2. Am I creating unnecessary copies?
3. Can I combine multiple passes into one?
4. Is there a built-in function for this?
5. What's the theoretical optimal complexity?

### COMMON PITFALLS TO AVOID:
- ❌ String conversion when math works
- ❌ Nested loops without considering hash maps
- ❌ Creating filtered/transformed copies unnecessarily
- ❌ Multiple passes when one suffices
- ❌ List when set is appropriate
- ❌ Checking `in list` in a loop (use set)

### GOOD HABITS:
- ✅ Analyze complexity before coding
- ✅ Consider edge cases early
- ✅ Write clean, readable code first
- ✅ Then optimize if needed
- ✅ Test with various inputs
- ✅ Explain approach before implementing

---

## 🏆 YOUR PROGRESS

### STRENGTHS YOU'VE SHOWN:
- ✅ Good understanding of basic algorithms
- ✅ Correct solutions to all problems
- ✅ Clear code structure
- ✅ Awareness of time/space complexity
- ✅ **4 Perfect solutions** out of 14 (28.6%)

### AREAS FOR IMPROVEMENT:
- → Default to space-efficient solutions
- → Consider mathematical patterns first
- → Use hash maps more for frequency problems
- → Avoid string conversions for number problems
- → Practice single-pass optimizations

### YOUR STATISTICS:
- **6 Perfect solutions** (Remove Duplicates, Is Subsequence, Group Anagrams, String Compression, Best Time to Buy/Sell Stock, Rotate Array) ✅✅
- **5 Near-optimal solutions** (Count Vowels, FizzBuzz, Valid Parentheses, Intersection of Arrays, Remove Min/Max) ✅
- **9 Solutions with optimization opportunities** (45%)
- **Improvement Rate:** 55% optimal/near-optimal on first try!

### NEXT MILESTONE:
- → Achieve 80%+ optimal solutions on first try
- → Recognize patterns faster
- → Master medium-level problems
- → Start tackling hard problems
- → Build strong dynamic programming foundation

---

## 🚀 FINAL THOUGHTS

You've made excellent progress! You have:
- ✅ Solved 20 problems across different patterns
- ✅ Achieved 6 perfect optimal solutions on first try
- ✅ Demonstrated understanding of core data structures
- ✅ Shown ability to analyze complexity
- ✅ 55% optimal/near-optimal rate - great improvement!

**Keep practicing!** Every problem teaches a new pattern. Focus on:
1. **Recognizing patterns faster** - You'll start seeing similar problems
2. **Hash maps for O(n²) → O(n)** - Two Sum is a classic example
3. **Avoid mutation during iteration** - Move Zeroes lesson
4. **Mathematical thinking** - Look for formulas before loops
5. **Medium problems** - Build confidence with harder challenges

**Remember:** The goal isn't just to solve problems, but to recognize patterns and apply optimal solutions naturally. You're on the right track! 🎉

**New Patterns Learned:**
- ✅ Hash map for complement lookup (Two Sum)
- ✅ Two-pointer swap technique (Move Zeroes)
- ✅ Boyer-Moore voting algorithm (Majority Element)
- ✅ Triple reversal for rotation (Rotate Array)
- ✅ Greedy single-pass tracking (Best Time to Buy/Sell Stock)

---

**Happy Coding! 💻✨**
