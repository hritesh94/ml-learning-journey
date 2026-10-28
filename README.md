# ML Learning Journey

My notes and practice code from learning Python, data analysis, and the basics of machine learning: from `print("hello world")` to cleaning real datasets and preparing them for models.

I followed Krish Naik's courses ([Complete Python Bootcamp](https://github.com/krishnaik06/Complete-Python-Bootcamp) and [Complete Data Science With Machine Learning And NLP 2024](https://github.com/krishnaik06/Complete-Data-Science-With-Machine-Learning-And-NLP-2024)). The course material stays in those repos. This repo has **my own work**: assignments I solved, notebooks I rewrote while following along, and small scripts I wrote to try ideas out.

## What I learned

**Python fundamentals**
- Syntax, variables, data types, operators, input/output
- Control flow: `if/elif/else`, `for`/`while` loops, `break`/`continue`/`pass`
- Data structures: lists, tuples, sets, dictionaries, comprehensions, `zip`, `collections`
- Functions: default/keyword arguments, `*args`/`**kwargs`, lambdas, callbacks, closures, currying, `functools.partial`, memoization
- Iterators, generators, and decorators
- OOP: classes, constructors, class/static methods, properties, inheritance (single and multiple), polymorphism, abstract base classes, operator overloading, custom exceptions, context managers
- Modules and packages (including building my own package)
- File handling (text, binary, CSV, JSON) and exception handling
- Logging: handlers, formatters, rotating log files
- Concurrency: `threading`, `multiprocessing`, `ThreadPoolExecutor`, `ProcessPoolExecutor`
- Web basics with Flask: routes, templates, GET/POST forms, a small JSON REST API

**Data analysis**
- NumPy arrays, indexing, broadcasting, statistics
- Pandas: reading CSV/Excel/URLs, selecting, cleaning, grouping, merging
- Visualization with Matplotlib and Seaborn
- SQL with SQLite3 from Python

**ML basics: feature engineering and EDA**
- Kinds of missing data (MCAR / MAR / MNAR) and imputation strategies
- Imbalanced datasets: up/down-sampling and SMOTE
- Outlier detection with the five-number summary, IQR, and box plots
- Encoding categorical data: one-hot, label, ordinal, and target-guided ordinal encoding
- End-to-end EDA on real datasets (wine quality, flight prices, Google Play Store)

## Repo layout

| Folder | Contents |
|---|---|
| [`python/`](python) | Python Bootcamp assignments, data analysis, Flask, logging, concurrency |
| [`New folder/`](New%20folder) | ML feature engineering notebooks |
| [`New folder/eda/`](New%20folder/eda) | Exploratory data analysis projects |

### File naming in `python/`
For most topics there are three notebooks:
- `*questions.ipynb` / `*_assignment.ipynb`: the assignment prompts from the course
- **`*_with_code_cells.ipynb`: my solutions** ← the main work
- `*solution(s).ipynb`: the tutor's reference solution, which I used to check my answers

In `New folder/`, the numbered notebooks (`1.0-…`, `2.0-…`, etc.) are the tutor's lecture notebooks. The notebooks with plain names (`Outliers.ipynb`, `smote_practice.ipynb`, …) are my own versions, rewritten while following along.

---

## `python/`: Python Bootcamp

### Basics and control flow
- **`assignment_question.ipynb`**: my answers for Python basics: Hello World, user input, positive/negative checks, largest of three, factorial, data types, swapping, °C→°F, palindromes, leap years, sorting.
- **`assignments.ipynb` / `assignment_solutions.ipynb`**: control flow prompts and reference: if/elif/else, nested ifs, loops, `break`/`continue`/`pass`, digit sums, prime check, Fibonacci.

