## Building the GPT Tokenizer

Andrej Karpathy: [YouTube Lecture](https://www.youtube.com/watch?v=zduSFxRajkE&t=1376s&ab_channel=AndrejKarpathy) It's really a good one.
# Tokenization in LLMs

Tokenization is the process of translating strings or text into a sequence of tokens and vice versa. 
Tokenization is at the heart of much weirdness of LLMs.

- Why can't LLM spell words? **Tokenization**.
- Why can't LLM do super simple string processing tasks like reversing a string? **Tokenization**.
- Why is LLM worse at non-English languages (e.g. Japanese)? **Tokenization**.
- Why is LLM bad at simple arithmetic? **Tokenization**.
- **etc**

---


### Efficiency and Tradeoff:

- **Larger vocabulary and better tokenization (like in GPT-4)** reduce token count and improve processing efficiency while using the same computational resources.

- **Tradeoff**: Increasing vocabulary size improves processing, but too large a vocabulary can make embedding tables and predictions less efficient. There’s a **sweet spot** for the optimal token count: **dense yet efficient**.

Tokenize strings into integers using a fixed vocabulary, and then use these integers to look up vectors and feed them into the Transformer.

### Why Not UTF-8 Alone?

**UTF-8 encoding** is preferred, but using it **naively** limits the vocabulary to just **256 tokens**, which results in:

1. **Long and inefficient text sequences**.
2. **Tiny embedding table**.
3. **Poor prediction accuracy** due to the challenge of processing long sequences with transformers.

This makes the model less efficient in understanding and predicting text.

---
# Tokenization and Encoding in LLMs

### Goal:
We need to take strings and feed them into language models. To do this:

- Tokenize the strings into integers using a fixed vocabulary.
- Use these integers to look up vectors in a table, and the vectors are then fed into the Transformer as input.

### Python Strings: 
Strings are immutable sequences of Unicode code points.

### Unicode Code Points:
These are unique identifiers for characters in the Unicode system.

##Problem with Unicode:
The Unicode system keeps changing, making it unstable for consistent use. It has around 150,000 code points which is very very large, and the system is still evolving.
To address this, encoding is used for a more stable and efficient representation. This is where systems like UTF-8 come into play, providing a better way to represent and process characters.
#### **UTF-8:**
- **Widely used** and efficient.
- Uses **1 to 4 bytes** per character, depending on the value.

| UTF-8 (binary) | Code Point (binary) | Range |
|-----------------|---------------------|-------|
| 0xxxxxxx        | xxxxxxx             | U+0000–U+007F |
| 110xxxxx 10yyyyyy | xxxxxxyyyyyy         | U+0080–U+07FF |
| 1110xxxx 10yyyyyy 10zzzzzz | xxxxyyyyyyzzzzzz | U+0800–U+FFFF |
| 11110xxx 10yyyyyy 10zzzzzz 10wwwwww | xxxyyyyyyzzzzzzwwwwww | U+10000–U+10FFFF |

#### **UTF-16:**
- Uses **2 or 4 bytes per character**.
- Efficient for characters outside the Basic Multilingual Plane.

#### **UTF-32:**
- Uses **4 bytes for every character**.
- The simplest but **leas**


```python
list("How are you?, 👋توهان ڪيئن آهيو؟ ".encode("utf-8"))
list("How are you?, 👋توهان ڪيئن آهيو؟ ".encode("utf-16"))
list("How are you?, 👋توهان ڪيئن آهيو؟ ".encode("utf-32"))
```
### Visualizing Tokenization

check out this app: [**TikTokenizer**](https://tiktokenizer.vercel.app/)

### Byte Pair Encoding (BPE) Algorithm:
BPE helps solve the above issue by compressing byte sequences. It works by merging frequent byte pairs in the text, allowing for a larger vocabulary and more efficient processing while still using UTF-8.

