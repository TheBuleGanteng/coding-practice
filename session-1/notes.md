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
- `lst.pop(i)` removes AND returns the item; the list shrinks in place. Never write `lst = lst.pop(0)`.
- `append`, `sort`, `remove` modify in place and return `None`. Don't assign their result.
- `lst.append(x)` adds `x` as ONE item to the list; appending a list to a list creates nested lists: `[[...]]`.
- Don't name variables `len`, `max`, `min`, `list`, `dict`, `sum` (shadows built-ins, breaks the whole function).
- `while cond:` rechecks `cond` before every pass. Something inside must change it.


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
| `while cond:` | passes × cost per pass | If the loop only moves a pointer forward (never resets), total passes ≤ n across the whole run → O(n) total, even inside another loop |

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
| Seen-so-far dict | "find a pair that sums to…", "one pass" | Look up the complement (target − current value) **before** storing the current item | O(n) time, O(n) space | Problem 7 |
| Stack | "brackets", "nesting", "most recent must close first" | `append` to push, check `[-1]`, `pop()`; empty-check first | O(n) time, O(n) space | Problem 8 |
| Sliding window (fixed size) | "k consecutive", "every stretch of length k" | First window once; then add the entering item `[i+k-1]`, subtract the leaving item `[i-1]` | O(n) | Problem 10 |
| Prefix sums | "many range queries", "total between X and Y" | Running totals once; range = `total[end] - total[start-1]` | O(n + q) | Problem 10b |
| Variable-size sliding window (two pointers) | "longest/shortest consecutive stretch where total ≤ / ≥ X" | Move the end `i` closer to the end one step at a time; As long as the window breaks the rule, use `while` to move `start` (the beginning of the window) closer to the end (closer to i), shrinking the window; record once the `while` stops running (when total is no longer violated) | O(n) | Problem 11b |


## Process
- New pattern and no idea after 10–15 min → ask for the concept only, then implement.
- Hard stop at 1.5× the time limit → study the solution, retype it cold next day.
- Simulate on paper as the computer: one line per step with i, pointers, total, action.
- Before switching approach, write one line saying why the current one fails.
- For every loop: how can it end, and what must happen in each case?
- Check every comparison against the spec's wording (≤ vs <).


## Worked examples (things I'm still getting comfortable with)

### Simulating on paper (one line per step)
Track each pointer (a variable holding a position), the window, its total, and the action.
```
budget = 5, counts = [2, 1, 3, 1, 1, 4]
i=2  add 3 → window pos 0–2 = [2, 1, 3]  total 6  TOO BIG
           → drop the 2, move start forward by 1 position, so start = [1] → [1, 3] → total 4  ok → length 2
i=5  add 4 → window pos 2–5 = [3, 1, 1, 4]  total 9  TOO BIG
           → drop the 3, move start forward by 1 position, so start = [3] → [1, 1, 4] → total 6  still too big
           → drop the 1, move start forward by 1 position, so start = [4] → [1, 4] → total 5  ok → length 2
```
"Still too big → drop again" = a `while` loop.

### Basic while loop
```python
x = 10
while x > 3:      # checked before every pass
    print(x)
    x = x - 2     # must change something the condition depends on
# prints 10, 8, 6, 4
```

### While loop that shrinks a window (Problem 11b)
```python
while stretch_total > budget:     # repeat until the window fits
    start += 1                    # drop the first item of the window
    stretch_total = counts_dict[i] - counts_dict[start - 1]   # recompute
# after the loop: the window from start to i fits → record i - start + 1
```

### Slicing: [a:b] gives b − a items, stops BEFORE b
```python
nums = [3, 1, 4, 1]
nums[0:1]   # [3]      (index 0 only)
nums[1:3]   # [1, 4]   (indices 1 and 2)
nums[0:0]   # []       (nothing)
nums[a:b+1] # to INCLUDE index b
```

### In-place method vs returning function
```python
lst.sort()          # changes lst, returns None
new = sorted(lst)   # leaves lst alone, returns a new sorted list
x = lst.pop(0)      # removes first item from lst AND gives it to you as x
```