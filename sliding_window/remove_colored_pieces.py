
# LeetCdoe No. 2038. Remove Colored Pieces if Both Neighbors are the Same Color
# Problem Statement:

# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece. Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first. Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'. Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'. Alice and Bob cannot remove pieces from the edge of the line. If a player cannot make a move on their turn, that player loses and the other player wins. Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

# Example 1: Input: colors = "AAABABB" Output: true

# Example 2: Input: colors = "AA" Output: false
# Explanation: Alice has her turn first.There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.Thus, Bob wins, so return false.

# Example 3: Input: colors = "ABBBBBBBAAA" Output: false
# Explanation: ABBBBBBBAAA -> ABBBBBBBAA, Alice moves first. Her only option is to remove the second to last 'A' from the right. ABBBBBBBAA -> ABBBBBBAA. Next is Bob's turn. He has many options for which 'B' piece to remove. He can pick any.On Alice's second turn, she has no more pieces that she can remove. Thus, Bob wins, so return false.
 

# Constraints: 1 <= colors.length <= 105, colors consists of only the letters 'A' and 'B'

# Solution:

# Intuition:
# The problem is essentially asking if Alice can make more moves (consecutive substrings of her color) than Bob in the given string of colors. To do this, we need to keep track of the number of consecutive colors chosen by Alice and Bob as we iterate through the string. If Alice can make more moves than Bob, she wins; otherwise, she loses.

# Approach:

# Initialize two variables alice and bob to keep track of the count of consecutive colors chosen by Alice and Bob, respectively. Start both counts at 0. Initialize a variable left to 0. This variable represents the left index of the current consecutive substring.Iterate through the colors string using a right pointer, starting from index 0 and moving to the right.Check if the color at the current left index is different from the color at the current right index. If they are different, it means the current consecutive substring has ended, and we update the left index to the current right index, effectively starting a new consecutive substring.Calculate the value of extra as right - left + 1 - 2. This value represents the number of additional moves that can be made in the current consecutive substring. We subtract 2 because Alice and Bob each start with one move.If extra is greater than 0, it means there are additional moves that can be made in the current consecutive substring. Check the color at the current right index: 
# If the color is "A," increment the alice count by 1
# If the color is "B," increment the bob count by 1
# Continue this process for all substrings in the colors string.
# After iterating through the entire string, compare the alice and bob counts. If alice has made more moves (consecutive substrings), return True, indicating that Alice wins. Otherwise, return False, indicating that Alice loses.

# In summary, this approach keeps track of consecutive substrings of the same color chosen by Alice and Bob while iterating through the colors string. It calculates the number of additional moves in each substring and updates the counts for Alice and Bob accordingly. Finally, it checks if Alice has made more moves than Bob to determine the winner.



def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        left = 0
        # two pointers approach
        # we use sliding window algorithm here 
        for right in range(len(colors)):
            if colors[left] != colors[right]:
                left = right
            #extra: size of the window: 
            extra = right - left + 1 - 2
            if extra > 0:
                if colors[right] == "A":
                    alice += 1
                if colors[right] == "B":
                    bob += 1
        return alice > bob    

if __name__ == "__main__":
    import doctest

    doctest.testmod()
            
