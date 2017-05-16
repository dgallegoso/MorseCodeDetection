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
test = [1,1,1,1,0,1,0,1,2,1,1,0,1,2,1,1,0,2,2,2]

def morse_to_english(secrets):
	secrets = "".join([str(s) for s in secrets])
	result = []
	letters = secrets.split(SPACE)
	result = [lookup("".join(l)) for l in letters]
	print "".join(result)
	


"""check if sequence is a valid morse code letter
letter is a string of {0, 1, 2}"""
def lookup(letter):
	letter = letter.replace(DOT, ".")
	letter = letter.replace(DASH, "-")
	if letter in dic:
		return dic[letter]
	else:
		return False


morse_to_english(test)
