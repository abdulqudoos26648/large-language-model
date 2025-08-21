#### **[Lecture 1 - Intro and Word Vectors](https://youtu.be/DzpHeXVSC5I?si=h1cKOLC38Qr9DWOX)**

---

#### **Starting**

- The human ability to use language is what truly sets us apart as a species.
- language is discovered arounf for th emillion so fthe years ago but the invention of writing, about 5,000 years ago, was a massive leap forward.
---

#### **From Old Methods to Modern AI**

- In the past, computers were bad at understanding language. Traditional methods relied on things like dictionaries and thesauruses, which failed to capture the nuances of meaning.
- A huge breakthrough happened around 2014 when deep learning revolutionized machine translation. This gave the way for modern AI.
- Today, we're in the era of **LLMs** like ChatGPT. These models can generate fluent, coherent text by simply predicting the most probable next word in a sequence. This is a fundamental concept for how they work.

---

#### **Representing Words Numerically**

- To use words in a computer, we need to turn them into numbers. The old way was with **one-hot vectors**.
- **One-Hot Vectors:** A long list where each word has its own unique position with a `1`, and all other positions are `0`.
- **The very huge problem with one-hot vectors:** They don't capture any relationships between words. Words like "motel" and "hotel" are treated as completely separate and unrelated.

- The new and better way is to use **word vectors** (also called **embeddings**).
- **Word Vectors:** These are short, dense vectors of numbers. The core idea is that a word's meaning is defined by the company it keeps.
- The vectors for words with similar meanings (like "hotel" and "motel") are **close to each other** in this multi-dimensional space.
- **Note:** While distance (e.g., Euclidean or cosine similarity) is an important measure of closeness in the embedding space, the **directions in the space** also have semantic meaning.  
  - Example: **King - Man + Woman = Queen**  
  - This shows that specific vector directions can encode relationships such as gender.

#### **Visualizing High-Dimensional Embeddings**

- Since embeddings exist in very high-dimensional space, it's hard to visualize them directly.  
- To address this, techniques like **t-distributed Stochastic Neighbor Embedding (t-SNE)** are used.  
- **t-SNE** projects high-dimensional vectors into **2D or 3D**, making it easier to see clusters and relationships between words.  
- The professor briefly mentioned t-SNE as a powerful tool to **visualize word embeddings**, where words with similar meanings appear close together in the reduced space.


---

#### **The word2vec Algorithm**

- **word2vec** is a popular and efficient algorithm for creating these word vectors.
- **How it works:** It trains a model by looking at a huge amount of text. For a given "center word," it tries to predict the "context words" that appear nearby.
- The model uses the **softmax function** to calculate the probability of a word appearing in a context. This probability is based on the **dot product** of the words' vectors. A higher dot product means the words are more similar.
- The learning process uses **gradient descent** to constantly update and refine the vectors. It starts with random vectors and adjusts them until they are good at predicting word relationships, thus capturing their meaning.
- This process is what allows us to automatically learn powerful word representations from raw text.

---

- #### **Explanation of the `Word2Vec Overview` Diagram**

![Word2Vec Overview]([Stanford CS224N: NLP with Deep Learning/Assets/Word2Vec Overview.png](https://github.com/abdulqudoos26648/large-language-model/blob/2cd1bb9df9ced2b2a44383ad7aa5c340d95163aa/Stanford%20CS224N%3A%20NLP%20with%20Deep%20Learning/Assets/Word2Vec%20Overview.png))

- The image shows a core concept of the `word2vec` algorithm.
- It illustrates a sentence fragment: `... problems turning into banking crises as ...`
- The red highlighted word, "**into**," is the **center word** (`w_t`).
- The words in purple are the **context words** within a window of size 2. These are the "outside context words." They are `problems` and `turning` to the left, and `banking` and `crises` to the right.
- The arrows show how the model works: it's calculating the probability of each outside word appearing, given the center word.
- For example, the model wants to find the probability of `problems` appearing given `into`, or `P(w_{t-2} | w_t)`. It does this for all the surrounding words in the window.
- The whole point of the `word2vec` training is to adjust the word vectors so these probabilities are as high as possible for the words that actually appear together in the text. This is what teaches the model the relationships between words.

