import codecs, arff, sys
import unicodecsv as csv
from itertools import izip
from nltk.tokenize import RegexpTokenizer
import nltk.data
from encodings.utf_8 import decode
words_count = []    # lista me ton arithmo twn leksewn ana keimeno
word = []   # lista me tis lekseis ana keimeno
spaces_count = []   # lista gia metrima twn kenwn
textClass = []
symbols_count = []  # lista gia metrimo twn symbolwn
symbols_count_per_char = []
avg_sentences_chars = []  # lista gia meso oro protasewn os pros toy xarakthres
avg_sentences_words = []  # lista gia meso oro protasewn os pros tis lekseis
upper_count = []    # lista gia metrima twn kefalaiwn grammatwn
upper_count_per_char = []
avg_word_len = []   # lista gia metrima toy mesou orou toy mhkous twn leksewn
letters_count = []  # lista gia to metrina twn grammatwn
letters_count_per_char = []
short_words_counter = []    # lista gia to metrima twn mikrwn leksewn (<4)

text_len = []   # megethos string toy katharoy keimenou (grammata, arithmoi, kena, symvola, ola)
total_chars_in_words = []   # total number of chars in word
text = []   # lista gia to katharo keimeno
ids = []    # lista gia ta ids
temp = []

file_path = raw_input("Give dataset's path")
sample_read = csv.reader(open(file_path,"rb")) # anoigma to dataset csv

# orisw san list ta slang gia kathe ethnikothta
slang_freq_US = []
slang_US=['ace','airhead','ammo','antifreeze','armpit','barf','bashed','beemer','bench',
'bent','blade','blimp','bombed','bonkers','booze','buck','bummed','bummer','bust','call','carb','cheesy',
'chicken','chintzy','clip','clunker','collar','con','cool','cop','cram','croak','cruise','cuffs','cushy',
'cut','deck','dicey','ditch','dope','dork','dough','drag','earful','eat','flaky','flashback','fox','foxy',
'freebie','gigglitch','glitzy','goof','goofy','grand','gravy','groovy','gross','grub','grungy','gut',
'guts','honcho','huffy','hustle','hyped','intense','jam','jock','joint','junkie','kegger','kick','klutz',
'knock','kook','lame','loser','mega','megabucks','mellow','mush','nark','neat','nip','nuke','nut','pad','paw',
'peanuutss','pickeld','prod','puke','quarterback','rack','racket','rag','rathole','sack','scam','scarf',
'spook','spud','square','stink','sucker','totaled','vibes','wad','whiz','wussy','zapped']
slang_freq_AUS=[]
slang_AUS=['prawn','kayfa','goon','mate','legit','blunnies','barbie','footy','bogan','ravo','chigger',
'booner','derro','jackaroo','dag','sheila','sanga','wuss','sickie','dob','woomera','cockie','trackies','arvo',
'chockers','esky','grommet','mozzie','pash','roo','servo','slab','sook','togs','ute','whinge','Thongs','plonk',
'dunny','Aboriginal','Aggro','avo','arvo','allophone','barchelor','Bytown','Canuck','chesterfield','chinook',
'dayliner','droke','eh','Gostapo','Grit','grit','humidex','hydro','loonie','parkade','pickerel','pogey',
'serviette','snowbird','toonie','toque','washroom']
slang_freq_CAN=[]
slang_CAN=['beaver','biffy','boonies','can'
'canuck','caper','chinook','click','cougar','diss','eh','emo','flat','frog','gino'
'gorby','grit','habs','hammered','heifer','hick','hoodie','hosed','housecoat','huck'
'humidex','hydro','islander','java','jib','kokanee','loonie','maritimer','mickey'
'mountie','parkade','pissed','pogle','poutine','puck','rad','randy','rez','saskabush'
'sasquatch','serviette','skid','skookum','snowbirds','spinny','spudhead','stagette'
'steeltown','stinktown','tad','toboggan','tuque','washroom','winterpeg','zed']
slang_freq_GBR=[]
slang_GBR=['Tosser','Cock-up','Bloody','Blimey','Wanker','Gutted','Bespoke','Chuffed'
'Fancy','Fortnight','Sorted','Hoover','Kip','Dodgy','Wonky','Wicked','Whinge'
'Tad','Tenner','Fiver','Skive','Toff','Punter','Scouser','Quid','Taking','Nicked'
'Nutter','Knackered','Gobsmacked','Chap','Bugger','Bog Roll','Pants','Throw','zed'
'Absobloodylootely','Nosh','Shambles','Brilliant','DIY','Fit','Arse','Shag','Fanny'
'Bollocks','Ponce','Bangers','Chips','Uni','Starkers','Smeg','Anorak','Shambles'
'Plastered','Knob','Chav','Ace','Plonker','Dobber','BellEnd','Blighty','Rubbish']

