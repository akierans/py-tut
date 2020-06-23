from nose.tools import *
from ex49 import parser
from ex49 import lexicon
from copy import deepcopy

def test_peek():
	assert_equal(parser.peek(lexicon.scan("north south east west")), "direction")
	assert_equal(parser.peek(lexicon.scan("NORTH south east west")), "direction")
	assert_equal(parser.peek(lexicon.scan("moo ias blargh")), 'error')
	#result = parser.peek(lexicon.scan("north, south, "))
	result = parser.peek(lexicon.scan("north south east west up downn left right"))
	assert_equal(result, 'direction')

def test_match():
 	assert_equal(parser.match(lexicon.scan("kill stop bear"), "verb"), ('verb', 'kill'))
 	assert_equal(parser.match(lexicon.scan("Eat kill bear"), "verb"), ('verb', 'Eat'))
 	assert_equal(parser.match(lexicon.scan("kill stop bear"), "stop"), None)
 	assert_equal(parser.match(lexicon.scan("bear walks in woods"), "noun"), ('noun', 'bear'))

def test_pverb():
	assert_equal(parser.parse_verb(lexicon.scan("eat it")), ('verb', 'eat'))
	assert_equal(parser.parse_verb(lexicon.scan("in the eat")), ('verb', 'eat'))
	assert_equal(parser.parse_verb(lexicon.scan("of the kill")), ('verb', 'kill'))
	assert_raises(Exception, parser.parse_verb, lexicon.scan("princess ate the bear"))

def test_pobj():
	assert_equal(parser.parse_object(lexicon.scan("the bear kill")), ('noun', 'bear'))
	assert_equal(parser.parse_object(lexicon.scan("princess in north")), ('noun', 'princess'))
	assert_equal(parser.parse_object(lexicon.scan("PRINCESS in north")), ('noun', 'PRINCESS'))
	assert_equal(parser.parse_object(lexicon.scan("North bear")), ('direction', 'North'))
	assert_equal(parser.parse_object(lexicon.scan("north the princess")), ('direction', 'north'))
	assert_raises(Exception, parser.parse_object, lexicon.scan("go in the north"))

def test_subj():
	assert_equal(parser.parse_subject(lexicon.scan("door in the forest")), ('noun', 'door'))
	assert_equal(parser.parse_subject(lexicon.scan("Door in the forest")), ('noun', 'Door'))
	assert_equal(parser.parse_subject(lexicon.scan("in the cabinet")), ('noun', 'cabinet'))
	assert_equal(parser.parse_subject(lexicon.scan("in the kill cabinet")), ('noun', 'player'))
	assert_equal(parser.parse_subject(lexicon.scan("kill the forest")), ('noun', 'player'))
	assert_equal(parser.parse_subject(lexicon.scan("in the cabinet kill bear")), ('noun', 'cabinet'))
	assert_raises(Exception, parser.parse_subject, lexicon.scan("From the north"))

def parse_sentence():
	return