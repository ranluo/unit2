Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_word(fn):
	import os.path
	if os.path.isfile(fn):
		with open(fn, 'r') as fh:
			text = fh.read()
			char_list = [',', '.', ';', '(', ')', '!', '?', '\t',
                                     '\n', '\"', '\'', '/', '\\',':']
			for each_char in char_list:
                            text = text.replace(each_char, ' ')
                        words = text.split()
			word_counts = len(words)
	return word_counts
    count_word('C:/Users/HP/Desktop/SES2020spring/unit2/readme.md')
