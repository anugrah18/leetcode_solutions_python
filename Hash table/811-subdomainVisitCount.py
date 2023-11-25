class Solution:
    def subdomainVisits(self, cpdomains):
        dict = {}
        ans = []
        for cpdomain in cpdomains:
            count, domains = int(cpdomain.split(" ")[0]), cpdomain.split(" ")[1].split(".")
            for i in range(len(domains)):
                if (".".join(domains[i:]) not in dict):
                    dict[".".join(domains[i:])] = 0
                dict[".".join(domains[i:])] += count

        for k in dict:
            ans.append(str(dict[k]) + " " + k)

        return ans




X = Solution()
print(X.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

# Time Complexity : O(N)
# Space Complexity : O(N)

