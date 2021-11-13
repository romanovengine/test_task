import Parser
from config import URL


for i in range(0, 12):
    p = Parser.Parser(URL, str(i))
    p.parse()
