from docxtpl import DocxTemplate
import datetime
import os
from Weighting_agent_Act import wa
from RVO_Act import rvo
from KMC_Act import kmc

key=str(input('Введите название образца (\"КМЦ\",\"РВО\",\"Утяжелитель\"):'))

if key=='РВО':
    rvo()

elif key=='Утяжелитель':
    wa()

elif key=='КМЦ':
    kmc()

else:
    print('Такого протокола не существует!')