hits_US = { 'deck':0, 'bombed':0, 'booze':0, 'huffy':0, 'dough':0, 'hyped':0, 'cruise':0, 'klutz':0, 'chicken':0, 'jock':0, 'bummed':0, 'cut':0, 'cuffs':0, 'guts':0, 'bust':0, 'bench':0, 'jam':0, 'bummer':0, 'kick':0, 'goof':0, 'sucker':0, 'dope':0, 'joint':0, 'zapped':0, 'spook':0, 'cool':0, 'knock':0, 'megabucks':0, 'airhead':0, 'loser':0, 'vibes':0, 'goofy':0, 'gut':0, 'rack':0, 'bonkers':0, 'square':0, 'grub':0, 'nut':0, 'junkie':0, 'antifreeze':0, 'whiz':0, 'barf':0, 'racket':0, 'flashback':0, 'gross':0, 'fox':0, 'prod':0, 'hustle':0, 'kook':0, 'honcho':0, 'wussy':0, 'carb':0, 'intense':0, 'dork':0, 'dicey':0, 'cop':0, 'mega':0, 'blimp':0, 'flaky':0, 'armpit':0, 'ammo':0, 'croak':0, 'cushy':0, 'sack':0, 'kegger':0, 'gigglitch':0, 'ditch':0, 'cheesy':0, 'nuke':0, 'wad':0, 'puke':0, 'call':0, 'freebie':0, 'cram':0, 'mush':0, 'buck':0, 'grungy':0, 'mellow':0, 'glitzy':0, 'chintzy':0, 'eat':0, 'groovy':0, 'bashed':0, 'ace':0, 'blade':0, 'beemer':0, 'neat':0, 'rag':0, 'stink':0, 'scam':0, 'bent':0, 'clip':0, 'earful':0, 'clunker':0, 'totaled':0, 'rathole':0, 'peanuutss':0, 'lame':0, 'pickeld':0, 'foxy':0, 'pad':0, 'nark':0, 'grand':0, 'spud':0, 'quarterback':0, 'gravy':0, 'drag':0, 'nip':0, 'collar':0, 'paw':0, 'scarf':0, 'con':0 }
hits_AUS = { 'sheila':0, 'esky':0, 'toonie':0, 'chockers':0, 'roo':0, 'sook':0, 'pash':0, 'prawn':0, 'jackaroo':0, 'parkade':0, 'ravo':0, 'thongs':0, 'bogan':0, 'trackies':0, 'grit':0, 'slab':0, 'eh':0, 'cockie':0, 'kayfa':0, 'arvo':0, 'grommet':0, 'barbie':0, 'dayliner':0, 'woomera':0, 'avo':0, 'derro':0, 'aboriginal':0, 'mate':0, 'mozzie':0, 'sickie':0, 'allophone':0, 'droke':0, 'pogey':0, 'wuss':0, 'canuck':0, 'washroom':0, 'pickerel':0, 'dag':0, 'barchelor':0, 'servo':0, 'goon':0, 'togs':0, 'toque':0, 'humidex':0, 'gostapo':0, 'serviette':0, 'aggro':0, 'blunnies':0, 'chigger':0, 'hydro':0, 'grit':0, 'chinook':0, 'legit':0, 'snowbird':0, 'whinge':0, 'ute':0, 'footy':0, 'bytown':0, 'loonie':0, 'booner':0, 'dob':0, 'plonk':0, 'chesterfield':0, 'sanga':0, 'dunny':0 }
hits_GBR = { 'starkers':0, 'fit':0, 'ponce':0, 'anorak':0, 'shambles':0, 'hoover':0, 'wonky':0, 'rubbish':0, 'dodgy':0, 'arse':0, 'taking':0, 'bog roll':0, 'gutted':0, 'whingetad':0, 'bespoke':0, 'nickednutter':0, 'skive':0, 'bugger':0, 'fiver':0, 'smeg':0, 'chips':0, 'chuffedfancy':0, 'bloody':0, 'fortnight':0, 'fannybollocks':0, 'gobsmacked':0, 'shag':0, 'bangers':0, 'tenner':0, 'shamblesplastered':0, 'quid':0, 'punter':0, 'diy':0, 'wicked':0, 'knob':0, 'blighty':0, 'zedabsobloodylootely':0, 'blimey':0, 'kip':0, 'dobber':0, 'sorted':0, 'pants':0, 'throw':0, 'plonker':0, 'ace':0, 'brilliant':0, 'tosser':0, 'scouser':0, 'nosh':0, 'uni':0, 'bellend':0, 'wanker':0, 'chap':0, 'chav':0, 'cock-up':0, 'toff':0, 'knackered':0 }
hits_CAN = { 'diss':0, 'pogle':0, 'puck':0, 'saskabushsasquatch':0, 'housecoat':0, 'serviette':0, 'skid':0, 'caper':0, 'jib':0, 'zed':0, 'maritimer':0, 'hammered':0, 'frog':0, 'cougar':0, 'randy':0, 'hydro':0, 'washroom':0, 'flat':0, 'grit':0, 'ginogorby':0, 'toboggan':0, 'mickeymountie':0, 'poutine':0, 'biffy':0, 'emo':0, 'loonie':0, 'hosed':0, 'kokanee':0, 'chinook':0, 'skookum':0, 'huckhumidex':0, 'rad':0, 'eh':0, 'parkade':0, 'tad':0, 'beaver':0, 'click':0, 'stinktown':0, 'hick':0, 'rez':0, 'tuque':0, 'spudhead':0, 'islander':0, 'habs':0, 'spinny':0, 'cancanuck':0, 'hoodie':0, 'java':0, 'pissed':0, 'winterpeg':0, 'heifer':0, 'stagettesteeltown':0, 'snowbirds':0, 'boonies':0 }


