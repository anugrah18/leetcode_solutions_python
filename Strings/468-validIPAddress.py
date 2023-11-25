class Solution:
    def validateIP4(self, IP):
        address = IP.split('.')
        for item in address:
            if not item.isnumeric():
                return "Neither"
            if int(item) > 255:
                return "Neither"
            if len(item) != 1 and item[0] == "0":
                return "Neither"

        return "IPv4"

    def validateIP6(self, IP):
        address = IP.split(':')
        Hexa = "0123456789ABCDEFabcdef"
        for item in address:
            if len(item) < 1 or len(item) > 4:
                return "Neither"
            for c in item:
                if c not in Hexa:
                    return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        if len(IP.split('.')) == 4:
            return self.validateIP4(IP)
        elif len(IP.split(':')) == 8:
            return self.validateIP6(IP)
        else:
            return "Neither"


X = Solution()
print(X.validIPAddress("192.168.0.1"))

# Time complexity : O(N)
# Space complexity : O(1)