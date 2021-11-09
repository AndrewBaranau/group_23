# 1. Создать переменную типа String
print('1. Создать переменную типа String')
a = str(input('Input variable type String: '))
print("You input variable type string and this is: ", a)
print('===================================================================')
# ======================================================================
# 2. Создать переменную типа Integer
print('2. Создать переменную типа Integer')
b = int(input('Input variable type Integer: '))
print("You input variable type Integer and this is: ", b)
print('===================================================================')
# ======================================================================
# 3. Создать переменную типа Float
print('3. Создать переменную типа Float')
c = 1.345
print('You have variable type : ', type(c), '\n and this is: ', c)
print('===================================================================')
# ======================================================================
# 4. Создать переменную типа Bytes
print('4. Создать переменную типа Bytes')
d = bytes(b)
print('We transform your variable from type Integer \n in type Bytes and this is: ', d)
print('===================================================================')
# ======================================================================
# 5. Создать переменную типа List
print('5. Создать переменную типа List')
itemlist = [a, b, c, d, 'My list variables']
print('Our list consist of: ', itemlist, '\n and we have ' + str(len(itemlist)), 'number of variables')
print('===================================================================')
# ======================================================================
# 6. Создать переменную типа Tuple
print('6. Создать переменную типа Tuple')
nameTuple = ('True', 'Vadim #', '1')
itemTyple = tuple(nameTuple)
print('The variable Tuple is: ', itemTyple)
print('===================================================================')
# ======================================================================
# 7. Создать переменную типа Set
print('7. Создать переменную типа Set')
itemSet = {11, True, 'appel', 41.5}
print('Our itemSet=: ', itemSet, "\n and it type:", type(itemSet))
print('===================================================================')
# ======================================================================
# 8. Создать переменную типа Frozen set
print('8. Создать переменную типа Frozen set')
itemFrozSet = frozenset(itemSet)
print('We made from itemSet type = ', itemSet, '\n frozesnet = ', itemFrozSet)
print('And type our frozenset = ', type(itemFrozSet))
print('===================================================================')
# 9. Создать переменную типа Dict
print('9. Создать переменную типа Dict')
itemDict = {
    'name':'Andrei',
    'surname':'Baranau',
    'age':40,
    'citizen':'Belarus'
     }
print('You can see our Dictionary Items: ', itemDict)
print('===================================================================')
# 10. Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print('10. Вывести в консоль все выше перечисленные переменные с добавлением типа данных')
allitems = [a, b, c, d, itemlist, itemTyple, itemSet, itemFrozSet, itemDict]
print('Hi, This is a list of all our variables:')
for i in allitems:
    print('\n :', i, ' In type: ', type(i))
print('====================================================================')
# 11. Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль
print('11. Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль')
x = input('Input variable in string type  x = ')
y = input('Input variable in string type  y = ')
z = x + ' '+ y
print('Our new variable from 2 variable before: ', z)
print('====================================================================')
# 12. Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('12. Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)')
x = input('Input variable in type string x = ')
y = int(input('Input variable in type integer y = '))
print('Our new variable from 2 variable before: ', x, y)
# 13. Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print('13. Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)')
x = input('Input variable in type string x = ')
y = int(input('Input variable in type integer y = '))
print('Our new variable from 2 variable before: ', x + str(y))