total_diff_words = []
hapax_legomena = []
hapax_dislegomena = []
freq_word = []
write = codecs.open("text", "wb", "utf-8")
write_open = codecs.open("text", "rb", "utf-8")
nation = []


text_US=[]
text_AUS=[]
text_GBR=[]
text_CAN = []
text_NNS  =[]

# synarthsh pou dhmiourgei lista me to katharo keimeno ana ethnikothta
def freq_words_nationality(l):

    #write = codecs.open("text", "wb", "utf-8")
    #write_open = codecs.open("text", "rb", "utf-8")
    for q in l:
        write.write(q)
    stopwords = set(nltk.corpus.stopwords.words('english'))
    temp = write_open.read().replace('\n', ' ')
    temp1 = RegexpTokenizer(r'\w+').tokenize(temp)
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in temp1 if w not in stopwords)

    return allWordExceptStopDist

def str2float_lst(lst):
    for i in range(len(lst)):
        lst[i]=float(lst[i])
    return lst


# synarthsh h opoia epistrefei to pososto tou keimenou pou emperiexei tis lekseis
# ths listas pou dinw ws orisma
def national_commons_per_doc(text_nation, string_list):
    counter = 0.00
    for j in string_list:
        counter += text_nation.count(j.lower())
    if counter!=0:
        return format(counter/float(len(text_nation)), '.3f')
    else:
        return 0.00

