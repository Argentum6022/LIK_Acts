from docxtpl import DocxTemplate
import datetime
import os

#Ввод данных
file_path=str(input('Введите путь папки: '))
date=str(input('Введите дату получения раствора:'))
number=str(input('Введите входящий номер раствора:'))
customer=str(input('Введите название фирмы заказчика:'))
receiving=str(input('Введите способ получения:'))
well=str(input('Введите номер скважины:'))
date_on_well=str(input('Введите дату и время отбора пробы:'))
seal=str(input('Введите номер пломбы:'))
dop_acts=list(map(str,input('Введите названия сопроводительных документов через запятую,'
                       ' если таковые отсутствуют, поставьте \"-\": ').split(',')))

#Создание новой папки
file_path=file_path.replace('\\','\\\\')
os.chdir(file_path)
os.mkdir(number)

#Определние текущей даты
date_now=datetime.date.today()
date_now=date_now.strftime('%d.%m.%Y')

#Заполнение акта приёма
doc = DocxTemplate(f"{file_path}\\Исходные акты\\Исходный акт приёма материалов.docx")
if dop_acts[0]=='-':
    context = { 'date' : date,'number' : number,'customer' : customer,
                'receiving' : receiving,'well' : well,
                'date_on_well' : date_on_well,'seal' : seal,'doc1':'-','doc2':'-'}
elif len(dop_acts)==1:
    context = {'date': date, 'number': number, 'customer': customer,
               'receiving': receiving, 'well': well,
               'date_on_well': date_on_well, 'seal': seal, 'doc1': dop_acts[0], 'doc2': '-'}
else:
    context = {'date': date, 'number': number, 'customer': customer,
               'receiving': receiving, 'well': well,
               'date_on_well': date_on_well, 'seal': seal, 'doc1': dop_acts[0], 'doc2': dop_acts[1]}
doc.render(context)
doc.save(f"{file_path}\\{number}\\{number} Акт приёма материалов.docx")


#Заполнение акта исследования
doc = DocxTemplate(f"{file_path}\\Исходные акты\\Исходный РВО.docx")
if dop_acts[0]=='-':
    context = { 'date' : date,'number' : number,'customer' : customer,
                'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                'seal' : seal,'now_date':date_now,'doc1':'-'}
else:
    context = {'date': date, 'number': number, 'customer': customer,
               'receiving': receiving, 'well': well, 'date_on_well': date_on_well,
               'seal': seal, 'now_date': date_now, 'doc1': 'присутствует'}
doc.render(context)
doc.save(f"{file_path}\\{number}\\{number} РВО.docx")