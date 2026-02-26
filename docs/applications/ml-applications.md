# Machine Learning in Information Contexts (Under Construction)

## CV

## NLP

## Text and data mining

Text and data mining, often abbreviated as TDM, refers to methods for extracting patterns, structures, or insights from large collections of documents. TDM often uses machine learning, but it can also include rule-based techniques and statistical analysis.

In information organizations, TDM can support:

- Exploration of large digitized collections
- Discovery of recurring themes or entities
- Automation of metadata creation and enrichment
- Research in digital humanities and social science
- Analysis of user feedback or service logs, when privacy and governance allow

TDM does not automatically produce truth. It produces patterns. Interpreting those patterns responsibly requires domain knowledge, validation, and attention to bias and data quality.

### Classification

Classification assigns documents to predefined categories. In practice, this is often supervised learning.

Examples:
- Identifying whether a document is a policy, a report, or a news article
- Tagging items as local history, genealogy, or government information

### Clustering

Clustering groups documents based on similarity without predefined categories.

Examples:
- Discovering clusters of community concerns in public comments
- Grouping archival items by thematic similarity for exploration

### Sentiment analysis

Sentiment analysis aims to estimate affective tone, such as positive or negative sentiment, in text. It is commonly treated as a classification task.

Sentiment analysis can be useful for summary views of large datasets, but it can be unreliable for sarcasm, domain specific language, and mixed sentiment.

### Topic modeling

Topic modeling aims to identify recurring word co-occurrence patterns that can be interpreted as themes.

Topic models can support exploratory analysis of large collections. They do not guarantee that topics correspond to meaningful human categories. Human interpretation is required.

!!! example "Hands on: Choose the right TDM technique"

    **Goal:** Match a question to a suitable TDM technique.

    For each question below, pick the most suitable technique.
    Choose from classification, clustering, sentiment analysis, or topic modeling.

    1. A library wants to route patron emails to the correct service unit.
    2. A digital humanities researcher wants to explore recurring themes in a corpus of letters.
    3. A library wants to summarize overall tone in public feedback comments.
    4. An archive wants to explore whether its collection contains distinct thematic groups that are not already labeled.

    For each answer, write one sentence explaining why the technique fits the question.

### Applications of TDM in libraries and information organizations

#### Metadata enrichment

TDM can support metadata creation by suggesting subject terms, extracting named entities, or identifying likely genres. In practice, automated suggestions often require human review, especially when metadata have policy or interoperability implications.

#### Digital humanities research

Researchers can use topic modeling, classification, and entity extraction to explore patterns across large corpora. These methods can help generate hypotheses and guide closer reading.

#### User behavior analysis

Analysis of interaction logs can support system improvement, such as identifying confusing navigation paths or unmet information needs. This area requires careful governance because user data can be sensitive.

#### Collection development

TDM can help identify gaps or trends in collections by analyzing holdings, publication metadata, and usage patterns. It can also support comparative analysis across collections, if data access and licensing permit.

!!! example "Hands on: Responsible use case design"

    **Goal:** Design a TDM use case that is useful and ethically defensible.

    Pick one application area above.

    Write a short plan that includes:

    1. The decision or insight you want to support
    2. The data you would use, including where they come from
    3. The method you would consider, such as classification or topic modeling
    4. One risk related to bias or privacy
    5. One mitigation step, such as human review, transparency to users, or data minimization

    Keep the plan realistic. Assume limited staff time.

## Recommendation

## Explainability

## Further information

- https://www.hathitrust.org/
- https://voyant-tools.org/
- https://text-processing.com/demo/
- https://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/