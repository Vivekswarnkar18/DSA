class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]):

        totalGas = 0
        totalCost = 0

        for val in gas:
            totalGas += val

        for val in cost:
            totalCost += val

        if totalGas < totalCost:
            return -1

        start = 0
        currGas = 0

        for i in range(len(gas)):
            currGas += gas[i] - cost[i]

            if currGas < 0:
                start = i + 1
                currGas = 0

        return start
        