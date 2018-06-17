# futhark
python class for unicode elder futhark runes


## Example

Instance a new `Futhark` class

	runes = Futhark()

Call some rune

	fehu = runes.FEHU
	print(fehu)

	>>> ᚠ

Print random runes

	runes.rune_play(10)
	>>> ᛇ ᚺ ᚦ ᛞ ᛞ ᛞ ᛖ ᛈ ᛉ ᚠ

Encrypt string to return a runestring

	runencrypt = runes.encrypt("Viking Python")
	print(runencrypt)
	>>> ᚹᛁᚲᛜᛈᛉᚦᛟᚾ


ᚺᚫᚹᛖᚠᚢᚾᛈᛚᚫᛉᛜᚹᛁᚦᛈᛉᚦᛟᚾᚫᚾᛞᚱᚢᚾᛖᛊ