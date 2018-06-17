# -*- coding: UTF-8 -*-

"""
Module futhark for printing unicode runes in prompt.
by: Bruno L. Carli
"""

class Futhark:
	"""
	Futhark class
	contains unicode runic attributes
	printing attribute will reveal a rune
	"""

	# 1 aetter
	FEHU = u"\u16A0"
	URUZ = u"\u16A2"
	THURISAZ = u"\u16A6"
	RAIDO = u"\u16B1"
	ANSUS = u"\u16AB"
	KENAZ = u"\u16B2"
	GEBO = u"\u16B7"
	WUNJO = u"\u16B9"

	# 2 aetter
	HAGALAZ = u"\u16BA"
	NAUDIZ = u"\u16BE"
	ISAZ = u"\u16C1"
	JERA = u"\u16C3"
	EOH = u"\u16C7"
	PEORTH = u"\u16C8"
	ALGIZ = u"\u16C9"
	SOWILO = u"\u16CA"

	# 3 aetter
	TEWAZ = u"\u16CF"
	BERKANA = u"\u16D2"
	EWAZ = u"\u16D6"
	MANNAZ = u"\u16D7"	
	LAGUZ = u"\u16DA"
	INGWAZ = u"\u16DC"
	OTHAL = u"\u16DF"
	DAGAZ = u"\u16DE"

	def rune_play(self, n):
		"""
		Prints a sequence of n random runes

		:param n: <int> n runes to print
		"""

 		runes = [
			self.FEHU,
			self.URUZ,
			self.THURISAZ,
			self.RAIDO,
			self.ANSUS,
			self.KENAZ,
			self.GEBO,
			self.WUNJO,
			self.HAGALAZ,
			self.NAUDIZ,
			self.ISAZ,
			self.JERA,
			self.EOH,
			self.PEORTH,
			self.ALGIZ,
			self.SOWILO,
			self.TEWAZ,
			self.BERKANA,
			self.EWAZ,
			self.MANNAZ,
			self.LAGUZ,
			self.INGWAZ,
			self.OTHAL,
			self.DAGAZ,
		]

		for i in range(n):
			print choice(runes),
		print("")

	def encrypt(self, text):
		"""
		Encrypt a string to runic inscription
		
		:param text: <str> a text to runencrypt
		:rtype: u<str>
		"""

		runestone = {
			"f": self.FEHU,
			"u": self.URUZ,
			"th": self.THURISAZ,
			"r": self.RAIDO,
			"a": self.ANSUS,
			"c": self.KENAZ,
			"q": self.KENAZ,
			"k": self.KENAZ,
			"g": self.GEBO,
			"w": self.WUNJO,
			"v": self.WUNJO,
			"h": self.HAGALAZ,
			"n": self.NAUDIZ,
			"i": self.ISAZ,
			"j": self.JERA,
			"eo": self.EOH,
			"p": self.PEORTH,
			"z": self.ALGIZ,
			"y": self.ALGIZ,
			"s": self.SOWILO,
			"t": self.TEWAZ,
			"b": self.BERKANA,
			"e": self.EWAZ,
			"m": self.MANNAZ,
			"l": self.LAGUZ,
			"ing": self.INGWAZ,
			"o": self.OTHAL,
			"d": self.DAGAZ,
		}

		sygil = ""
		text = [i for i in text.lower()]
		while text:
			i = 0
			if text[i] == "t" and text[i+1] == "h":
				rune = "th"
				sygil += runestone[rune]
				del text[i], text[i]
			elif text[i] == "e" and text[i+1] == "o":
				rune = "eo"
				sygil += runestone[rune]
				del text[i], text[i]
			elif text[i] == "i" and text[i+1] == "n" and text[i+2] == "g":
				rune = "ing"
				sygil = runestone[rune]
				del text[i], text[i], text[i]
			elif text[i] in runestone.keys():
				sygil += runestone[text[i]]
				del text[i]
			else:
				sygil += ""
				del text[i]
			i += 1
		return sygil
