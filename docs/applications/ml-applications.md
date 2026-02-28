# Machine Learning in Information Contexts

## Computer vision

Computer vision (CV) refers to computational methods that enable machines to process and analyze visual data such as images and videos. Computer vision often relies on machine learning models trained on large datasets.

In information contexts, computer vision is not about "seeing like humans." Instead, systems are trained on many labeled examples and learn to associate recurring pixel patterns with specific categories or objects.

In libraries, archives, and information systems, CV can support:

* Digitization and image processing
* Optical character recognition (OCR)
* Assisted description and tagging of visual collections
* Quality control for scanned materials, such as detecting skew, page boundaries, or missing pages

The introduction of large labeled datasets such as [ImageNet](https://en.wikipedia.org/wiki/ImageNet), and the strong performance of deep neural networks like [AlexNet](https://en.wikipedia.org/wiki/AlexNet) in 2012 image classification benchmarks, marked a shift toward large-scale data-driven approaches that established deep learning as a dominant method in modern computer vision.

### How do computer vision models process images?

At a basic level, computer vision systems transform images into numerical data. An image is not treated as a meaningful picture by the model. It is represented as a grid of small units called [pixels](https://www.geeksforgeeks.org/computer-graphics/what-is-a-pixel/), and each pixel is described by numerical values such as brightness or color.

Machine learning models analyze patterns in these numerical values. Rather than being given explicit visual rules (for example, “a face has two eyes and a nose”), the system is trained on many labeled examples. For example:

- In image classification, training images are labeled with categories.
- In object detection, training images include annotations showing where objects are located.
- In OCR, training data include images of text paired with the correct transcribed characters.

If certain pixel patterns frequently appear in images labeled with a particular category, the model gradually adjusts its internal parameters to increase the likelihood of predicting that category when similar patterns appear again.

The effectiveness of this process depends heavily on the quantity and quality of labeled training data, the consistency of annotation practices, and the similarity between training data and real-world inputs.

If a model is trained on modern, high-resolution photographs and later applied to degraded historical scans, its performance may decrease.

Predictions remain probabilistic. The system estimates how likely an image belongs to a category or contains a certain object. These estimates do not represent certainty or human-level interpretation.

### Common computer vision tasks

Computer vision supports several tasks. Although these tasks differ in output format, they share a common foundation: learning statistical mappings from pixel patterns to structured outputs.

**Image classification**

Image classification assigns an entire image to a predefined category.

Examples:

* Identifying whether an image contains a manuscript, a map, or a photograph
* Classifying archival photos by type (portrait, landscape, event)

**Object detection**

Object detection identifies specific objects within an image and locates them, often using bounding boxes.

Examples:

* Detecting faces or human figures in historical photographs (detection is not identity recognition)
* Locating repeated visual elements in digitized collections, such as stamps, seals, or illustrations
* Detecting pedestrians, vehicles, or traffic signs in autonomous driving systems

Object detection is more complex than simple classification because it requires both identification and spatial localization.

**Optical Character Recognition (OCR)**

OCR converts images of text into machine-readable text.

Examples:

* Converting scanned newspapers into searchable documents
* Extracting text from archival letters

OCR performance depends heavily on image quality, font type, language, layout structure, etc. 

**Image captioning**

Image captioning systems generate short textual descriptions of images.

Examples:

* Generating draft alt text for accessibility
* Producing brief descriptive text to support search and discovery

These systems typically combine computer vision models with natural language generation models. However, generated descriptions may omit important context, reflect biases in training data, or introduce inaccuracies.

### Limitations and Risks

* Training data bias may lead to unequal performance across demographic groups.
* Historical materials may differ significantly from the datasets on which models were trained.
* Visual systems may misclassify rare, ambiguous, or degraded objects.
* Privacy concerns may arise when analyzing user-uploaded images or surveillance footage.

!!! example "Hands on: Exploring Face Detection"

    **Goal:** Evaluate how computer vision detects faces using a pre-built demo.

    Visit the Microsoft Azure Vision demo:
    https://portal.vision.cognitive.azure.com/demo/face-detection

    Use the sample images provided on the page. 
    You do not need to sign in or upload your own photo.

    Click different sample images and observe how the system draws bounding boxes around detected faces.

    Reflect on the following:

    1. Does the system correctly detect all visible faces?
    2. Does it detect faces when they are partially obscured?
    3. What information does the system output besides face location, if any?
    4. What ethical or privacy concerns might arise if similar systems were applied to large-scale digitized collections?

    This demo performs face detection, which means locating faces in an image. It does not identify who the person is. Consider the difference between detecting a face and recognizing identity.

!!! example "Hands on: Visual Recognition with Google Images"

    **Goal:** Observe how computer vision connects visual input to search, ranking, and information retrieval systems.

    Visit:
    https://images.google.com/

    Click the camera icon and upload an image of your choice.

    Step 1:
    Upload the image and examine the full results page.

    Step 2:
    Observe what the system returns:
    - Does it generate a textual description or summary?
    - Does it identify a specific person, place, or object?
    - Does it provide contextual information (e.g., location, historical background)?
    - Does it display visually similar images?

    Reflect on the following:

    1. Is the system producing a single answer or a structured set of ranked results?
    2. What additional information sources appear to be integrated (e.g., web content, knowledge panels)?
    3. How might computer vision be combined with search indexing and ranking algorithms?
    4. What assumptions does the system make when presenting a summary at the top of the page?
    5. Could incorrect identification affect how users interpret the image?

### Further information

- Why Computer Vision Is a Hard Problem for AI
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/YOKPo-I6cgs"
    title="Why Computer Vision Is a Hard Problem for AI"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

- [AI unlocks ancient Dead Sea Scrolls mystery](https://www.bbc.com/news/world-middle-east-56842712)
- [Digitizing the paper of record: Archiving digital newspapers at the New York Times](https://doi.org/10.1177/14648849211023849)
- [Managing the risks of inevitably biased visual artificial intelligence systems](https://www.brookings.edu/articles/managing-the-risks-of-inevitably-biased-visual-artificial-intelligence-systems/)
- [Computer Vision Tagging the Metropolitan Museum of Art's Collection: A Comparison of Three Systems](https://doi.org/10.1145/3446621)
- [Unmasking the bias in facial recognition algorithms](https://mitsloan.mit.edu/ideas-made-to-matter/unmasking-bias-facial-recognition-algorithms)

## Natural language processing

Natural language processing (NLP) refers to computational methods for analyzing and generating human language. NLP systems work primarily with text and sometimes speech converted into text.

Instead of understanding language as humans do, these systems convert words into numerical representations and learn statistical patterns from large collections of examples. This allows them to classify documents, extract names or dates, summarize content, or generate responses.

In information contexts, NLP systems are typically used to structure large volumes of text so that they can be searched, categorized, or analyzed at scale.

In libraries, archives, and information systems, NLP can support:

- Automated classification of documents
- Identification of names, places, and organizations
- Keyword extraction
- Summarization of long texts
- Question answering and chatbot systems
- Language translation

### How do NLP systems process text?

NLP systems convert text into numerical form so that it can be processed mathematically. A document is not treated as meaning in itself, but as sequences of smaller units that can be analyzed statistically.

Before machine learning is applied, text often goes through [preprocessing](https://www.geeksforgeeks.org/nlp/text-preprocessing-for-nlp-tasks/) steps. These steps make the text more structured and consistent.

One common step is [**tokenization**](https://www.geeksforgeeks.org/nlp/nlp-how-tokenizing-text-sentence-words-works/), which divides text into smaller units such as words or sub-word segments. For example, a sentence may be split into individual word tokens so that each can be analyzed separately. In some languages, identifying word boundaries is straightforward. In others, segmentation requires more complex processing.

Another step is **normalization**, which reduces superficial variation. This may include converting text to lowercase, standardizing spelling, or removing punctuation.

Some systems also apply [**stemming**](https://www.geeksforgeeks.org/machine-learning/introduction-to-stemming/) or [**lemmatization**](https://www.geeksforgeeks.org/python/python-lemmatization-with-nltk/), which reduce related word forms to a common base. For example, “running,” “runs,” and “ran” may be treated as variations of the same underlying term. This can help models recognize related patterns, though it may also remove useful distinctions.

For example, converting all text to lowercase may treat “May” (the month) and “may” (a modal verb) as the same word, or “US” (United States) and “us” (the pronoun) as identical, even though they refer to different meanings.

After these transformations, the text is converted into numerical representations. These representations allow the model to measure statistical relationships between words, phrases, and larger patterns.

During training, the system is exposed to large collections of text. In some cases, the data are paired with known outputs, such as document categories or labeled entities. In other cases, the system learns from raw text without explicit labels by identifying recurring statistical regularities.

Rather than relying on explicit grammatical rules written by experts, modern NLP systems learn patterns directly from data. Depending on the task, this may involve learning from labeled examples or from large amounts of unlabeled text. Across these settings, the model adjusts internal parameters to better capture recurring language patterns. It does not encode linguistic knowledge symbolically, but learns statistical relationships between language inputs and outputs.

### Common NLP task types

The following NLP tasks are common in information contexts.

**Text classification**

Text classification assigns documents or passages to predefined categories.

Examples:

- Classifying patron emails by service type
- Identifying whether a document is a policy, report, or news article
- Detecting spam or inappropriate content

**Sentiment analysis**

Sentiment analysis estimates affective tone, such as positive, negative, or neutral sentiment, in text.

At a general level, sentiment analysis treats tone as a classification problem. The system is trained on examples of text that have been labeled according to sentiment categories. During training, it learns statistical associations between language patterns and these labels.

Such patterns may include:

- The presence of evaluative words (e.g., “excellent,” “disappointing”)
- Repeated intensifiers (e.g., “very,” “extremely”)
- Negation patterns (e.g., “not helpful”)
- Certain phrase structures that frequently appear in opinionated writing

After training, the model estimates the likelihood that new text belongs to one of the sentiment categories based on learned correlations.

Sentiment analysis can support high-level summaries of large datasets, such as aggregating overall tone in user feedback.

However, performance may degrade when handling sarcasm, irony, domain-specific language, mixed sentiment within the same document, or historical texts whose language conventions differ from modern training data. Because sentiment categories are simplified representations of affect, results should be interpreted cautiously.

**Named entity recognition (NER)**

Named entity recognition identifies and labels entities within text, such as names of people, organizations, dates, or locations.

Examples:

- Extracting author names from archival documents
- Identifying geographic references in historical letters
- Detecting organization names in grant proposals

**Information extraction**

Information extraction identifies structured facts or relationships from unstructured text.

Examples:

- Extracting publication dates and titles from records
- Identifying relationships between individuals mentioned in archival collections

**Text summarization**

Text summarization produces shorter versions of longer documents.

Examples:

- Creating brief summaries of policy documents
- Generating abstracts from reports

**Question answering and chat systems**

NLP models can generate responses to user queries based on patterns learned from large text collections.

Examples:

- AI-driven reference assistants
- Internal knowledge base search tools
- FAQ automation systems

Such systems generate responses probabilistically and may produce plausible but inaccurate statements.

### Limitations and Risks

- Models may reflect biases present in training data.
- Domain shift (for example, historical language versus modern training corpora) can reduce performance.
- Ambiguity, metaphor, and sarcasm remain difficult for computational systems.
- Outputs are probabilistic and may contain factual inaccuracies.
- Privacy concerns may arise when analyzing user communications.

As with computer vision and text and data mining, NLP systems generate statistically derived outputs rather than grounded semantic understanding.

Large language models are a recent development within this broader NLP landscape.

!!! example "Hands on: Exploring Named Entity Recognition"

    **Goal:** Examine how NLP systems identify entities in text and evaluate their suitability for professional information work.

    Visit:
    [https://demos.explosion.ai/displacy-ent](https://demos.explosion.ai/displacy-ent)

    Paste different types of text into the interface, such as:
    - A short news article
    - A historical document excerpt
    - A library collection description
    - A grant proposal paragraph

    Observe the highlighted entities.

    1. Which entities were correctly identified (e.g., people, organizations, locations)?
    2. Were any entities missed or incorrectly labeled?
    3. Would the extracted entities meet professional metadata or cataloging standards without human review?

!!! example "Hands on: Exploring Statistical Word Associations"

    **Goal:** Examine how word meaning is represented through statistical associations in a corpus.

    Visit:
    [https://demos.explosion.ai/sense2vec](https://demos.explosion.ai/sense2vec)

    Enter one of the following words:

    - bank
    - apple
    - python

    Keep the sense set to "auto."

    Observe the related terms and similarity scores.

    Reflect on the following:

    1. Do the associated terms reflect multiple possible meanings?
    2. What does this suggest about how word meaning is represented?
    3. Does the model understand the concept, or is it capturing co-occurrence patterns?

!!! example "Hands on: Exploring Multiple NLP Tasks"

    **Goal:** Examine how different NLP models process text and evaluate their reliability

    Visit the text-processing demo:  
    [https://text-processing.com/demo/](https://text-processing.com/demo/)

    Choose one or more of the available options:

    - Sentiment analysis  
    - Tokenization  
    - Stemming  
    - Tagging and chunking  

    Enter short texts of different types, such as:

    - A short positive or negative review  
    - A sarcastic or mixed-tone comment  
    - A neutral informational paragraph  
    - A short sentence containing names or locations  

    Observe the system outputs carefully.

    Reflect on the following:

    1. What kind of output does each task produce (e.g., labels, tokens, grammatical tags)?
    2. How does the output differ across tasks?
    3. Where does the system perform well, and where does it struggle?
    4. Would these outputs be reliable enough for professional use without human review?

    Consider how each task reduces language into structured representations, and what may be lost in that process.


### Further information

- Simplilearn: Natural Language Processing In 10 Minutes
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/6I-Alfkr5K4"
    title="Natural Language Processing In 10 Minutes"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

- [GeeksforGeeks: Natural Language Processing (NLP) Tutorial](https://www.geeksforgeeks.org/nlp/natural-language-processing-nlp-tutorial/)
- [GeeksforGeeks: Named Entity Recognition](https://www.geeksforgeeks.org/nlp/named-entity-recognition/)
- [GeeksforGeeks: What is Sentiment Analysis?](https://www.geeksforgeeks.org/machine-learning/what-is-sentiment-analysis/)


## Text and data mining

Text and data mining (TDM) refers to computational methods for identifying patterns, structures, or recurring or statistically prominent patterns in large collections of documents. While TDM may involve machine learning, it also includes simpler methods such as counting word frequencies, tracking term trends over time, or applying predefined rules to extract information.

In information organizations, TDM can support:

- Exploration of large digitized collections
- Identification of recurring themes, entities, or terminology
- Assistance with large-scale metadata enrichment through pattern detection and term extraction
- Collection-level research and planning

TDM does not automatically produce interpretation or truth. It produces structured representations of patterns derived from data. Interpreting those patterns requires domain expertise, methodological caution, and attention to bias, sampling limitations, and data quality.

### How does TDM work at a general level?

At a basic level, TDM treats a collection of documents as analyzable data.

Individual documents are transformed into structured representations, such as word counts, term frequencies, or other measurable features. These representations allow the system to compare documents and detect recurring statistical regularities.

Instead of focusing on sentence-level meaning, TDM often emphasizes aggregate behavior:

- How frequently does a term appear over time?
- Which words tend to co-occur across documents?
- Which documents share similar vocabulary patterns?

By identifying these regularities, TDM supports exploratory analysis at scale. The system does not determine meaning on its own. It reveals patterns that researchers or professionals must interpret.

### Common TDM task types

**Classification**

Classification assigns documents to predefined categories based on patterns learned from labeled data.

These patterns may include:

- The presence or frequency of certain words or phrases
- Co-occurrence patterns between terms
- Structural features such as document length or formatting cues
- Stylistic tendencies, such as formal policy language versus conversational tone

For example, documents labeled as “Policy” may frequently contain terms such as “regulation,” “compliance,” or “procedure.” Over many training examples, the model learns statistical associations between such patterns and the assigned category.

Importantly, the system does not encode a conceptual definition of the category. It learns correlations between observable features and labeled outcomes.

Examples:

- Identifying whether a document is a policy, report, or news article
- Tagging items as local history, genealogy, or government information

Classification produces probabilistic outputs and may misclassify ambiguous or out-of-domain texts.

**Clustering**

Clustering groups documents based on measured similarity without predefined categories.

Measured similarity refers to numerical comparisons between document representations. After documents are converted into structured features (such as word frequencies or other measurable attributes), the system calculates how similar two documents are based on shared patterns.

Similarity may be influenced by:

- Overlap in vocabulary
- Co-occurring terms
- Similar distributions of key words
- Shared metadata attributes

For example, two documents that frequently use similar terms such as “zoning,” “ordinance,” and “municipal” may be considered more similar to each other than to documents focused on health services.

The clustering algorithm groups documents that are numerically closer to one another according to the chosen similarity measure.

Documents grouped together may share statistical features even if their broader meanings differ. Interpretation of clusters therefore requires human judgment.

Examples:

- Discovering clusters of community concerns in public comments
- Grouping archival items by thematic similarity for exploratory analysis

**Topic modeling**

Topic modeling identifies recurring word co-occurrence patterns within a corpus.

At a general level, topic modeling examines how words tend to appear together across many documents. If certain terms frequently co-occur. For example, “budget,” “appropriation,” “committee,” and “legislation”, the model may group them into a shared word cluster.

Unlike classification, topic modeling does not rely on predefined categories. Instead, it examines how words tend to appear together across many documents and groups those recurring patterns.

Each document is then represented as a mixture of these word clusters in varying proportions. A single document may reflect multiple clusters rather than belonging to only one.

These clusters can be interpreted as thematic structures, but the model does not assign meaning to them. It detects patterns of co-occurrence, not concepts. Human interpretation is required to decide whether a cluster corresponds to a meaningful theme, whether labels are appropriate, and whether results are analytically useful.

Topic models support exploratory investigation at scale rather than definitive classification or interpretation.

!!! example "Hands on: Exploring Corpus Patterns with Voyant"

    **Goal:** Examine how corpus-level pattern analysis differs from individual document interpretation.

    Visit:
    [https://voyant-tools.org/](https://voyant-tools.org/)

    Upload or paste a small corpus (e.g., several short documents, letters, or public comments).

    Explore the following tools:
    - Word frequency
    - Cirrus (word cloud showing term frequency by size)
    - Collocates (words that frequently appear near a selected term)
    - Context view (showing how a word appears in different sentences)

    Reflect on the outputs:

    1. Which terms appear most frequently?
    2. Do high-frequency words necessarily represent the most important concepts?
    3. How do collocations shape your interpretation of themes?
    4. What might you miss about meaning or interpretation if you rely only on word counts or word clouds?

    Consider how corpus-level statistical patterns differ from close reading of individual texts.

!!! example "Hands on: Exploring Historical Trends with HathiTrust"

    **Goal:** Examine how large-scale corpus analytics reveal historical language trends without interpreting individual texts.

    Visit the HathiTrust Research Center Analytics portal:
    [https://analytics.hathitrust.org/](https://analytics.hathitrust.org/)

    Then explore Bookworm (HathiTrust):
    [https://bookworm.htrc.illinois.edu/develop/](https://bookworm.htrc.illinois.edu/develop/)

    Use single-word queries to explore trends across time.
    Examples to try:
    - "democracy"
    - "library"
    - "industry"
    - "immigration"
    - "technology"

    Observe the frequency trends across years.

    1. How does the frequency of a term change over time?
    2. Does higher frequency necessarily indicate greater social importance?

### Further information

- [HathiTrust - Text and data mining resources](https://hathitrust.atlassian.net/servicedesk/customer/portal/1/topic/dd359fbc-c095-4319-a223-353ebf0fd5b2)
- [HathiTrust - How to Use HathiTrust Data Resources](https://www.hathitrust.org/member-libraries/resources-for-librarians/data-resources/)
- [Text & Data Mining resources @ UK Library](https://libguides.uky.edu/dsd-services/text-data-mining)
- [Topic Modeling and Digital Humanities](https://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/)
- [ProQuest's TDM Studio](https://proquest.libguides.com/tdmstudio/home)

## Recommendation

Recommendation systems predict which items are likely to be relevant to a user and rank them accordingly. In doing so, they shape visibility by influencing which materials appear more prominently.

From a machine learning perspective, recommendation can be understood as a prediction and optimization problem.

The system is trained on past interaction data, such as:

- Which items were borrowed or accessed
- Which results were clicked
- Which items were frequently accessed together

Based on these data, the model learns to estimate the likelihood that a user will interact with a given item. During training, the system compares predicted interactions with observed behavior. A loss function measures the difference, and model parameters are adjusted to reduce this loss.

In other words, recommendation systems learn statistical mappings between users, items, and interaction outcomes.

Recommendation systems typically optimize measurable metrics, such as:

- Click-through rate
- Borrowing frequency
- Time spent interacting with materials
- Other engagement indicators

The choice of objective function shapes ranking outcomes. If the system optimizes for engagement alone, it may amplify already popular materials or reinforce existing usage patterns.

### Limitations and risks

- Historical interaction data may reflect existing inequalities or popularity bias.
- New users or new materials may be disadvantaged due to limited interaction history.
- Personalization may narrow exposure to alternative perspectives.

As with other machine learning systems, recommendation outputs reflect statistical predictions derived from past data rather than explicit semantic understanding of user intent.

### Further information

- [Google - Recommendation systems overview](https://developers.google.com/machine-learning/recommendation/overview/types)

## Applications of Machine Learning in Libraries and Information Organizations

In practice, machine learning in libraries and information organizations is integrated into workflows rather than deployed as isolated techniques. The following examples illustrate common institutional applications.

### Metadata Generation and Enrichment

Machine learning can support large-scale metadata creation and enhancement for digital collections. Systems may assist in extracting names, dates, or places, suggesting subject terms, or identifying visual elements in digitized materials.

These tools can improve efficiency, particularly for large backlogs. Final metadata decisions, however, remain a professional responsibility.


### Discovery, Ranking, and Recommendation

Machine learning influences how materials are surfaced to users, including search result ranking and item recommendations.

Because ranking affects visibility, these systems shape patterns of access, circulation, and discovery. Design choices, therefore, have institutional and equity implications.

### Large-Scale Corpus Analysis

Collections may be analyzed as corpora to identify recurring themes, shifts in terminology, or patterns across large document sets.

Such analyses support exploratory research and institutional insight at scale.


### User Interaction and Service Automation

Machine learning can support user-facing services such as chat-based assistance, automated inquiry routing, and predictive support systems.

While these tools may improve efficiency for routine tasks, complex or sensitive interactions continue to require human judgment.

### Digitization and Collection Processing

Machine learning can assist in large-scale digitization workflows, including layout detection, image quality assessment, and descriptive tagging of visual materials.

These tools can reduce manual workload but require validation in preservation and archival contexts.