### Data structures
- **`Module_3_Data_Structures_Assignments.ipynb`**: my list exercises: slicing, comprehensions, filtering, sorting, nested lists, sorting dicts by key, matrix transpose, flattening, rotation, intersection.
- **`list_Assignment.ipynb`**, `list_assignment_solution.ipynb`: list prompts and reference.
- **`tuple_assignment_with_code_cells.ipynb`**: tuple creation, slicing, nesting, unpacking, and immutability.
- **`sets_assignment_with_code_cells.ipynb`**: set operations (union, intersection, difference), set comprehensions, removing duplicates.
- **`dictionaries_assignment_with_code_cells.ipynb`**: dict methods, iteration, nested dicts, dict comprehensions, merging, `defaultdict`/`Counter`, JSON conversion.

### Functions
- **`advancefunctions_with_code_cells.ipynb`**: memoized Fibonacci, the mutable-default-argument pitfall, `**kwargs` filtering, callbacks, functions returning functions, a timing decorator, filter-and-map higher-order functions, composition, `partial`, generators, currying, keeping state between calls.
- **`itergenerdecorquestions_with_code_cells.ipynb`**: custom iterators and iterable classes, generator functions, expressions and pipelines, decorators (with arguments, nested, class decorators).

### Modules, files and errors
- **`packagesquestion_with_code_cells.ipynb`**: importing, aliasing, `from … import`, `sys.path`, handling `ImportError`, and using my own package.
- **`my_package/`**: a small package I built (`add` in `module1`, `multiply` in `subpackage/module2`) to practice `__init__.py` and relative imports.
- **`filehandlingquestions_with_code_cells.ipynb`**: reading, writing, copying, and appending files; counting words; reversing contents; binary files; CSV and JSON; splitting a large file into parts (`manyfiles/`) and merging files. The `.txt`, `.csv`, `.json` and `.bin` files in `python/` are the inputs and outputs of these exercises.
- **`exceptionhandlingquestions_with_code_cells.ipynb`**: `try/except/else/finally`, multiple exceptions, custom exceptions, re-raising, handling bad user input and failed HTTP requests (`requests`).

### Object-oriented programming
- **`classesobjectquestions_with_code_cells.ipynb`**: classes, constructors, private attributes (a `BankAccount`), inheritance, `__str__`, composition, class/static methods, properties, ABCs, operator overloading (`Vector.__add__`), a custom exception, a context-manager class, method chaining.
- **`inhertiancequestions_with_code_cells.ipynb`**: single and multiple inheritance, method overriding, `super()`, MRO and the diamond problem, `isinstance` checks.
- **`oopsquestion_with_code_cells.ipynb`**: polymorphism, abstraction with ABCs, encapsulation with getters/setters.

### Data analysis: `python/data_analyis/`
- **`numpy.ipynb`**: creating arrays, reshaping, indexing, vectorized operations, broadcasting, statistics.
- **`numpyassignments_with_code_cells (1).ipynb`**: my NumPy assignments: array manipulation, slicing, linear algebra, statistics, masked arrays (`numpy.ma`).
- **`pandas.ipynb`**: Series and DataFrames, selection with `loc`/`iloc`, adding and dropping columns, working with `sales_data.csv`.
- **`pandasasssignments_with_code_cells.ipynb`**: my Pandas assignments: indexing, filtering, cleaning missing values, `groupby` aggregation, merging, pivoting.
- **`datamanipulation.ipynb`**: handling missing values, renaming, changing dtypes, `apply`, `groupby`/`agg`, `merge` on `data.csv`.
- **`readdata.ipynb`**: reading and writing JSON, CSV from a URL (UCI wine dataset), Excel, and pickle.
- **`matplotlib.ipynb`**: line, bar, histogram, scatter, pie, and subplot charts, then plotting real sales data.
- **`seaborn.ipynb`**: scatter, line, bar, box, violin, histogram/KDE, pair plots, and heatmaps on the sales dataset.
- **`SQLite3/Module_SQLite3_Assignments_Questions.ipynb`**: my SQLite3 work: creating tables, CRUD queries, transactions, relationships, indexing, and database backups (`test.db`, `backup.db`).

