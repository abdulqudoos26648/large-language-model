# Lec. 1: Lecture 1: Overview and Tokenization
- **Wrong interpretation:** scale is all that matters, algorithms don't matter.  
- **Right interpretation:** algorithms that scale is what matters.
  `accuracy = efficiency × resources`
- Tokenizers convert between strings and sequences of integers (tokens).
  
    Efficiency drives design decisions
    Today, we are compute-constrained, so design decisions will reflect squeezing the most out of given hardware.
    
Data processing: avoid wasting precious compute updating on bad / irrelevant data
    
Tokenization: working with raw bytes is elegant, but compute-inefficient with today's model architectures.
    
Model architecture: many changes motivated by reducing memory or FLOPs (e.g., sharing KV caches, sliding window attention)
    
Training: we can get away with a single epoch!
    
Scaling laws: use less compute on smaller models to do hyperparameter tuning
    
Alignment: if tune model more to desired use cases, require smaller base models
    Tomorrow, we will become data-constrained...
# Tokenization

- Converts text to integer tokens so LLMs can process text.
- Types:
  - **Character-based**: simple, large vocab, long sequences.
  - **Byte-based**: small fixed vocab (0–255), long sequences.
  - **Word-based**: splits into words, huge vocab, UNK tokens needed.
  - **BPE (Byte Pair Encoding)**: merges frequent pairs, balances vocab size and sequence length, used in GPT-2.

**BPE Workflow**:
1. Start with bytes as tokens.
2. Count frequent adjacent pairs.
3. Merge them repeatedly to reduce sequence length.

**Key points**:
- Tokenization is needed for LLMs but has trade-offs between vocab size and sequence length.
- BPE is widely used for its efficiency.
- GPT tokenization uses regex for initial splitting before BPE.

-----------------------------------

# Lec. 2: Pytorch, Resource Accounting

### Lecture Overview:
- Focus: Training models from bottom-up: tensors → models → optimizers → training loop.
- Efficiency: Resource management (memory and compute).

### Key Points:
- Tensors are the fundamental units for storing data, parameters, gradients, and activations.
- Memory Usage: 
  - float32 (4 bytes per element) is standard, but can be inefficient.
  - float16 and bfloat16 reduce memory usage but risk instability.
  - fp8 is more efficient, especially for H100 GPUs.
- Tensor Operations: Matrix multiplication is the most compute-heavy operation.
- Gradient Computation: Backpropagation uses chain rule to compute gradients.
- Optimizers:
  - Basic optimizer: SGD.
  - Variations: AdaGrad, RMSProp, Adam.
- Training Loop:
  1. Data Loading
  2. Forward Pass (Loss Calculation)
  3. Backward Pass (Gradient Computation)
  4. Optimizer Step (Parameter Update)
- Memory and Compute Trade-offs:
  - Mixed precision for faster training and reduced memory usage.
  - Use float32 for parameters and bfloat16/fp8 for activations.
- FLOPs measure the computation cost (e.g., GPT-3 required 3.14e23 FLOPs).
- Note, Save model periodically to avoid losing progress during long training.

# Spring 2025 | Lec. 3: Architectures, Hyperparameters

