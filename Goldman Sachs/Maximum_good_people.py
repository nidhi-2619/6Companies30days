class Solution:
    def validation(self, guessedTypes, statements):
        N = len(statements)
        for i, type in enumerate(guessedTypes):
            # We only need to take care the statements of good person
            if type == 1:
                for j in range(N):
                    # This statement is contradicted with our current guess
                    if statements[i][j] != 2 and statements[i][j] != guessedTypes[j]:
                        return False
        return True

    def maximumGood(self, statements: List[List[int]]) -> int:
        N = len(statements)
        ans = 0
        for i in range(1<<N):
            guessedTypes = [int(x) for x in bin(i)[2:].zfill(N)]
            if self.validation(guessedTypes, statements):
                ans = max(ans, sum(guessedTypes))
        return ans