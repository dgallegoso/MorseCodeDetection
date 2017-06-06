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
WORDB = "-1"
DOT = '1'
DASH = '2'

def morse_to_english(secrets, dic):
	secrets = "".join([str(s) for s in secrets])
	result = []
	words = secrets.split(WORDB)
	msg = ""
	for word in words:
		msg += translate_word(word, dic)
		msg += " "
	
	return msg

def translate_word(secrets, dic):
	letters = secrets.split(SPACE)
	word = ""
	for letter in letters:
		word += lookup(letter, dic)

	return word
	


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


