class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
	        return 0
        if x > 0:
	        rev = str(x)
	        rev = rev[::-1]
	        if int(rev) > 2 ** 31:
		        return 0
	        return (int(rev))
        if x < 0:
	        x = x * -1
	        rev = str(x)
	        rev = rev[::-1]
	        if int(rev) > 2 ** 31:
		        return 0
	        return (int(rev) * -1)
        