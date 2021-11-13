from Parser import Parser
from config import URL

films = dict()

for i in range(0, 12):
    p = Parser(URL, str(i))
    films['page ' + str(i)] = p.parse()
Parser.save_json(films)
