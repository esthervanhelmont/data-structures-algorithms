# Data Structures & Algorithms | Gender Equity Employment Gap Monitor

## Project overview

This project is a technical report for a software application that could be used by a gender equity NGO.

The application is called the **Gender Equity Employment Gap Monitor**.

Its purpose is to help an NGO:

- compare employment rates for women and men;
- identify countries with larger employment gaps;
- sort large amounts of data;
- filter data by country, region and year;
- prepare simple summaries for dashboards and reports.

The main value used in this project is:

```text
employment gap = male employment rate - female employment rate
```

A higher value means that the difference between men and women is larger.

This project is connected to:

- **SDG 5: Gender Equality**
- **SDG 8: Decent Work and Economic Growth**

> The dataset is artificial. It was created for technical testing and should not be used to make real policy decisions.

---

## Main deliverable

The main deliverable is the Jupyter Notebook:

```text
IC_Data_Structures_Algorithms_Final_Capstone.ipynb
```

The notebook contains the complete technical report, Python code, experiment results, graphs and recommendations.

---

## Project goals

The project:

- creates an artificial dataset with 5,000 records;
- implements three sorting algorithms;
- compares algorithm performance;
- measures execution time in milliseconds;
- tests different input orders;
- checks if every sorting result is correct;
- recommends data structures for the application;
- explains the technical choices in simple English.

---

## Artificial dataset

The dataset contains exactly **5,000 artificial observations**.

Each record contains:

| Column | Meaning |
|---|---|
| `record_id` | Unique number for the observation |
| `country` | Artificial country code |
| `region` | Region connected to the country |
| `year` | Year between 2010 and 2024 |
| `female_employment_rate` | Artificial employment rate for women |
| `male_employment_rate` | Artificial employment rate for men |
| `employment_gap` | Difference between male and female employment |
| `unpaid_work_minutes` | Artificial unpaid work estimate |
| `women_in_leadership_pct` | Artificial leadership percentage |

The dataset contains no missing values.

### Dataset versions

The same 5,000 records are organized in four different ways:

| Version | Description |
|---|---|
| Random | Records are in a mixed order |
| Already sorted | Records are already ordered from low to high |
| Reverse sorted | Records are ordered from high to low |
| Nearly sorted | Most records are sorted, but 50 pairs are switched |

This makes it possible to test how the order of the input data affects performance.

---

## Sorting algorithms

Three sorting algorithms were implemented manually.

### Bubble Sort

Bubble Sort compares neighbouring records and switches them when they are in the wrong order.

**Advantage**

- easy to understand;
- can stop early when the data is already sorted.

**Disadvantage**

- very slow for large unsorted datasets.

**Recommended use**

- learning;
- very small lists;
- simple demonstrations.

### Merge Sort

Merge Sort divides the data into smaller parts and combines these parts in the correct order.

**Advantage**

- fast and predictable;
- performs well on large datasets.

**Disadvantage**

- needs extra memory.

**Recommended use**

- large datasets;
- situations where stable performance is important.

### Quick Sort

Quick Sort divides the data around a pivot value.

**Advantage**

- often very fast;
- suitable for data stored in memory.

**Disadvantage**

- performance depends on the pivot and the input data.

**Recommended use**

- general in-memory sorting;
- larger datasets.

---

## Performance experiment

Every algorithm was tested on all four dataset versions.

Each test was repeated **three times**.

The notebook reports:

- average execution time;
- fastest execution time;
- slowest execution time;
- standard deviation.

All times are reported in **milliseconds**.

Before accepting a result, the notebook also checks if the complete output is correctly sorted.

### Main performance conclusion

The executed notebook reported:

- **Overall fastest:** Merge Sort (7.024 ms)
- **Overall slowest:** Bubble Sort (1005.666 ms)

The exact timing can change slightly on another computer.

The general conclusion is still clear:

- Bubble Sort is easy to understand, but normally too slow for a large application.
- Merge Sort gives stable and predictable performance.
- Quick Sort is efficient and usually performs well for in-memory data.
- For a real Python application, the built-in `sorted()` function or Pandas `sort_values()` would normally be preferred.

---

## Time complexity

| Algorithm | Best case | Average case | Worst case |
|---|---:|---:|---:|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

`O(n²)` grows quickly when the dataset becomes larger.

`O(n log n)` normally grows more slowly.

This explains why Merge Sort and Quick Sort are more suitable for large datasets.

---

## Data structure recommendations

The application needs different data structures for different tasks.

### 1. List

A list stores multiple records in one ordered collection.

**Application use**

- store records that need to be sorted;
- store all employment gap values;
- keep duplicate values.

### 2. Dictionary

A dictionary stores key-value pairs.

**Application use**

- store one complete observation;
- store country summaries;
- quickly find information using a country code.

### 3. Set

A set stores unique values.

**Application use**

- create unique region filters;
- create unique year filters;
- remove duplicate options from dropdown menus.

### 4. Tuple

A tuple stores a fixed combination of values.

**Application use**

- create a key such as `("NLD", 2024)`;
- find records for one country in one year.

### Recommended combination

For the prototype:

- use lists for collections that need to be sorted;
- use dictionaries for records and summaries;
- use sets for unique filters;
- use tuples for fixed lookup keys.

For a real application with millions of records, the data should be stored in a database.

---

## Final recommendation

For the Gender Equity Employment Gap Monitor:

1. Do not use Bubble Sort for large unsorted datasets.
2. Use Merge Sort when predictable performance is important.
3. Use Quick Sort for efficient in-memory sorting.
4. Use Python's optimized sorting tools in a production application.
5. Use lists, dictionaries, sets and tuples for different application tasks.
6. Move the data to a database when the application becomes larger.

---

## Final conclusion

This project shows that algorithm choice matters.

All three algorithms produced the correct result, but they did not need the same amount of time.

Simple algorithms can be useful for learning, but efficient algorithms are better for large datasets.

The project also shows that data structures have different jobs.

Choosing the correct algorithm and data structure helps make an application:

- faster;
- easier to understand;
- easier to filter;
- easier to maintain.

The proposed technical building blocks could help a gender equity NGO explore large datasets more efficiently.

---

## Limitations

- The dataset is artificial.
- The results do not describe real countries.
- Timing can change between computers.
- The experiment measures execution time, but not memory use.
- The prototype keeps all records in Python memory.
- A real application needs validated and current gender equity data.
- More testing is needed before creating a production system.

---

## How to run the notebook

### Requirements

- Python 3
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook or VS Code with the Jupyter extension

Install the packages with:

```bash
pip install numpy pandas matplotlib notebook
```

### Run the project

1. Download or clone the repository.
2. Open `IC_Data_Structures_Algorithms_Final_Capstone.ipynb`.
3. Select a Python kernel.
4. Choose **Restart Kernel and Run All**.
5. Check that all tables and graphs are visible.

---
