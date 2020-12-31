import io
import keyword
import token
import tokenize

samp = """\
for x in range(8):
  if x%2:
    y = x
    while y>0:
      print y,
      y -= 3
    print('the if while def')
"""

translate = {"for": "per", "if": "se", "while": "mentre", "print": "stampa"}


def toks(tokens):
    for tt, ts, src, erc, ll in tokens:
        if tt == token.NAME and keyword.iskeyword(ts):
            ts = translate.get(ts, ts)
        yield tt, ts


def main():
    rl = io.StringIO(samp).readline
    tokens = tokenize.generate_tokens(rl)
    for Token in tokens:
        print(Token)
    # toki = toks(tokenize.generate_tokens(rl))
    # print(tokenize.untokenize(toki))


main()
