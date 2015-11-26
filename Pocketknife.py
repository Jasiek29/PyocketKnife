from pocket import *



kluczyk = Key("kungwokallkargt")
teststr = "west was raised in a middle class household in Chicago  Illinois  and began rapping in the third grade becoming involved in the city s hip hop scene  West attended art school for one semester before dropping out to pursue music entirely in the late Although his real desire was to become a rapper record executives did not take West seriously viewing him as a producer first and foremost After being signed to Roc A Fella in  West released his debut album The College Dropout in to commercial and critical acclaim The baroque inspired Late Registration followed in  and Graduation in  West switched rapping for singing on his emotive effort  Heartbreak and embraced maximalism on s My Beautiful Dark Twisted Fantasy Following several collaborations West released his sixth album"
teststr = teststr.lower()
passwd = teststr.split()
rezult = encode_it(passwd,kluczyk)
strr = " ".join(rezult)

gravity = "NLMXQWWN IIZ LZFNF "
pock = PocketKnife(gravity)
print pock
print pock.Kasiski()


pock.prototype(7)



