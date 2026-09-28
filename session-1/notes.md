## Syntax gotchas
- `break` exits a loop; `continue` skips to the next pass
- Two ways to find the max in a dict:
  - **Way 1: max over the keys, compared by their values** (returns the key only)
```python
    best_start = max(running_total, key=running_total.get)
    return best_start, running_total[best_start]
```
  - **Way 2: max over (key, value) pairs** (returns the whole pair)
```python
    best_window = max(running_total.items(), key=lambda kv: (kv[1], -kv[0]))
    return best_window
```

## Costs

### Operation costs
| Operation | Cost | Notes |
|---|---|---|
| `lst[i]`, `lst[i] = x` | O(1) | Direct index |
| `len(x)` | O(1) | Stored, not counted |
| `lst.append(x)` | O(1) | Add to end |
| `lst.pop()` | O(1) | Remove from end |
| `lst.pop(0)`, `lst.insert(0, x)` | O(n) | Everything shifts over |
| `x in lst`, `lst.index(x)`, `lst.remove(x)`, `lst.count(x)` | O(n) | Scans the list (hidden loop) |
| `lst[a:b]` | O(b − a) | Copies the items |
| `sum()`, `max()`, `min()` over n items | O(n) | One pass |
| `sorted()`, `.sort()` | O(n log n) | Never O(n) |
| `d[k]`, `d[k] = v`, `k in d`, `d.get(k)`, `del d[k]` | O(1) average | Hashing: goes straight to the "hook" |
| `s.add(x)`, `x in s` | O(1) average | Same as dict |
| `str.split()`, `str.lower()` | O(length of string) | Touches every character |
| `for x in ...` over n items | O(n) | Times whatever the body costs |

### Combining rules
- Steps one after another → **add** the costs.
- Work inside a loop → **multiply** (passes × cost per pass).
- Keep the dominant term, drop constants: O(3n) → O(n); O(n² + n) → O(n²).
- In a **sum**, a smaller variable gets absorbed: O(n + k) → O(n) if k ≤ n.
- In a **product**, keep both: O(nk). Worst-case ceiling: O(n²) if k ≤ n.
- State space too: extra dicts, lists or stacks that grow with input → O(n) space.

## Patterns and triggers

| Pattern | Trigger phrases | Core move | Typical cost | Seen in |
|---|---|---|---|---|
| Count / group with a dict | "how many per…", "total by…", "frequency" | `d[k] = d.get(k, 0) + 1` | O(n) | Problem 1, Drills B–C |
| Set for distinct | "distinct", "unique", "dedupe" | `s.add(x)`; `len(s)` | O(n) | Drill A |
| Rank / top-k | "top k", "most common", "with ties…" | Count, then `sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))` | O(n + m log m) | Problem 1, Drill B |
| Sort, then scan | "overlapping", "merge", "intervals" | Sort by start; compare each item to `result[-1]` | O(n log n) | Problem 5 |
| Seen-so-far dict | "find a pair that sums to…", "one pass" | Look up the complement (total - current value) **before** storing the current item | O(n) time, O(n) space | Problem 7 |
| Stack | "brackets", "nesting", "most recent must close first" | `append` to push, check `[-1]`, `pop()`; empty-check first | O(n) time, O(n) space | Problem 8 |
| Sliding window (fixed size) | "k consecutive", "every stretch of length k" | First window once; then add the entering item `[i+k-1]`, subtract the leaving item `[i-1]` | O(n) | Problem 10 |
| Prefix sums | "many range queries", "total between X and Y" | Running totals once; range = `total[end] - total[start-1]` | O(n + q) | Problem 10b |