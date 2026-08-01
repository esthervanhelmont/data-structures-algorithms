# Technical Report  
## Gender Equity Employment Gap Monitor

**Author:** Esther van Helmont  
**Project:** Data Structures & Algorithms Capstone  
**Main deliverable:** `IC_Data_Structures_Algorithms_Final_Capstone.ipynb`

---

## 1. Executive summary

For this project, I imagined a software application for an NGO working in gender equity.

The application is called the **Gender Equity Employment Gap Monitor**.

Its main purpose is to help an NGO explore a large amount of gender equity data. The application could compare employment rates for women and men, show the largest employment gaps and prepare information for dashboards or reports.

The most important technical question was:

> Which sorting algorithm is suitable when the application needs to sort a large amount of data often?

To answer this question, I created an artificial dataset with **5,000 gender equity records**. I implemented and tested three sorting algorithms:

- Bubble Sort;
- Merge Sort;
- Quick Sort.

I tested the algorithms on four versions of the same dataset and repeated every test three times.

The main result was clear. **Merge Sort was the fastest algorithm overall, with an average time of approximately 7.024 ms. Bubble Sort was the slowest, with an average time of approximately 1005.666 ms.**

Based on the experiment, I would not recommend Bubble Sort for a real application with large datasets. Merge Sort, Quick Sort or Python's optimized built-in sorting tools are better choices.

---

## 2. Application idea

The proposed application helps an NGO find and compare gender inequality in employment.

Each record can contain information such as:

- country;
- region;
- year;
- female employment rate;
- male employment rate;
- employment gap;
- unpaid work by women;
- women in leadership.

The main value used in this experiment is:

```text
employment gap = male employment rate - female employment rate
```

A higher number means that the difference between the male and female employment rate is larger.

The application could use this information to:

- sort countries from the smallest to the largest gap;
- identify areas that may need more attention;
- compare years and regions;
- create filters for dashboards;
- prepare summaries for NGO reports.

This project connects to **SDG 5: Gender Equality** and **SDG 8: Decent Work and Economic Growth**.

The data in this project is artificial. It is suitable for testing code, but it should not be used to make real conclusions about countries.

---

## 3. Research question

The main research question was:

> How does the choice of sorting algorithm affect the time needed to sort 5,000 artificial gender equity records?

I also wanted to understand whether the original order of the records changes the performance.

For that reason, I tested four dataset versions:

| Dataset version | Description | Reason for testing |
|---|---|---|
| Random | Records are mixed | Represents normal unsorted data |
| Already sorted | Values already go from low to high | Tests if an algorithm can use existing order |
| Reverse sorted | Values go from high to low | Creates a more difficult situation |
| Nearly sorted | Most values are sorted, but 50 pairs are switched | Represents data that only needs a smaller update |

Using the same records for every version keeps the comparison fair. The content and size stay the same. Only the order changes.

---

## 4. Artificial dataset

The experiment uses exactly **5,000 records** and **9 columns**.

The artificial dataset contains:

| Column | Meaning |
|---|---|
| `record_id` | Unique number for each observation |
| `country` | Country code |
| `region` | Region connected to the country |
| `year` | Year between 2010 and 2024 |
| `female_employment_rate` | Artificial employment rate for women |
| `male_employment_rate` | Artificial employment rate for men |
| `employment_gap` | Difference between male and female employment |
| `unpaid_work_minutes` | Artificial estimate of unpaid work |
| `women_in_leadership_pct` | Artificial percentage of women in leadership |

I used a random seed of `42`.

This means that the same artificial data is created every time the notebook is run. This makes the experiment reproducible and the comparison more fair.

The dataset was checked before the experiment:

- 5,000 rows were created;
- no values were missing;
- 20 countries were included;
- 7 regions were included;
- 15 years were included.

---

## 5. Sorting algorithms

### 5.1 Bubble Sort

Bubble Sort compares two neighbouring records.

When the first value is higher than the second value, the records switch places. This continues until the list is sorted.

**Advantages**

- easy to understand;
- easy to implement;
- can stop early when the data is already sorted.

**Disadvantages**

- performs many comparisons;
- becomes very slow when the dataset grows;
- not suitable for frequently sorting large datasets.

**Best use case**

Bubble Sort is useful for learning and for very small lists.

Its average time complexity is `O(n²)`.

---

### 5.2 Merge Sort

Merge Sort divides the list into smaller parts.

It sorts these smaller parts and then combines them in the correct order.

**Advantages**

- fast for larger datasets;
- predictable performance;
- always has `O(n log n)` time complexity.

**Disadvantages**

- creates extra lists;
- therefore uses more memory.

**Best use case**

Merge Sort is useful when stable and predictable performance matters.

---

### 5.3 Quick Sort

Quick Sort selects a pivot value.

Values lower than the pivot go into one group. Equal values go into a second group. Higher values go into a third group. The lower and higher groups are sorted again using the same method.

**Advantages**

- often very fast;
- suitable for data stored in memory;
- worked efficiently in this experiment.

**Disadvantages**

- performance depends on the pivot;
- the worst case can be `O(n²)`.

**Best use case**

Quick Sort is useful for general sorting of larger in-memory datasets.

---

## 6. Experimental method

Every algorithm was tested on every dataset version.

This created:

```text
3 algorithms × 4 dataset versions = 12 combinations
```

Every combination was run three times:

```text
12 combinations × 3 runs = 36 sorting runs
```

I used `time.perf_counter()` to measure the execution time.

The results were converted from seconds to milliseconds.

