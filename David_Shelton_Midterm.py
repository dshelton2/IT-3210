import sys, os, random, time
from subprocess import call
from threading import Timer

# David Shelton - Intro to Scripting

score = 60
run = True
speed = 1.0
y = 1
guys = 3
word_file = sys.argv[1]
words_list = []

def start():
	print """
		Welcome to Roy G. Biv Light Speed Type Racer!
		The letters in "Roy G. Biv" stand for the colors
		of the rainbow: Red, Orange, Yellow, Green, Blue,
		Indigo, and Violet.
		
		Race against the speed timer to gain points and 
		progress to harder, faster levels. Can you make
		it across the rainbow??
		"""
	raw_input("Press Enter to begin: ")
	os.system('cls')
	
def GenList():
	in_file = open(word_file, 'r')
	words = in_file.readlines()
	for i in range(len(words)):
		words_list.append(words[i].strip('\n'))
	in_file.close()
	
def event(string):
	for i in('20','30','40','50','60','70','80','90','a0','b0','c0','d0','e0', '5f'):
		call('cls', shell=True)
		call('color ' + i, shell=True)
		print string
		time.sleep(0.3)	
	
def RandomWord():
	global y, t
	word = random.choice(words_list)
	y = len(word)
	wordspeed = y * speed
	t = Timer(wordspeed, TimesUp)		
	t.start()
	LevelPlay(word)
	
def done():
	print "Your score was : %d" % score
	raw_input()
	event('R.I.P.')
	
def LevelPlay(word):
	print "%35s" % word
	entered = raw_input("Type the word above: ")
	IsItRight(word, entered)
		
def IsItRight(word, x):
	if run != False and word == x:
		t.cancel()
		global score
		score += 1
		print "Score: %d" % score
		BoardColors(score)
	elif run != False and word != x:
		print "\nSorry, you spelled it wrong!"
		UseContinue()
	else:
		pass
		
def UseContinue():
	global guys, run
	t.cancel()
	 
	if guys > 0 :
		again = raw_input ("\nUse a Continue? (%d remaining) y/n: " % guys)
		if again == 'y' and guys > 0:
			guys -= 1
			run = True
			print "\r"
			RandomWord()
		else:
			guys = 0
			print 'Too Bad!! You Die Now!!'
			run = False
			done()
	else:
		print 'Too Bad!! You Die Now!!'
		run = False
		done()
		
def TimesUp():
	global run
	run = False
	print "\nSorry, Time's up! "
	UseContinue()
	
def BoardColors(score):
	a = "You made it to the next level! The timer speeds up!\n"	
	global speed
	if score == 0:
		event('Welcome to Level 1: Red!')
		call('color 0c', shell=True) # RED bg black text red
		RandomWord()
	elif score <= 9:
		RandomWord()
	elif score ==10:
		event(a + "Welcome to Level 2: Orange\n")
		call('color ec', shell=True) # ORANGE bg yellow text red
		speed = 0.9
		RandomWord()
	elif score <=19:
		RandomWord()
	elif score ==20:
		event(a + "Welcome to Level 3: Yellow\n")
		call('color 0e', shell=True) # YELLOW bg black text yellow	
		speed = 0.8
		RandomWord()
	elif score <=29:
		RandomWord()	
	elif score ==30:
		event(a + "Welcome to Level 4: Green\n")
		call('color 0a', shell=True) # GREEN bg black text green
		speed = 0.7
		RandomWord()
	elif score <=39:
		RandomWord()
	elif score ==40:
		event(a + "Welcome to Level 5: Blue\n")
		call('color 81', shell=True) # BLUE bg dk gray text blue	
		speed = 0.6
		RandomWord()
	elif score <=49:
		RandomWord()
	elif score ==50:
		event(a + "Welcome to Level 6: Indigo\n")
		call('color 0b', shell=True) # INDIGO bg black text indigo(lt blue)
		speed = 0.5
		RandomWord()
	elif score <=59:
		RandomWord()
	elif score ==60:
		event("If you made it here...You're fast!!Welcome to The Next Level: Violet\n")
		call('color 0d', shell=True) # VIOLET bg black text violet(lt purple)
		speed = 0.4
		RandomWord()
	elif score <= 69:
		RandomWord()	
	elif score ==70:
		event("Super speeds ahead, How long can you last??\n3 Bonus Continues Awarded!!\nWelcome to The Final Level: UltraViolet\n")
		call('color d0', shell=True) # UltraViolet VIOLET bg Violet text Black
		speed = 0.3
		global guys
		guys += 3
		RandomWord()
	elif score > 70:
		RandomWord()	
	else:
		print 'Error!'

t = Timer(None, TimesUp)		

GenList()
start()
while run!= False:
	BoardColors(score)
	

	