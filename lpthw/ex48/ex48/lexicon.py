directions = {'north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back', 'forward'}
verbs = {'go', 'stop', 'kill', 'eat'}
stop_words = {'the', 'in', 'from', 'of', 'at', 'it'}
nouns = {'door', 'bear', 'princess', 'cabinet'}

def scan(words):
	
	words = words.split()
	sentence = []

	for i in words:
		if i.lower() in directions:
			sentence.append(('direction', i))

		elif i.lower() in verbs:
			sentence.append(('verb', i))

		elif i.lower() in stop_words:
			sentence.append(('stop', i))

		elif i.lower() in nouns:
			sentence.append(('noun', i))
		
		elif i.isdigit():
			sentence.append(('number', convert_number(i)))

		else:
			sentence.append(('error', i))

	return sentence

def convert_number(s):
	try:
		return int(s)

	except ValueError:
		return None