For every combination, I calculated:

- average execution time;
- fastest execution time;
- slowest execution time;
- standard deviation.

I also checked the complete output after every run. A result was only accepted when all values were in the correct order.

This was important because a fast result has no value when the algorithm sorts the data incorrectly.

---

## 7. Results

### Figure 1: Performance per dataset version

![Figure 1: Average sorting time per dataset version](images/notebook_figure_1.png)

**Figure 1** compares the algorithms on random, already sorted, reverse-sorted and nearly sorted data.

The graph uses a logarithmic scale because Bubble Sort is much slower than Merge Sort and Quick Sort. Without this scale, the faster bars would be difficult to see.

The figure shows that the original order of the data affects performance.

Bubble Sort benefits strongly from data that is already sorted because the implementation can stop early. On random and reverse-sorted data, it has to make many more comparisons.

Merge Sort remains more predictable across the different versions.

Quick Sort also performs efficiently, although its exact time depends on how the pivot divides the data.

---

### Figure 2: Overall average performance

![Figure 2: Overall average sorting time per algorithm](images/notebook_figure_2.png)

**Figure 2** combines the results from the four dataset versions.

The overall result was:

| Result | Algorithm | Average time |
|---|---|---:|
| Fastest | Merge Sort | approximately 7.024 ms |
| Slowest | Bubble Sort | approximately 1005.666 ms |

The exact number can change slightly on another computer. The main pattern is more important than a small timing difference.

Bubble Sort was much slower overall.

Merge Sort and Quick Sort were both more suitable for the 5,000-record dataset.

---

## 8. Interpretation

The experiment shows that an algorithm is not automatically a good choice just because it can sort the data correctly.

All three algorithms returned the correct result, but their performance was very different.

The main reason is their time complexity:

| Algorithm | Best case | Average case | Worst case |
|---|---:|---:|---:|
| Bubble Sort | `O(n)` | `O(n²)` | `O(n²)` |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` |
| Quick Sort | `O(n log n)` | `O(n log n)` | `O(n²)` |

`O(n²)` means that the amount of work can grow very quickly when more records are added.

This is why Bubble Sort becomes a problem for large datasets.

`O(n log n)` grows more slowly. This makes Merge Sort and Quick Sort better choices for an application that needs to sort data often.

---

## 9. Data structure recommendations

The application needs more than one data structure because every structure has a different purpose.

### 9.1 List

A list is useful for storing all records that need to be sorted.

In this project, every sorting algorithm receives a list and returns a sorted list.

**Recommended use**

- storing observations;
- preserving order;
- allowing duplicate values;
- preparing records for sorting.

---

### 9.2 Dictionary

A dictionary stores information as key-value pairs.

One complete observation is stored as a dictionary. This keeps values such as country, year and employment gap connected.

A dictionary is also useful for country summaries.

**Recommended use**

- storing one labelled observation;
- quickly finding a country summary;
- storing algorithms by name;
- organizing application results.

---

### 9.3 Set

A set stores unique values.

The application can use sets to create filter options without duplicates.

**Recommended use**

- unique regions;
- unique years;
- dropdown filters.

A set is not the main structure for sorting because it does not preserve a fixed order.

---

### 9.4 Tuple

A tuple can store a fixed combination such as:

```python
("NLD", 2024)
```

This tuple can be used as a dictionary key.

**Recommended use**

- quickly finding records for one country and year;
- creating fixed lookup combinations.

---

## 10. Technical recommendation

For the prototype, I recommend:

- **lists** for collections of records;
- **dictionaries** for observations and summaries;
- **sets** for unique filters;
- **tuples** for fixed lookup keys.

For sorting, I recommend:

- do not use Bubble Sort for large unsorted datasets;
- use Merge Sort when predictable performance is important;
- use Quick Sort for efficient in-memory sorting;
- use Python's built-in `sorted()` function or Pandas `sort_values()` in a real production application.

The manual algorithms are useful for learning and comparing performance.

For an actual NGO application, optimized and tested library functions would be safer and easier to maintain.

When the amount of data grows to millions of records, I would also move the information into a database. The application should then request only the records needed for a specific analysis or dashboard page.

---

## 11. Limitations

This experiment has several limitations:

- the dataset is artificial;
- the values do not represent real countries;
- execution time can change between computers;
- only three repetitions were used;
- the experiment measures speed but not memory use;
- the complete dataset is kept in Python memory;
- only three sorting algorithms were compared.

A future experiment could:

- use more repetitions;
- measure memory use;
- test larger datasets;
- compare Python's built-in sorting method;
- use validated real-world gender equity data.

---

## 12. Final conclusion

This project helped me understand that choosing an algorithm is not only about getting the correct answer.

Performance also matters.

Bubble Sort was useful because it clearly showed what happens when an algorithm performs too many comparisons. It worked correctly, but it was not a good choice for sorting 5,000 records often.

Merge Sort and Quick Sort were much more suitable for this type of application.

The experiment also showed that the structure of the input data matters. Already sorted data can be much easier for some algorithms than random or reverse-sorted data.

My final recommendation is to use efficient sorting methods together with data structures that match the task:

- lists for sorting;
- dictionaries for labelled data and summaries;
- sets for filters;
- tuples for fixed lookups.

These choices would make the Gender Equity Employment Gap Monitor faster, clearer and easier to maintain.

---

## Appendix: project files

- `IC_Data_Structures_Algorithms_Final_Capstone.ipynb` — complete code, outputs and visualizations
- `README.md` — project overview
- `requirements.txt` — required Python packages

