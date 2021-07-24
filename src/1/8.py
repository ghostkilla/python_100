def cipher(str):
	cryp_chars = [chr(219 - ord(char)) if char.islower() else char for char in str]
	return ''.join(cryp_chars)
	
message = 'cuz in his arms'
crypted_message = cipher(message)
print('暗号化：', crypted_message)

composited_message = cipher(crypted_message)
print('複合化：', composited_message)

