class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        table = dict(zip(alpha, morse))
        
        translates = set()
        
        for word in words:
            trans = ""
            for char in word:
                trans += table[char]
            translates.add(trans)
            
        
        return len(translates)