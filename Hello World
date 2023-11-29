import random 
dec = ["=","^",":","~","*","+","_","<",">","'"]
langs = ["English","Indonesian","Japanese","French","Portuguese","Dutch","Filipino","Malay","Korean","Italian","Latin","Arabic","Armenian","Danish","Finnish","German","Hindi","Spanish","Latvian","Irish","Zulu","Greek","Russian","Serbian","Turkish","Kannada","Thai","Swahili","Chinese"]

words = ["Hello World","Halo Dunia","Ohayō Sekai","Bonjour le Monde","Ol"+chr(160)+" Mundo","Hallo Wereld","Kumusta Mundo","Hai Dunia","Annyeong Sesang","Ciao Mondo","Salve Mundi","Marhabaan Bialealam","Barev Ashkharh","Hej Verden","Hei Maailma","Hallo Welt","Namaste Duniya","Hola Mundo","Sveika pasaule","Dia Duit Domhan","Sawubona Mhlaba","Gei"+chr(160)+" sou K"+chr(162)+"sme","Privet Mir","Zdravo Svete","Merhaba Dunya","Namaste Prapancha","Sawasdee Chow Lok","Salamu, Dunia","Nihao Shijie"]

def rndm(to):
  return random.randint(0,to-1)

def decors(func,lang,n,n2,space):
   def wrap():
      print(" "*space+ dec[n]*5 + lang + dec[n]*5)
      func(space,n2)
      print(" "*space+ dec[n]*(10+len(lang))+"\n")
   return wrap
      
def text(x,t):
  print(" "*x+ words[t])
  
for i in range(len(langs)):
   x = rndm(len(dec))
   sp = 20 if i%2 == 0 else 1
   decorated = decors(text,langs[i],x,i,sp)
   decorated()
