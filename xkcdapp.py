from flask import Flask, request, render_template
import random
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():

	return render_template('xkcd_index.html')

@app.route('/show_passwords')
def show_passwords():
	args = request.args

	minpass = int(args.get('minpass'))  
	maxpass	= int(args.get('maxpass'))
	minword = int(args.get('minword'))
	maxword = int(args.get('maxword'))

	if 'order' in args:
		nouns = open("templates/static/nouns.txt", "r+")
		verbs = open("templates/static/verbs.txt", "r+")
		adverbs = open("templates/static/adverbs.txt", "r+")
		adjectives = open("templates/static/adjectives.txt", "r+")

		noun_list = []
		verb_list = []
		adverb_list = []
		adj_list = []

		for n in nouns:
			n = n.strip()
			if len(n) > minword and len(n) < maxword:
				noun_list.append(n)

		for v in verbs:
			v = v.strip()
			if len(v) > minword and len(v) < maxword:
				verb_list.append(v)

		for av in adverbs:
			av = av.strip()
			if len(av) > minword and len(av) < maxword:
				adverb_list.append(av)

		for adj in adjectives:
			adj = adj.strip()
			if len(adj) > minword and len(adj) < maxword:
				adj_list.append(adj)
		
		args = request.args

		fnouns = []
		fverbs = []
		fadjs = []
		fadvs = []

		valid = 0
		while valid < 12:

			rnoun = random.randint(0,len(noun_list) - 1)
			rverb = random.randint(0,len(verb_list) - 1)
			radj = random.randint(0,len(adj_list) - 1)
			radv = random.randint(0,len(adverb_list) - 1)
			
			noun = noun_list[rnoun]
			verb = verb_list[rverb]
			adj = adj_list[radj]
			adv = adverb_list[radv]

			while noun_list[rnoun] in fnouns:
				rnoun = random.randint(0,len(noun_list) - 1)
				noun = noun_list[rnoun]
			
			while verb_list[rverb] in fverbs:
				rverb = random.randint(0,len(verb_list) - 1)
				verb = verb_list[rverb]
			
			while adj_list[radj] in fadjs:
				radj = random.randint(0,len(adj_list) - 1)
				adj = adj_list[radj]

			while adverb_list[radv] in fadvs:
				radv = random.randint(0,len(adverb_list) - 1)
				adv = adverb_list[radv]
			
			if 'numsub' in args:
				noun = numsub(noun)
				verb = numsub(verb)
				adj = numsub(adj)
				adv = numsub(adv)

			fnouns.append(noun)
			fverbs.append(verb)
			fadjs.append(adj)
			fadvs.append(adv)

			passlen = (len(noun) + len(verb) + len(adj) + len(adv))
			if passlen < maxpass and passlen > minpass:
				valid += 1
			else:
				fnouns.pop()
				fverbs.pop()
				fadjs.pop()
				fadvs.pop()

		nouns.close()
		verbs.close()
		adverbs.close()
		adjectives.close()

	else:
		words = open("templates/static/words.txt", "r+")
		word_list = []

		for word in words:
			word.strip()
			if len(word) > minword and len(word) < maxword:
				word_list.append(word)

		args = request.args
		print(args)

		fnouns = []
		fverbs = []
		fadjs = []
		fadvs = []

		valid = 0
		while valid < 12:

			rw1 = random.randint(0,len(word_list) - 1)
			rw2 = random.randint(0,len(word_list) - 1)
			rw3 = random.randint(0,len(word_list) - 1)
			rw4 = random.randint(0,len(word_list) - 1)

			word1 = word_list[rw1]
			word2 = word_list[rw2]
			word3 = word_list[rw3]
			word4 = word_list[rw4]

			while word1 in fnouns:
				rw1 = random.randint(0,len(word_list) - 1)
				word1 = word_list[rw1]
			
			while word2 in fverbs:
				rw2 = random.randint(0,len(word_list) - 1)
				word2 = word_list[rw2]
			
			while word3 in fadjs:
				rw3 = random.randint(0,len(word_list) - 1)
				word3 = word_list[rw3]

			while word4 in fadvs:
				rw4 = random.randint(0,len(word_list) - 1)
				word4 = word_list[rw4]
			
			if 'numsub' in args:
				word1 = numsub(word1)
				word2 = numsub(word2)
				word3 = numsub(word3)
				word4 = numsub(word4)

			fnouns.append(word1)
			fverbs.append(word2)
			fadjs.append(word3)
			fadvs.append(word4)

			passlen = (len(word1) + len(word2) + len(word3) + len(word4))
			if passlen < maxpass and passlen > minpass:
				valid += 1
			else:
				fnouns.pop()
				fverbs.pop()
				fadjs.pop()
				fadvs.pop()		

		words.close()

	return render_template('show_passwords.html', nouns=fnouns, verbs=fverbs, adjs=fadjs, advs=fadvs)

def numsub(word):
	for i in range(0, len(word)):
		w = list(word)
		if w[i] == 's':
			w[i] = '$'
		if w[i] == 'e':
			w[i] = '3'
		if w[i] == 'i':
			w[i] = '!'
		if w[i] == 'a':
			w[i] = '@'
		if w[i] == 'o':
			w[i] = '0'
		if w[i] == 'l':
			w[i] = '1'
		word = "".join(w)
	return word


if __name__ == '__main__':
	app.run(debug=True, port=5001)
