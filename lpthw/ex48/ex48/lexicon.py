directions = {' north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back', 'forward'}
verbs = {'go', 'stop', 'kill', 'eat'}
stop_words = {'the', 'in', 'from', 'of', 'at', 'it'}
nouns = {'door', 'bear', 'princess', 'cabinet'}
#numbers = {}

def scan(words):
	
	words = words.split()
	sentence = []

	for i in directions:
		if i in directions:
			sentence.append(('direction', i))

		elif i in verbs:
			sentence.append(('verb', i))

		elif i in stop_words:
			sentence.append(('stop', i))

		elif i in nouns:
			sentence.append(('noun', i))
		else:
			sentence.append(('error', i))

	return sentence