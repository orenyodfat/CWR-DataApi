import codecs
import os
import sys
import getopt
import io

from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder

#Read a cwr file stream via stdin and return back cwr-json via stdout
#Usage example  : python3 cwr2json.py < tests/examples/ackexample.V21 > ackexample.V21.json
if __name__ == '__main__':

    decoder = default_file_decoder()

    data = {}
    data['filename'] = ''
    data['contents'] = sys.stdin.read()

    data['contents'] = data['contents'].replace('\n','')
    #replace '\r with 300 SPACES
    #this is needed inorder to be on the safe side to parse optional cwr params
    spaces =''
    for i in range(1,300):
      spaces +=" "
    spaces +='\n'
    data['contents'] = data['contents'].replace('\r',spaces)

    data = decoder.decode(data)
    encoder = JSONEncoder()
    result = encoder.encode(data)
    sys.stdout.write(result)
