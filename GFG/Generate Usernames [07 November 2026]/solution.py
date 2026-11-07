class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)    
        assigned = set()         
        next_suffix = {}      
        ans = []

        for name in arr:
            if name not in assigned:
                assigned.add(name)
                ans.append(name)
                continue

            k = next_suffix.get(name, 1)
            while (name + str(k)) in reserved or (name + str(k)) in assigned:
                k += 1

            new_name = name + str(k)
            assigned.add(new_name)
            next_suffix[name] = k + 1
            ans.append(new_name)

        return ans
