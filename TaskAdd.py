#Шаблон нашей адресной книги и запись данных в файл
import pickle
import shelve

book = {}
#opena = open('book.data', 'ab')
#openr = open('book.data', 'rb')
#openw.write(str(book))

search = shelve.open('book')



SearchAdd()
