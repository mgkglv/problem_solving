def highest_value_palindrome(s, n, k):
	num = list(s)
	k_needed = 0
	for i in range(n // 2):
		if num[i] != num[n-i-1]:
			k_needed += 1
	if k_needed > k:
		return '-1'
		
	i = 0
	
	for i in range(n//2):
		req = 0
		des = 0
		if num[i] == num[n-i-1]:
			req = 0
			des = 2 if num[i] != '9' else 0
		else:
			req = 1
			des = 1 if max(num[i], num[n-i-1]) == '9' else 2			
		print [req, des, k, k_needed]	
		if k - k_needed >= 2 - req and des == 2:				
			num[i] = num[n-i-1] = '9'
			k -= 2
			k_needed -= req
		elif req > 0:
			num[i] = num[n-i-1] = max(num[i], num[n-i-1])
			k -= 1
			k_needed -= 1

	if n % 2 != 0 and k > 0:
		num[n//2] = '9'
				

	return ''.join(num)
	
	