### Logging: `python/Logging/`
- **`Module_Logging_Assignments_Questions.ipynb`**: basic logging, file and stream handlers, custom formats, rotating file handlers, logging exceptions, contextual logging, dict-based config. The `.log` files are its output.

### Concurrency: `python/Process_and_Threads/`
Scripts that compare running time with and without concurrency (the timings are in the code comments):
- **`multi_threading.py`**: two threads printing numbers and letters at the same time.
- **`multi_process.py`**: two processes computing squares and cubes in parallel.
- **`advance_multi_threading.py`**: `ThreadPoolExecutor.map` (about 14 s → about 5 s).
- **`advance_multi_processing.py`**: `ProcessPoolExecutor.map` (about 20 s → about 8 s).
- **`factorial_multi_processing.py`**: very large factorials with `multiprocessing.Pool`.
- **`webscrapping_multi_threading.py`**: fetching several web pages in parallel with `requests` and BeautifulSoup.

### Flask: `python/FLASK/`
- **`app.py`**: a minimal Flask app with two routes.
- **`main.py`**: rendering HTML templates (`templates/index.html`, `about.html`).
- **`getpost.py`**: handling GET and POST, submitting a form (`form.html`) and reading `request.form`.
- **`api.py`**: a small REST API for a to-do item list, returning JSON with `jsonify`.

---

## `New folder/`: ML feature engineering

| My notebook | Tutor's lecture version | What it covers |
|---|---|---|
| `Handling_missing_values.ipynb` | `1.0-Handling Missing values` | Kinds of missingness (MCAR/MAR/MNAR) on the Titanic dataset, dropping rows/columns, mean/median/mode imputation |
| `handing_imbalanced_dataset.ipynb` | `2.0-Handling Imbalance Dataset` | Building a 90/10 imbalanced dataset and fixing it by up- and down-sampling with `sklearn.utils.resample` |
| `smote_practice.ipynb` | `3.0-SMOTE` | Generating synthetic minority samples with `imblearn`'s SMOTE on `make_classification` data and plotting before and after |
| `Outliers.ipynb` | `4.0-Handling Outliers` | Five-number summary, IQR, lower and upper fences, spotting outliers with box plots |
| `Nominal_or_OHE.ipynb` | `5.0-Nominal or OHE` | One-hot encoding with `OneHotEncoder` (also on the `tips` dataset) |
| `Label_ordinal.ipynb` | `7.0-Label and Ordinal` | `LabelEncoder` vs `OrdinalEncoder` with an explicit category order |
| — | `8.0-Target Guided Ordinal Encoding` | Encoding categories by the mean of the target |

### `New folder/eda/`: EDA projects
- **`wine_quality.ipynb`** (my version of `1.0-WinequalityEDA`): red wine quality dataset (`winequality-red.csv`). Checks for duplicates and missing values, looks at the quality distribution, and studies correlations with heatmaps, histograms, and scatter plots.
- **`flight.ipynb`** (my version of `2.0-EDA And FE Flight Price`): flight price data (`flight_price.xlsx`). Splits dates and times into day, month, hour, and minute, converts duration to minutes, maps stops to numbers, and one-hot encodes airline, source, and destination.
- **`Google-Playstore.ipynb`** (my version of `3.0-EDA And FE Google Playstore`): cleans the Google Play Store dataset (converts reviews, sizes with `M`/`k`, installs with `+`/`,`, and prices to numbers; parses dates; removes duplicates), then explores categories, ratings, installs, and paid vs free apps. Saves the result to `google_cleaned.csv`.

---

## Running the code

```bash
python -m venv venv
venv\Scripts\activate        # Windows  (source venv/bin/activate on macOS/Linux)
pip install -r python/requirements.txt imbalanced-learn openpyxl requests beautifulsoup4
jupyter notebook
```

Run each notebook from its own folder, because they load their data files using relative paths.
