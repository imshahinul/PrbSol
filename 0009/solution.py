class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_string = str(x)
        new_string = ""
        reverse_string = ""
        for letter in input_string.strip():
            new_string = new_string + letter.replace(" ", "")
            reverse_string = letter.replace(" ", "") + reverse_string
        if new_string.lower() == reverse_string.lower():
            return True
        return False