def national_commons_per_doc_hits(text_nation, string_list, nat_str):
    counter = 0.00
    for j in string_list:
		count_word = text_nation.count(j.lower())
        #counter += count_word
		if nat_str == 'us' and count_word:
			hits_US[j.lower()] += count_word
		elif nat_str == 'gbr' and count_word:
			hits_GBR[j.lower()] += count_word
		elif nat_str == 'aus' and count_word:
			hits_AUS[j.lower()] += count_word
		elif nat_str == 'can' and count_word:
			hits_CAN[j.lower()] += count_word

    if counter!=0:
        return format(counter/float(len(text_nation)), '.3f')
    else:
        return 0.00
co = 0
# diavazw to object me to katharo keimeno
print('Dialogi ethnikotitas...')
for row in sample_read:
    # lista me to katharo keimeno
    text.append(row[1])  # pernaw sti lista text to katharo keimeno
    # lista me ta ids twn keimenwn
    ids.append(int(row[0]))  # to antistoixo id
    # lista me ta nationalities twn keimenwn
    nation.append(row[7])
    # antistoixes listes me ta keimena ana nationalities
    if row[7]=='US':
        text_US.append(row[1].encode("ascii", "ignore"))
        textClass.append(0)
    elif row[7]=='AUS':
        text_AUS.append(row[1].encode("ascii", "ignore"))
        textClass.append(1)
    elif row[7]=='CAN':
        text_CAN.append(row[1].encode("ascii", "ignore"))
        textClass.append(2)
    elif row[7]=='UK':
        text_GBR.append(row[1].encode("ascii", "ignore"))
        textClass.append(3)
    else:
        textClass.append(4)
        text_NNS.append(row[1].encode("ascii", "ignore"))
    temp = float(co)/7100.00
    sys.stdout.write("\r completed: %.1f %%" %temp )
    sys.stdout.flush()
    co = co + 1


del sample_read
print('DONE!')
print 'megethos dataset: ', len(text)
print('Most used words processing...')
freq_words_US = freq_words_nationality(text_US)
del text_US
print('US DONE!')
freq_words_AUS = freq_words_nationality(text_AUS)
del text_AUS
print('AUS DONE!')
freq_words_CAN = freq_words_nationality(text_CAN)
del text_CAN
print('CAN DONE!')
freq_words_GBR = freq_words_nationality(text_GBR)
del text_GBR
print('UK DONE!')
freq_words_NNS = freq_words_nationality(text_NNS)
del text_NNS, temp
print('NNS DONE')
print('Removing commons words...')
# vriskw ta keina most commons words
commons = set(freq_words_US)&set(freq_words_AUS)&set(freq_words_GBR)&set(freq_words_CAN)&set(freq_words_NNS)
for j in commons:
    # kai ta svinw apo oles tis listes
    del freq_words_US[j]
    del freq_words_AUS[j]
    del freq_words_CAN[j]
    del freq_words_GBR[j]
    del freq_words_NNS[j]
del commons
print('DONE!')
# apo afta krataw ta 20 most commons
freq_words_US=freq_words_US.most_common(75)

freq_words_AUS=freq_words_AUS.most_common(75)

freq_words_CAN=freq_words_CAN.most_common(75)

freq_words_GBR=freq_words_GBR.most_common(75)

freq_words_NNS=freq_words_NNS.most_common(75)


#kai apo ta antistoixa krataw mono tis lekseis xwris to value
freq_US=[]
for i,j in freq_words_US:
    freq_US.append(i.encode("ascii","ignore"))
del freq_words_US
print freq_US
freq_CAN=[]
for i,j in freq_words_CAN:
    freq_CAN.append(i.encode("ascii","ignore"))
del freq_words_CAN
print freq_CAN
freq_AUS=[]
for i,j in freq_words_AUS:
    freq_AUS.append(i.encode("ascii","ignore"))
del freq_words_AUS
print freq_AUS
freq_GBR=[]
for i,j in freq_words_GBR:
    freq_GBR.append(i.encode("ascii","ignore"))
