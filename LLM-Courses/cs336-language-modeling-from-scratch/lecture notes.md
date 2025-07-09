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

## Transformers (overall)

* Use self-attention, positional encodings, LayerNorm, MLP, residual connections.
* Attention: Q, K, V → softmax → weighted sum.
* Causal masking to prevent looking ahead.
* Scaling laws: compute, data, parameters scale predictably.

## Memory & FLOPs (What Matters)

* Memory = parameters + activations + gradients + optimizer states.
* FLOPs:

  * Forward: `2 * tokens * parameters`
  * Backward: `4 * tokens * parameters`
  * Total: `~6 * tokens * parameters`
* Matrix multiplications dominate compute.

## PyTorch Essentials

* Use `.to(device)` for tensors/models.
* `pin_memory`, `non_blocking=True` for fast data transfer.
* Mixed precision with `torch.cuda.amp`: use bfloat16/float16 forward, float32 params/grad.
* Random seeds:

  ```python
  torch.manual_seed(0)
  np.random.seed(0)
  random.seed(0)
  ```

## `einops` + `jaxtyping`

* `einops`:

  * `rearrange`: clean reshaping with named dims.
  * `reduce`: clear reductions.
  * `einsum`: explicit matmul with clear indexing.
* Example:

  ```python
  z = einsum(x, y, "batch seq1 hidden, batch seq2 hidden -> batch seq1 seq2")
  ```
* `jaxtyping` for documentation:

  ```python
  x: Float[torch.Tensor, "batch seq hidden"] = torch.ones(2, 3, 4)
  ```

## Core PyTorch Patterns

### Linear Layer

```python
class Linear(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_dim, out_dim) / np.sqrt(in_dim))
    def forward(self, x):
        return x @ self.weight
```

### Stacked Linear Model

```python
class Cruncher(nn.Module):
    def __init__(self, dim, num_layers):
        super().__init__()
        self.layers = nn.ModuleList([Linear(dim, dim) for _ in range(num_layers)])
        self.final = Linear(dim, 1)
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return self.final(x).squeeze(-1)
```

## Optimizers (Simple Versions)

### SGD

```python
class SGD(torch.optim.Optimizer):
    def __init__(self, params, lr=0.01):
        super().__init__(params, dict(lr=lr))
    def step(self):
        for group in self.param_groups:
            for p in group["params"]:
                p.data -= group["lr"] * p.grad.data
```

### AdaGrad

```python
class AdaGrad(torch.optim.Optimizer):
    def __init__(self, params, lr=0.01):
        super().__init__(params, dict(lr=lr))
    def step(self):
        for group in self.param_groups:
            for p in group["params"]:
                grad = p.grad.data
                state = self.state.setdefault(p, {})
                g2 = state.get("g2", torch.zeros_like(grad))
                g2 += grad ** 2
                state["g2"] = g2
                p.data -= group["lr"] * grad / (g2.sqrt() + 1e-5)
```

## Efficiency Insights

* Matrix multiplications = main compute cost.
* Mixed precision improves speed and reduces memory.
* Track FLOPs:

  ```python
  actual_num_flops = 2 * B * D * K
  actual_flop_per_sec = actual_num_flops / actual_time
  mfu = actual_flop_per_sec / promised_flop_per_sec
  ```
