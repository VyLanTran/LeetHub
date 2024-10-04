class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1
        prevSum = skill[0] + skill[-1]
        res = 0
        while i < j:
            skill1, skill2 = skill[i], skill[j]
            if skill1 + skill2 != prevSum:
                return -1
            res += skill1 * skill2
            i, j = i + 1, j - 1
        return res            