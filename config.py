import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('2075061407:AAHQB-60I6wqpgP_7psVnRWkWCP1y6pIQIo')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('2093082226'))
w.write('\n')
w.write('}')
