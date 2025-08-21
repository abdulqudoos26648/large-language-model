## **[Lecture 1 - Intro and Word Vectors](https://youtu.be/DzpHeXVSC5I?si=h1cKOLC38Qr9DWOX)**

---

#### **Starting**

- Language itself emerged hundreds of thousands of years ago, but the invention of **writing** (about 5,000 years ago) was a massive leap forward.  
  - Writing enabled knowledge to be preserved and transmitted across generations, accelerating human progress.

---

#### **From Old Methods to Modern AI**

- Traditionally, computers were bad at understanding language.  
  - Early approaches relied on **dictionaries, thesauruses, and rules**, which failed to capture nuance and meaning.  
- A breakthrough came around **2014**, when **deep learning revolutionized machine translation**.  
- Today, we are in the era of **LLMs** such as ChatGPT.  
  - These models generate fluent and coherent text by predicting the **most probable next word** in a sequence — a core principle behind modern NLP.

---

#### **Representing Words Numerically**

- Computers need **numbers** to work with words.  
- **One-Hot Vectors:**  
  - Each word is represented by a long sparse vector with a single `1` and many `0`s.  
  - **Problem:** No relationships are captured. Words like *hotel* and *motel* are treated as completely unrelated.  

- **Word Vectors / Embeddings:**  
  - Short, dense vectors that capture meaning.  
  - A word’s meaning is defined by the **company it keeps**.  
  - Words with similar meanings (e.g., *hotel* and *motel*) have vectors that are **close together** in the embedding space.  

- **Note:** In embedding spaces, **distance** (e.g., Euclidean or cosine similarity) is important, but **directions** in the space also encode semantic relationships.  
  - Example: **King - Man + Woman = Queen**  
  - This demonstrates that vector directions can capture relationships such as **gender**.

---

#### **Visualizing High-Dimensional Embeddings**

- Embeddings live in **high-dimensional space**, which humans cannot directly visualize.  
- To interpret them, dimensionality reduction techniques like **t-distributed Stochastic Neighbor Embedding (t-SNE)** are used.  
  - **t-SNE** projects vectors into **2D or 3D** while preserving local similarities.  
  - Words with similar meanings appear **close together** in the reduced space.  
- The professor briefly highlighted **t-SNE** as a powerful tool for visualizing word embeddings.

---

#### **The Word2Vec Algorithm**

- **word2vec** is a widely used and efficient algorithm for learning embeddings.  
- **Core Idea:** Given a *center word*, predict the *context words* that appear nearby in a sentence.  
- **How it works:**  
  - For a given center word, the model assigns probabilities to all possible context words.  
  - The **softmax function** converts the dot product between vectors into a probability score.  
  - A higher dot product means higher similarity.  
- The vectors start randomly but are refined using **gradient descent**, improving their ability to capture semantic relationships.  

---

#### **[Word2Vec Overview](https://github.com/abdulqudoos26648/large-language-model/blob/c1515f7aeabc4001dbe8faeb4869d47341b87df1/Stanford%20CS224N%3A%20NLP%20with%20Deep%20Learning/Assets/lect%231/Word2Vec%20Overview.png)**

- The diagram illustrates the key training setup:  
  - Sentence fragment: `... problems turning into banking crises as ...`  
  - Center word: "**into**" (`w_t`)  
  - Context words (window size = 2): `problems`, `turning`, `banking`, `crises`  
- The model computes probabilities like `P(problems | into)`.  
- Training adjusts vectors so that real context words have **high probability**, teaching the model the relationships between words.

---

#### **[Word2Vec: The Objective Function](https://github.com/abdulqudoos26648/large-language-model/blob/c1515f7aeabc4001dbe8faeb4869d47341b87df1/Stanford%20CS224N%3A%20NLP%20with%20Deep%20Learning/Assets/lect%231/Word2Vec%20%20objective%20function.png)**

- The goal of Word2Vec is to **maximize the likelihood** of seeing real context words given a center word.  
- To simplify:  
  - Instead of maximizing likelihood, we **minimize the negative log likelihood (NLL)**.  
  - The `log` function converts products into sums, making optimization easier.  
  - Adding a negative sign flips maximization into minimization.  
- The final objective is the **average negative log likelihood**.  
  - Minimizing this is equivalent to maximizing prediction accuracy.

---

#### **[Word2Vec: The Prediction Function (Softmax)](https://github.com/abdulqudoos26648/large-language-model/blob/c1515f7aeabc4001dbe8faeb4869d47341b87df1/Stanford%20CS224N%3A%20NLP%20with%20Deep%20Learning/Assets/lect%231/Word2Vec%20predictive%20function.png)**

- Probabilities are calculated using the **softmax function**:  

  1. **Dot Product:** `u_o · v_c` — similarity between outside word (`u_o`) and center word (`v_c`).  
  2. **Exponentiation:** Ensures positivity.  
  3. **Normalization:** Divides by the sum over all words in the vocabulary, ensuring values form a valid probability distribution.  

- The softmax turns similarity scores into a probability distribution over possible context words.  
- This is a central technique used across deep learning, not just in NLP.

---

#### **[Training the Model: Optimization](https://github.com/abdulqudoos26648/large-language-model/blob/c1515f7aeabc4001dbe8faeb4869d47341b87df1/Stanford%20CS224N%3A%20NLP%20with%20Deep%20Learning/Assets/lect%231/Word2Vec%20optimize%20parameters.png)**

- Word vectors = **parameters** (`θ`) of the model.  
  - With vocabularies of millions of words, this is a massive parameter space.  
- We use **gradient descent** to optimize:  
  - Imagine a ball rolling downhill on the loss surface.  
  - The **gradient** points in the steepest slope direction.  
  - By taking small steps opposite to the gradient, we gradually minimize the loss.  
- Repeated updates refine the embeddings, leading to high-quality word vectors that capture meaning automatically from raw text.