del freq_words_GBR
print freq_GBR
freq_NNS=[]
for i,j in freq_words_NNS:
    freq_NNS.append(i.encode("ascii","ignore"))
del freq_words_NNS
print freq_NNS
most_used_words_US=[]
most_used_words_AUS=[]
most_used_words_CAN=[]
most_used_words_NNS=[]
most_used_words_GBR=[]


punctuations_count_per_char = []
spaces_count_per_char = []
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
i=[]
print('Basic feature processing...')
for i in range(len(text)):
    # ypologismos arithmou xarakthrwn ana keimeno
    # ypologismos toy arithmou twn symvolwn ana keimeno

    # eisagwgh sth word twn leksewn ana keimeno
    word_tmp = RegexpTokenizer(r'\w+').tokenize(text[i])
    [x.lower() for x in word_tmp]
    word.append(word_tmp)


    # ypologizw ta most used words gia kathe ethnikothta
    most_used_words_US.append(national_commons_per_doc(word[i], freq_US))
    most_used_words_CAN.append(national_commons_per_doc(word[i], freq_CAN))
    most_used_words_GBR.append(national_commons_per_doc(word[i], freq_GBR))
    most_used_words_AUS.append(national_commons_per_doc(word[i], freq_AUS))
    most_used_words_NNS.append(national_commons_per_doc(word[i], freq_NNS))
    slang_freq_US.append(national_commons_per_doc_hits(word[i], slang_US, 'us'))
    slang_freq_CAN.append(national_commons_per_doc_hits(word[i], slang_CAN, 'can'))
    slang_freq_AUS.append(national_commons_per_doc_hits(word[i], slang_AUS, 'aus'))
    slang_freq_GBR.append(national_commons_per_doc_hits(word[i], slang_GBR, 'gbr'))


    temp = i/float(len(text))*100
    sys.stdout.write("\rCompleted: %.1f %%" % temp)
    sys.stdout.flush()
print('DONE!')
del freq_AUS, freq_CAN, freq_GBR, freq_NNS, freq_US, freq_word, slang_AUS, slang_CAN, slang_GBR, slang_US
del word, i, words_count

print '---------\nUS slang hits:'
for i in hits_US:
	if hits_US[i]:
		print i + ': ' + str(hits_US[i])
del i
print '---------\nAUS slang hits:'
for i in hits_AUS:
	if hits_AUS[i]:
		print i + ': ' + str(hits_AUS[i])
del i
print '---------\nCAN slang hits:'
for i in hits_CAN:
	if hits_CAN[i]:
		print i + ': ' + str(hits_CAN[i])
del i
print '---------\nGBR slang hits:'
for i in hits_GBR:
	if hits_GBR[i]:
		print i + ': ' + str(hits_GBR[i])
del i

# ftiaxnw to header gia to csv pou tha eksagw
header = ['most_used_words_US',
          'GBR_most_used_words/doc', 'AUS_most_used_words/doc', 'CAN_most_used_words/doc', 'NNS_most_used_words/doc',
          'US_freq_words/doc', 'GBR_freq_words/doc','AUS_freq_words/doc','CAN_freq_words/doc','class']
print('izip object processing...')
# me izip pernaw sto output ola ta features pou einai pros eggrafh sto csv
output = izip(most_used_words_US,
 most_used_words_GBR, most_used_words_AUS, most_used_words_CAN, most_used_words_NNS,
 slang_freq_US, slang_freq_GBR,slang_freq_AUS,slang_freq_CAN, textClass)
print('DONE!')

del ids, text_len, symbols_count_per_char, punctuations_count_per_char, spaces_count_per_char, textClass
del most_used_words_GBR, most_used_words_AUS, most_used_words_CAN, most_used_words_NNS, most_used_words_US
del slang_freq_US, slang_freq_GBR,slang_freq_AUS,slang_freq_CAN, nation
print('Eggrafi arxeiou arff')
arff.dump("geo-feat.arff", output, relation='results', names=header)
del output, header
print('DONE!')
print('TELOS - BE HAPPY :)')
