fake_dic = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
		'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

dic = {}
for k, v in fake_dic.iteritems():
	dic[v] = k

SPACE = '0'
DOT = '1'
DASH = '2'

def morse_to_english(secrets, dic):
	secrets = "".join([str(s) for s in secrets])
	result = []
	letters = secrets.split(SPACE)
	result = [lookup("".join(l), dic) for l in letters]
	return "".join(result)
	


"""check if sequence is a valid morse code letter
letter is a string of {0, 1, 2}"""
def lookup(letter, dic):
	if len(letter) == 0: return ""
	letter = letter.replace(DOT, ".")
	letter = letter.replace(DASH, "-")
	if letter in dic:
		return dic[letter]
	else:
		print "Could not find {0}".format(letter)
		return "$"


