import re

# Define regular expressions for the different token types
token_specs = [
    ('KEYWORD',   r'\b(if|then|else|int|char)\b'),
    ('SYMBOL',    r'(\(|\)|!=|==|<=|>=|<|>|=|\+|\*|;)'),
    ('REAL',      r'\b\d+\.\d+\b'),
    ('INTEGER',   r'\b\d+\b'),
    ('IDENTIFIER',r'\b[a-zA-Z][a-zA-Z0-9]*\b'),
    ('WHITESPACE',r'\s+'),    # Skip over spaces and tabs
]

# Compile the regular expressions
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
get_token = re.compile(tok_regex).match

# Define the tokenizer procedure
def tokenize(filename):
    with open(filename, 'r') as f:
        data = f.read()
    
    position = 0
    tokens = []
    while position < len(data):
        match = get_token(data, position)
        if match is not None:
            type_ = match.lastgroup
            value = match.group(type_)
            if type_ != 'WHITESPACE':  # Ignore whitespace
                tokens.append((type_, value))
            position = match.end()
        else:
            raise RuntimeError(f'Unexpected character: {data[position]}')
    
    return tokens

# Example usage
if __name__ == "__main__":
    tokens = tokenize('text.txt')
    for token in tokens:
        print(token)