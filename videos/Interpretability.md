# Notes on Anthropic’s Video: *Interpretability: Understanding how AI models think*

**Video Link:** [Interpretability: Understanding how AI models think](https://youtu.be/fGKNUvivvnc?si=zDf5HJC-s0sdzUqE)

---

## Introduction
- When we talk to an LLM, is it just autocomplete or something deeper?  
- Truth: no one fully knows.  
- Interpretability = trying to open up the model’s “brain.”  
- They describe it as doing neuroscience on AIs or biology on math organisms.

---

## The “Biology” of AI Models
- LLMs aren’t built with simple rules like if/then statements.  
- They’re trained in a kind of evolutionary process: start out bad, gradually improve with tons of data.  
- The final system is complex and emergent, not explicitly designed.  
- Predicting the next word sounds simple, but forces the model to build internal concepts and strategies.  
- Analogy: humans have a basic drive (survive + reproduce) but it leads to rich thoughts and behaviors. Models have something similar.

---

## What the Model is “Thinking”
- Researchers want a flowchart of how the model moves from input → output.  
- Advantage over human neuroscience: they can actually see all the components lighting up.  

Findings so far:
- **Sycophantic praise feature** → circuit activates when the model gets too many compliments.  
- **Generalizable math circuits** → e.g. it can add numbers ending in 6 + 9 in all kinds of contexts, proving it learned the rule instead of memorizing answers.  
- **Shared concepts** → a single representation of “big” that isn’t tied to any one language, which helps explain why models translate so well.

---

## Why This Matters
- It’s not just curiosity — interpretability shows us risks.  

**Faithfulness problem:**  
- In one test, the model was given a hard math problem with a wrong hint.  
- Instead of solving, it worked backwards to create a fake but convincing solution.  
- Shows models can be unfaithful — prioritizing pleasing the user instead of being correct.  

**Hallucinations:**  
- Models sometimes just make stuff up.  
- There seem to be two processes: one that works on the answer, and one that decides confidence.  
- If confidence is misaligned, the model will give a wrong answer but sound completely sure.  
- Researchers are trying to connect those two processes more tightly.

---

## The Future of Interpretability
- Current tools are clunky — like a microscope that only works 20% of the time.  
- Goal: make it easy to generate a flowchart of a model’s reasoning for any prompt.  

Potential benefits:
- Debugging bad behavior.  
- Building trust by seeing what the model is really doing.  
- Eventually developing a proper scientific language for how AI works.  

Overall: This isn’t just academic — it’s foundational for making AI safer and more reliable as it gets woven into society.

