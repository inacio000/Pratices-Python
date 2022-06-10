from ClassMonkey import Monkey
from cabecalho import cabecalho


cabecalho('MONKEY 1')
m1 = Monkey('Monkey1')
m2 = Monkey('Monkey2')

m1.eat('Banana')
m1.see_stomach()

m1.eat('Mango')
m1.see_stomach()

m1.eat('Bread')
m1.see_stomach()
m1.digest_stomach()
m1.see_stomach()

cabecalho('MONKEY 2')
m2.eat('Apple')
m2.eat('Banana')
m2.eat(m1)
m2.see_stomach()
