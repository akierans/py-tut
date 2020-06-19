from nose.tools import *
from ex49 import parser
from ex49 import lexicon
from copy import deepcopy

def test_peek():
	assert_equal(parser.peek(lexicon.scan("north south east west")), "direction")
	assert_equal(parser.peek(lexicon.scan("moo ias blargh")), 'error')
	result = parser.peek(lexicon.scan("north, south, east, west, up, downn, left, right"))
	assert_equal(result, [('direction', 'north'),
							('direction', 'south'),
							('direction', 'east'),
							('direction', 'west'),
							('direction', 'up'),
							('direction', 'left'),
							('direction', 'right')])


def test_match():
 	assert_equal(parser.match(lexicon.scan("kill stop bear"), "verb"), ('verb', 'kill'))
# 	assert_equal(parser.match(lexicon.scan("kill stop bear"), "stop"), None)

