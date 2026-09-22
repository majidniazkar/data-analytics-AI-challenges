# Challenge 1 - A recommender system for online shops

**Topic:** recommender systems &nbsp;|&nbsp; **Techniques:** data cleaning, language
detection, weighted multi-criteria scoring &nbsp;|&nbsp;
**Data:** 500 books from [Open Library](https://openlibrary.org)

The original brief as handed out is preserved in [`challenge.pdf`](challenge.pdf).

## Scenario

You are a data scientist working for a company. The current task is to build a recommender
system for an online marketplace. The recommender system is a Python program that suggests
a list of the five top books on *machine learning*. The criteria it uses are the year of
publication (the more recent, the better), the number of editions (the higher the better),
and usefulness for *Python*.

In practice a data scientist would retrieve live data from online platforms. As this is the
first challenge, the task starts simpler: a real dataset from
[openlibrary.org](https://openlibrary.org) has been collected for you and is provided as
the input to the recommender system.

## Dataset

[`data/ml_books_openlibrary.csv`](data/ml_books_openlibrary.csv) - 500 books, 8 columns:

| Column | Notes |
|--------|-------|
| `title` | book title |
| `authors` | comma-separated author list |
| `first_publish_year` | year of first publication |
| `edition_count` | number of known editions |
| `publishers` | **empty in this snapshot** |
| `isbn` | **empty in this snapshot** |
| `subjects` | comma-separated Open Library subject tags |
| `description` | free text, frequently missing |

Because the data is real, it needs cleaning before anything else:

- some books are not genuinely about machine learning, even though the keyword
  `machine learning` was used to collect the dataset;
- there is missing information and there are duplicated entries;
- some titles are in languages other than English and should be removed.

## Scoring criteria

The ranking should reflect three factors:

1. **Publication year.** Machine learning moves fast, so recent books deserve higher scores.
2. **Number of editions.** A good proxy for how useful readers have found a book.
3. **Python relevance.** The user wants to apply the techniques in Python, so `python`
   appearing in the `title`, `subjects` or `description` is a plus.

You may define your own ranking function, as long as the choice is justified.

## Requirements

- Clean the dataset before building the recommender.
- Implement a recommender function that returns the top *N* books.
- Test it for **3, 5 and 10** top books, and check the results are consistent with the
  criteria above.

## Deliverables

A short report of **at most two pages** containing the top 5 books suggested by your code.
Depending on how your recommender performs, the report can also describe the scoring
function, explain how the code cleans the dataset and produces its ranking, and discuss the
limitations of your implementation and how it could be improved.

## Optional extension (extra credit)

Enrich the dataset with additional books or additional fields gathered from online
platforms, and show what that does to the recommendations.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
