class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currDir = [0, 1]
        currCoord = [0, 0]
        for i in instructions:
            currCoord = self.roboMove(currDir, i, currCoord)
            currDir = self.roboDirection(currDir, i)

        if currCoord == [0, 0] or currDir != [0, 1]:
            return True
        else:
            return False

    def roboMove(self, currDirection, instruction, coordinate):
        if instruction != 'G':
            return coordinate

        newcoordinate = [0, 0]
        newcoordinate[0] = coordinate[0] + currDirection[0] * 1
        newcoordinate[1] = coordinate[1] + currDirection[1] * 1

        return newcoordinate

    def roboDirection(self, currDirection, instruction):
        if instruction != "L" and instruction != "R":
            return currDirection

        newDirection = [0] * 2
        if instruction == 'L':
            newDirection[0], newDirection[1] = currDirection[1] * -1, currDirection[0]
        if instruction == 'R':
            newDirection[0], newDirection[1] = currDirection[1], currDirection[0] * -1

        return newDirection


X = Solution()
print(X.isRobotBounded('GGLLGG'))

