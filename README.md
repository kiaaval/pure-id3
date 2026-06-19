# pure-id3

A tiny **ID3 decision tree** built from scratch in pure Python — no `scikit-learn`, no
`pandas`, no `numpy`. It learns the classic "Play Tennis?" dataset and then predicts
whether you'd play given a new day's weather.

The point of the project is to make the algorithm legible: every step (entropy,
information gain, recursive splitting) is plain Python you can read top to bottom.

## What it does

1. Reads `data.csv` (14 labelled days).
2. Builds a decision tree using the **ID3** algorithm — at each node it picks the
   feature with the highest *information gain* and recurses on the rows that fall down
   each branch.
3. Prints the learned tree.
4. Asks you for a new day's conditions and walks the tree to a prediction.

## Run it

```bash
python3 main.py
```

Example session:

```
[1] Training on data.csv (14 rows)...
[2] Learned tree:
        Weather?
        ├── Sunny → Humidity? (High→No, Normal→Yes)
        ├── Overcast → Yes
        └── Rainy → Windy? (False→Yes, True→No)
[3] Predict new day:
Weather ['Sunny', 'Overcast', 'Rainy']: Sunny
Temperature ['Hot', 'Mild', 'Cool']: Cool
Humidity ['High', 'Normal']: High
Windy ['True', 'False']: True
        Weather=Sunny → Humidity=High → No
        Prediction: NO
```

No third-party dependencies — only the Python standard library (`csv`, `math`).

## How ID3 works here

- **Entropy** measures how mixed a set of Yes/No labels is (0 = pure, 1 = an even split).
- **Information gain** = the parent's entropy minus the weighted average entropy of the
  children after splitting on a feature. The feature with the largest gain wins.
- The tree recurses on each branch using **only the rows that match that branch's
  value**, so entropy and gain are always measured on the same subset. A branch stops
  (becomes a leaf) when its rows are pure, or when there are no features left (then it
  falls back to a majority vote).

## File layout

| File         | Responsibility                                                        |
|--------------|-----------------------------------------------------------------------|
| `schema.py`  | `TypedDict` shapes for features, branches, and gain records           |
| `dataset.py` | `load_data()` — reads `data.csv` into feature columns + labels        |
| `entropy.py` | `get_entropy()` and `information_gain()`                               |
| `tree.py`    | `piles()`, `build_tree()`, `model()`, `predict()` — the ID3 core      |
| `display.py` | `print_tree()` rendering and the `ask()` input prompt                 |
| `main.py`    | Entry point that wires training → display → prediction together       |
| `data.csv`   | The Play Tennis dataset (14 rows)                                      |

## Dataset

`data.csv` is the textbook Play Tennis set: columns `Weather`, `Temperature`,
`Humidity`, `Windy`, and the target `Play` (Yes/No).
