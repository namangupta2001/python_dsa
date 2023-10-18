# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

# Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

# Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
# Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.







class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_score = 0
        bob_score = 0

        # Iterate through the colors, excluding the edge pieces
        for i in range(1, len(colors) - 1):
            current_color = colors[i]
            prev_color = colors[i - 1]
            next_color = colors[i + 1]

            # Check if Alice can make a move here
            if current_color == 'A' and prev_color == 'A' and next_color == 'A':
                alice_score += 1  # Alice can remove 'A'

            # Check if Bob can make a move here
            elif current_color == 'B' and prev_color == 'B' and next_color == 'B':
                bob_score += 1  # Bob can remove 'B'

        # Determine the winner based on the scores
        return alice_score > bob_score
