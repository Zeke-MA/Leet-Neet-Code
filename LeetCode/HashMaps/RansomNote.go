package hashmaps

/*
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

My solution:
 1. Create a map to store the unique characters found (key = letter, val = occurences)
 2. Populate the map from each letter of the magazine, increment if already seen
 3. Iterate over each letter in the ransomNote and check if was seen in the magazine. If it was, check if there are letters to use.
    If letters are available decrement the value and continue.
 4. If no letter is found or the value is 0 return false
 5. Return true when all letters in the ransom note are used
*/
func CanConstruct(ransomNote string, magazine string) bool {
	availLetters := make(map[string]int)

	for _, letter := range magazine {
		availLetters[string(letter)]++
	}

	for _, ransom := range ransomNote {
		if val, ok := availLetters[string(ransom)]; ok {
			if val == 0 {
				return false
			}
			availLetters[string(ransom)]--
		} else {
			return false
		}
	}
	return true
}
