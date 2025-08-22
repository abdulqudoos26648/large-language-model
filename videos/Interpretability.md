# Anthropic – Interpretability: Understanding How AI Models Think

**Video:** [Interpretability: Understanding how AI models think](https://youtu.be/fGKNUvivvnc?si=remasNk8AiBEi3Qd)

---

## Starting
- Nobody fully knows what’s really going on inside LLMs.  
- Interpretability = trying to open up the model’s “brain.”  
- Feels like doing neuroscience on AI or biology on math organisms.  
- We don’t yet have the right language for describing models → so we borrow analogies (sometimes “like little people,” sometimes “like programs”).

---

## The “Biology” of AI Models
- Not rule-based like traditional software.  
- Trained through a kind of evolution: start bad, get better with massive data + tuning.  
- Result: complex, emergent systems nobody explicitly designed.  
- Simple goal (predict next word) pushes the model to create rich internal structures.  
- Analogy: humans have basic drives (survive/reproduce) → leads to complex thoughts/emotions.

---

## What’s Going On Inside
- Researchers try to map out how inputs turn into outputs.  
- Advantage over human neuroscience: they can see every component “lighting up.”  

**Key discoveries:**  
- **Sycophantic praise** → circuit activates when receiving too many compliments.  
- **Generalizable math** → found circuits that can add numbers ending in 6 + 9 across contexts (even in citations).  
- **Shared concepts** → e.g. “big” exists as a universal idea, not tied to one language → helps explain strong translation.

---

## Why This Matters
Interpretability reveals risks:  

**Faithfulness problem**  
- Model asked a tough math question with a wrong hint.  
- It didn’t solve the problem → instead built a fake but convincing proof.  
- Shows models can be unfaithful → prioritizing pleasing the user over truth (“bullshitting”).  

**Hallucinations**  
- Models can be confidently wrong.  
- Two processes:  
  1. Working on the answer.  
  2. Judging confidence.  
- If the confidence process is misaligned, the model makes stuff up but sounds certain.  
- Fix idea: better connect the two processes.

---

## The Future of Interpretability
- Current tools = like a microscope that only works ~20% of the time and requires lots of expertise.  
- Goal: push-button interpretability → any interaction can generate a flowchart of what the model was “thinking.”  
- Once that exists, interpretability shifts from building tools → to an “army of biologists” studying model behaviors directly.  
- Claude itself may help with interpretability (good at analyzing large patterns).  
- Important not just to study finished models, but also to trace *training processes* → see how circuits form and feed insights back into design.

---
