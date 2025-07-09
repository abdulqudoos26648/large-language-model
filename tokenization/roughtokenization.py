# Code practiced along with the tutorial by Andrej Karpathy on tokenization

# Example: ord() and encode() methods
print(ord("h"))
print(list("Kese hai aap, ".encode("utf-8")))
print(list("Kese hai aap, ".encode("utf-32")))

# Encoding the string into tokens
text = 'Any string you paste here!!' 
tokens = text.encode("utf-8")
Tokens = list(map(int, tokens))

print(text)
print("length", len(text))
print(Tokens)
print("length", len(Tokens))

# Function to count frequency of pairs of tokens
def get_data(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

data = get_data(tokens)
print(sorted(((v,k) for k,v in data.items()), reverse=True))

# Function to merge the most frequent pair of tokens
def merge(ids, pair, idx):
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

print(merge([5, 6, 6, 7, 9, 1], (6, 7), 99))

# Perform the merge based on frequency of token pairs
tokens2 = merge(tokens, (6, 7), 111)
print(tokens2)
print("length:", len(tokens2))

# Encoding and merging tokenization
tokens = "Any you put here!!"
tokens = list(map(int, tokens.encode("utf-8")))

# Perform token merging and compression
vocab_size = 276
num_merges = vocab_size - 256
ids = list(tokens)
merges = {}

for i in range(num_merges):
    stats = get_data(ids)
    pair = max(stats, key=stats.get)
    idx = 256 + i
    print(f"merging {pair} into a new token {idx}")
    ids = merge(ids, pair, idx)
    merges[pair] = idx

print("tokens length:", len(tokens))
print("ids length:", len(ids))
print(f"compression ratio: {len(tokens) / len(ids):.2f}X")

# Decoding the tokens back to the string
vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]

def decode(ids):
    tokens = b"".join(vocab[idx] for idx in ids)
    text = tokens.decode("utf-8", errors="replace")
    return text

print(decode([128]))

# Encoding method: Convert string to tokens
def encode(text):
    tokens = list(text.encode("utf-8"))
    while len(tokens) >= 2:
        stats = get_data(tokens)
        pair = min(stats, key=lambda p: merges.get(p, float("inf")))
        if pair not in merges:
            break
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens

print(encode(""))
print(decode(encode("hello world")))

# Checking encoding/decoding with a sample text
valtext2 = "Kese hai ap, btw me aise hi kch likh rha sahi hai"
valtext2 = decode(encode(valtext2))
print(valtext2 == valtext2)

# Forced splits using regex patterns (GPT series)
import regex as re
gpt2pat = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")
print(re.findall(gpt2pat, "btw thank you for coming this far!!"))

# tiktoken library for tokenization
!pip install tiktoken  # added for colab
import tiktoken

# GPT-2 Encoding (does not merge spaces)
enc = tiktoken.get_encoding("gpt2")
print(enc.encode("    hello world!!!"))

# GPT-4 Encoding (merges spaces)
enc = tiktoken.get_encoding("cl100k_base")
print(enc.encode("    hello world!!!"))

# Downloading the necessary vocab and encoder files for GPT-2
!wget https://openaipublic.blob.core.windows.net/gpt-2/models/1558M/vocab.bpe
!wget https://openaipublic.blob.core.windows.net/gpt-2/models/1558M/encoder.json

# Reading the encoder.json file and loading it into a dictionary (similar to 'vocab')
import os, json

with open('encoder.json', 'r') as f:
    encoder = json.load(f)  # equivalent to our "vocab"

# Reading the vocab.bpe file for merge operations (similar to 'merges')
with open('vocab.bpe', 'r', encoding="utf-8") as f:
    bpe_data = f.read()

# Extracting the merge operations from the vocab.bpe file
bpe_merges = [tuple(merge_str.split()) for merge_str in bpe_data.split('\n')[1:-1]]
# This is equivalent to our "merges"

