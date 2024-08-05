class Solution:
    def validateIP4(self, IP):
        # Split the input IP string by '.' to get the components of the IPv4 address
        address = IP.split('.')

        # Iterate through each component of the IPv4 address
        for item in address:
            # Check if the component is numeric
            if not item.isnumeric():
                return "Neither"  # Return "Neither" if it is not numeric

            # Convert the component to an integer and check if it is within the valid range for IPv4 (0-255)
            if int(item) > 255:
                return "Neither"  # Return "Neither" if it exceeds 255

            # Check if the component has leading zeros (invalid in IPv4 except for the number "0")
            if len(item) != 1 and item[0] == "0":
                return "Neither"  # Return "Neither" if there are leading zeros

        return "IPv4"  # Return "IPv4" if all components are valid

    def validateIP6(self, IP):
        # Split the input IP string by ':' to get the components of the IPv6 address
        address = IP.split(':')

        # Define a set of valid hexadecimal characters for IPv6
        Hexa = "0123456789ABCDEFabcdef"

        # Iterate through each component of the IPv6 address
        for item in address:
            # Check if the component length is within the valid range for IPv6 (1-4 characters)
            if len(item) < 1 or len(item) > 4:
                return "Neither"  # Return "Neither" if the length is invalid

            # Check if each character in the component is a valid hexadecimal character
            for c in item:
                if c not in Hexa:
                    return "Neither"  # Return "Neither" if an invalid character is found

        return "IPv6"  # Return "IPv6" if all components are valid

    def validIPAddress(self, IP: str) -> str:
        # Check if the IP string has 4 components when split by '.' (possible IPv4)
        if len(IP.split('.')) == 4:
            return self.validateIP4(IP)  # Validate as IPv4

        # Check if the IP string has 8 components when split by ':' (possible IPv6)
        elif len(IP.split(':')) == 8:
            return self.validateIP6(IP)  # Validate as IPv6

        else:
            return "Neither"  # Return "Neither" if it is neither a valid IPv4 nor IPv6 format


X = Solution()
print(X.validIPAddress("192.168.0.1"))

# Time complexity : O(N)
# Space complexity : O(1)