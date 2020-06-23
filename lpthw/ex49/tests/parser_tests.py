from nose.tools import *
from ex49 import parser
from ex49 import lexicon
from copy import deepcopy

def test_peek():
	assert_equal(parser.peek(lexicon.scan("north south east west")), "direction")
	assert_equal(parser.peek(lexicon.scan("moo ias blargh")), 'error')
	#result = parser.peek(lexicon.scan("north, south, "))
	result = parser.peek(lexicon.scan("north south east west up downn left right"))
	assert_equal(result, 'direction')

def test_match():
 	assert_equal(parser.match(lexicon.scan("kill stop bear"), "verb"), ('verb', 'kill'))
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
	assert_raises(Exception, parser.parse_object, lexicon.scan("go in the north"))