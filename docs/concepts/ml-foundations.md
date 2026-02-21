# Machine learning foundations

Subsymbolic AI refers to approaches that learn patterns from data rather than relying on explicitly written rules. In this course, subsymbolic AI mainly refers to data-driven statistical learning approaches, especially machine learning models. Machine learning is widely used in information systems because it learns patterns from data and applies those learned patterns to new cases. It is often applied to tasks such as classification, recommendation, and text and data mining.

In symbolic AI, knowledge is explicitly represented, and reasoning follows traceable rules. Subsymbolic AI shifts the emphasis to statistical learning. Instead of encoding domain knowledge as rules, the system learns model parameters from data. This often improves coverage and flexibility, but it can reduce transparency.

## How machine learning works at a general level

Machine learning is a method for building models that learn from data.

We begin with a dataset. A dataset is at minimum a collection of observations. These observations might be documents, images, user records, or other forms of data. In some cases, the dataset includes known outcomes (for example, past emails labeled as spam or not spam). In other cases, it only contains raw inputs without predefined labels (for example, a large collection of digitized newspapers with no assigned categories).

Next, we choose a machine learning model. The model has internal parameters that determine how it processes data. These parameters can be adjusted during training so that the model’s outputs better match the learning objective. When the parameters change, the model’s outputs change.

For example, imagine a simple machine learning model that decides whether a document belongs to “History” based on the words it contains. The model assigns different parameter values to different words. If certain words are strongly associated with historical documents, their parameters increase. If they are not, their parameters decrease. Adjusting these values changes how the document is classified.

To guide this adjustment, we need an objective. The objective specifies what counts as good performance of the machine learning. In this example, the objective is to correctly classify documents as “History” or “Other.”

This objective is usually expressed through a loss function, which provides a concrete way to measure performance during training. A loss function is a rule that measures how far the model’s predictions are from the desired outcome. For instance, if the model classifies a historical document as “Other,” the loss increases. If it classifies the document correctly, the loss decreases. Smaller loss means better performance according to the objective.

During training, the model makes predictions using its current parameters. The loss function evaluates those predictions. The system then adjusts the parameters to reduce the loss. This repeated adjustment process is called optimization.

The model updates its parameters many times. These updates are performed automatically by the training algorithm, not manually by people. Once the objective and optimization method are specified, the system repeatedly adjusts the parameters according to mathematical rules designed to reduce the loss. Over time, it moves toward parameter values that produce lower loss on the training data.

However, performing well on training data does not guarantee useful learning. A model may memorize those examples. This problem is called overfitting. Overfitting occurs when a model performs well on training data but poorly on new data.

To check whether the model has learned meaningful patterns, we evaluate it on separate data that were not used during training. If it performs well on these new cases, we say it shows evidence of generalization.

In summary, machine learning involves:

- A dataset that provides observations.
- A model with adjustable parameters.
- A loss function that measures performance.
- An optimization process that adjusts parameters.
- An evaluation step that checks generalization.

Learning means adjusting parameters so that the model performs well according to a defined objective, not only on past data but also on new cases.

!!! example "Hands on: Experiment with Google Teachable Machine"

    **Goal:** Observe a minimal machine learning workflow in action.

    Visit: https://teachablemachine.withgoogle.com/

    Choose the “Image Project” option.

    Step 1: Create two simple classes.  
    For example:

    - Book
    - Not a book  

    Step 2: Collect training examples.  
    Use your webcam or upload images. Try to provide several examples for each class.

    Step 3: Train the model.  
    Click the “Train Model” button and wait for the system to complete training.

    Step 4: Test the model in real time.  
    Show new objects to the webcam and observe the predictions.

    As you experiment, consider the following:

    1. What counts as the training data in this setup?
    2. What is the input to the model?
    3. What is the output?
    4. What happens if your training examples are very limited?
    5. Can you create a situation where the model makes confident but incorrect predictions?

    Notice that you did not manually adjust any parameters. The system performed optimization automatically based on the examples you provided.

    Think about:

    - How does the quality and diversity of training data affect performance?
    - What kinds of mistakes does the model make?
    - Would you trust this model in a real decision-making context?

## Learning paradigms

Machine learning approaches can be distinguished by the type of feedback signal available during learning. The form of feedback shapes what the model can learn and what kinds of information tasks it is suited for.

### Supervised learning

Supervised learning is used when each training example includes both an input and a known desired output. The model learns a mapping from inputs to targets.

This approach is particularly suitable when outcome categories are clearly defined and historical labeled data are available.

For example, in our earlier scenario of identifying “History” books, supervised learning would require a dataset where each book has already been labeled as “History” or “Other.” The model then learns patterns that distinguish the two categories.

In information science contexts, supervised learning is commonly used for tasks such as:

- Classifying documents into predefined subject categories.
- Assigning metadata fields such as genre or resource type.
- Routing patron questions to specific service units.

The strength of supervised learning lies in its ability to align with established institutional categories. However, it inherits the assumptions embedded in those labels. If labels are inconsistent, biased, or outdated, the model will learn those patterns. Label design is therefore both a technical and an institutional decision.


### Unsupervised learning

Unsupervised learning operates without predefined labels. Instead of predicting known outcomes, the model attempts to detect structure in the data.

Returning to the “History” example, suppose we remove all labels from the books. An unsupervised model might group books based on patterns of word usage. One cluster might contain texts discussing wars and empires. Another might focus on economic history. The model does not know what “History” means. It only identifies statistical similarities.

This approach is appropriate when categories are not yet defined or when exploration is the goal. In information science, unsupervised learning can support:

- Exploring thematic patterns in large digitized collections.
- Discovering recurring topics in archival materials.
- Grouping user feedback comments to detect common concerns.

The output of unsupervised learning does not automatically correspond to meaningful human categories. Clusters and topics require interpretation. For this reason, unsupervised learning is often used for exploratory analysis, and its results typically need human validation before informing decisions.

### Reinforcement learning

Reinforcement learning differs from both supervised and unsupervised approaches. Instead of learning from a fixed dataset, an agent interacts with an environment. It takes actions and receives feedback in the form of rewards or penalties. The objective is to learn a strategy, often called a policy, that increases cumulative reward over time.

In an information context, imagine a library search system that adapts how it ranks results. Each time a user submits a query, the system must decide how to order the results. If users click on top-ranked items, spend time reading them, or complete a task successfully, the system receives positive feedback. If users quickly reformulate their query or abandon the session, the feedback may be interpreted as weaker or negative.

Over time, the system may adjust its ranking strategy in order to increase successful interactions. The system is not simply predicting a fixed label. It is learning from interaction, where decisions and feedback are connected.

Some adaptive ranking or search optimization systems can be framed as reinforcement learning problems, particularly when decisions are sequential and feedback accumulates over time. Not all ranking systems use reinforcement learning, but the framework is useful for understanding how systems learn from ongoing user behavior.

In institutional settings, reinforcement learning raises important governance questions. The definition of reward becomes central. If reward is defined only in terms of clicks or dwell time, the system may prioritize engagement rather than relevance, diversity, or informational quality. Aligning reward structures with institutional values is therefore essential. In this context, institutional values refer to an organization's mission and professional commitments, such as promoting equitable access, supporting learning, protecting user privacy, and ensuring that systems prioritize informational quality rather than engagement alone.

!!! example "Hands on: Choosing the appropriate learning paradigm"

    **Goal:** Practice identifying which learning paradigm best fits an information task.

    For each scenario below:

    1. Decide whether supervised learning, unsupervised learning, or reinforcement learning is most appropriate.
    2. Briefly explain your reasoning in terms of the type of feedback signal available.
    3. Identify one practical limitation or governance concern.

    Scenario A:
    A university library has ten years of digitized theses. Each thesis has already been assigned a disciplinary category. The library wants to automate category assignment for new submissions.

    Scenario B:
    A public library has collected thousands of open-ended patron feedback comments. The library does not have predefined categories and wants to explore recurring themes.

    Scenario C:
    An academic search system wants to dynamically adjust the ranking of search results based on how users interact with results over time.

    Scenario D:
    A digital archive wants to identify groups of photographs that share visual similarity, but no metadata are available.

    Scenario E:
    A campus IT help desk wants to predict the expected resolution time for incoming tickets, based on historical records that include past resolution times.

    As you respond, focus on:

    - Does the task include known labels or outcomes in the training data?
    - Is the system trying to discover structure without predefined categories?
    - Does the system learn from ongoing interaction and feedback over time?
    - Who defines the target, cluster meaning, or reward signal in this scenario?

## Neural networks

Neural networks are a class of machine learning models capable of learning complex patterns from data through layered transformations. Instead of relying on explicitly defined rules, a neural network adjusts many parameters during training in order to reduce a defined loss function. These parameters, often called weights and bias terms, determine how inputs are transformed as they move through the network.

A neural network consists of multiple layers of computational units. Each layer transforms its input into a new representation. As data pass through successive layers, the model can learn increasingly abstract patterns.

Returning to the “History” book example, a simple supervised model might rely on a small set of word counts. A neural network, by contrast, assigns parameters across many words simultaneously. Instead of depending on a single word such as “war,” it may learn that combinations of words like “empire,” “revolution,” “treaty,” and time expressions together signal that a book belongs to the History category. These patterns are not manually specified. They are learned from data through optimization.

Neural networks are particularly useful when:

- The input data contain many variables or features, such as text with thousands of possible words, images made up of many pixels, or audio signals sampled over time.
- Relevant patterns are complex and not easily captured by simple rules.
- Large amounts of training data are available.

When neural networks contain many layers, they are often referred to as deep neural networks, and training such models is commonly called deep learning. In other words, deep learning refers to the practice of training multi-layer neural networks. Large language models are a specific type of deep neural network trained on very large text corpora to learn patterns in language.

In information science contexts, neural networks are widely used for tasks such as:

- Text classification and information extraction.
- Image recognition in digitized collections.
- Semantic search and recommendation systems.

However, neural networks introduce interpretability challenges. The learned parameters are distributed across many layers, and it is often difficult to explain in simple human-readable terms why a particular prediction was made. This opacity is commonly described as the “black box” problem.

A neural network may achieve low loss and strong predictive performance, yet still be difficult to justify or audit. For institutions that require transparency, accountability, and alignment with policy, this creates tension between performance and interpretability.

!!! example "Hands on: Experiment with TensorFlow Playground"

	**Goal:** Visualize how a neural network works.
	
	Visit: [A Neural Network Playground](https://playground.tensorflow.org/)
	
	(Optional reference reading: [Understanding neural networks with TensorFlow Playground](
	https://cloud.google.com/blog/products/ai-machine-learning/understanding-neural-networks-with-tensorflow-playground))
	
	Make sure:

	- Problem type = **Classification**
	- Noise = 0
	- Training/Test split = 50%
	
	**Step 1: Start with a minimal model**
	
	Choose the XOR-style dataset (the one with four colored quadrants).
	
	Set:

	- Hidden layers: 1  
	- Neurons: 1  
	- Activation: Tanh  
	- Learning rate: 0.03  
	
	Click **Play**.
	
	Observe:

	- Does the model successfully separate the blue and orange points?
	- What does the decision boundary look like?
	- What is the final training loss?
	
	**Step 2: Increase model capacity**
	
	Change the network to:

	- Hidden layers: 1  
	- Neurons: 4  
	
	Train again.
	
	Observe:

	- Does the loss decrease more effectively?
	- How does the decision boundary change?
	- What do the hidden neuron visualizations show?
	
	**Step 3: Add depth**
	
	Try:

	- 2 or 3 hidden layers  
	- Keep 4 neurons in the first layer  
	
	Train again.
	
	Observe:

	- Does the model learn faster?
	- Does the boundary become smoother or more complex?
	- What changes when you increase depth instead of width?
	
	**Step 4: Introduce noise**
	
	Increase **Noise** to 30 or 50. Noise means some data points are randomly distorted or mislabeled, making the pattern less clean and harder to learn.
	
	Train again.
	
	Observe:

	- Does the loss still reach zero?
	- Does the boundary look less clean?
	- Does performance differ between training and test data?
	
	**Step 5: Adjust learning rate**
	
	Lower the learning rate to 0.001. Learning rate determines how quickly the model adjusts its parameters during training.
	
	Train again.
	
	Observe:

	- Does learning slow down?
	- How does the loss curve behave differently?
	
	As you experiment, consider the following:
	
	1. What counts as the training data in this setup? Make sure “Show test data” is checked so you can see both training and test points.
	2. What are the input features?
	3. What is the output of the model?
	4. Why can’t a single neuron solve the XOR dataset?
	5. What changes when you add more neurons or layers?
	6. What happens when noise increases?
	7. Can you create a case where the model performs well on training data but not on test data?
	
	Notice that you did not manually define any rules.  
	The system adjusts model parameters automatically to reduce the loss.


## Neuro-symbolic AI

Neuro-symbolic AI refers to approaches that combine neural networks with symbolic representations or rule-based reasoning. The goal is not to replace one paradigm with the other, but to integrate their strengths.

Neural models are effective at learning patterns from large and complex data, especially unstructured text or images. Symbolic systems, by contrast, represent knowledge explicitly and support structured reasoning using defined concepts, relationships, and constraints.

Consider an information organization scenario in which a system extracts entities and relationships from historical documents. A neural model might identify names, dates, locations, and possible relationships based on language patterns. For example, it might detect that a particular person “served as mayor of a city in 1890.”

However, the neural model does not inherently know whether this information is consistent with an existing knowledge structure. A symbolic system, such as a knowledge graph with defined classes and relations, can represent constraints such as:

- A person can hold a political office only within a valid time range.
- A city must exist as an entity in the institutional knowledge base.
- An office term cannot overlap with another incompatible office held by the same individual.

A neuro-symbolic system could use the neural network to extract candidate statements from text, and then use symbolic reasoning to check consistency, enforce constraints, or infer additional relationships.

Neuro-symbolic approaches are particularly relevant when learned pattern recognition must operate together with explicit rules or safety constraints.

For example, in autonomous driving, a neural network may be used to detect pedestrians, traffic signs, or lane markings from camera images. However, traffic laws and safety constraints cannot be left to statistical pattern recognition alone. A symbolic component can encode rules such as speed limits, right-of-way regulations, or the requirement to stop at red lights. The system must both perceive the environment and reason about structured rules.

Similar situations arise in information systems. A neural model might extract entities or suggest classifications from text, but symbolic rules or ontologies may enforce constraints such as:

- A publication date cannot occur after an author’s death.
- A resource assigned to a restricted category must not be publicly searchable.
- A metadata field must conform to a controlled vocabulary.

Neuro-symbolic systems are therefore useful when statistical learning must be combined with formal constraints, institutional policy, or structured domain knowledge.

Neuro-symbolic AI is an active research area. There is no single standard architecture. Rather, it refers to a range of strategies for integrating statistical learning with structured knowledge representation.

## Clarification on common terms

**1. Do all machine learning models require separate training and test datasets?**

Not all machine learning procedures require a separate test dataset in order to run. A model can be trained using a single dataset.

However, if we want to assess whether the model has learned patterns that extend beyond the data it was trained on, we need independent data for evaluation. Without separate evaluation data, it is difficult to determine whether the model has generalized or memorized the training examples. This is why training and test splits are common in practice, especially when predictive performance is important.

In some cases, alternative strategies such as cross-validation are used instead of a fixed split, but the underlying idea remains the same: evaluation should be performed on data that were not used for parameter adjustment.

**2. What is the difference between parameters and hyperparameters?**

Parameters are the internal values of a machine learning model that are learned from data during training. These values are adjusted automatically by the optimization process in order to reduce the loss function.

Hyperparameters, by contrast, are settings chosen before training begins. They control aspects of the model or the training process itself. Examples include the learning rate, the number of training iterations, or the number of clusters in a clustering algorithm.

In short:

- Parameters are learned from data.
- Hyperparameters are set by the researcher or practitioner before training.

**3. What is the difference between underfitting and overfitting?**

Underfitting and overfitting describe two different ways a machine learning model can fail to learn useful patterns.

*Underfitting* occurs when a model is too simple to capture meaningful structure in the data. In this case, the model performs poorly even on the training data. The loss remains relatively high because the model cannot represent the underlying patterns well enough.

For example, imagine our document classification model for identifying “History” texts only considers whether the word “war” appears. Many historical documents may not contain that word, and many non-historical documents might mention it. Because the model relies on too little information, it fails to capture the broader patterns that define the category. As a result, it misclassifies many documents, including those in the training data.

*Overfitting*, by contrast, occurs when a model fits the training data too closely. It may perform very well on the training data, showing low loss during training, but perform poorly on new data.

In the same example, suppose the model assigns very specific parameter values to rare word combinations that appear only in the training documents. It may learn that a particular phrase found in one historical document strongly signals the “History” category. However, this phrase does not appear in future documents. The model has captured details specific to the training set rather than general characteristics of historical writing. As a result, it performs poorly on new documents.

A useful way to compare them:

- Underfitting: the model is too weak to capture real structure.
- Overfitting: the model captures too much detail, including noise.

The immediate goal of training is to reduce loss on training data, but the broader goal is to achieve good performance on new data.

**Further information**

- [How the machine 'thinks': Understanding opacity in machine learning algorithms](https://doi.org/10.1177/2053951715622512)
- [GeeksforGeeks: Machine Learning Tutorial](https://www.geeksforgeeks.org/machine-learning/machine-learning/)
- [Difference Between Model Parameters VS HyperParameters](https://www.geeksforgeeks.org/machine-learning/difference-between-model-parameters-vs-hyperparameters/)
- [AI & Machine Learning in Libraries](https://libereurope.github.io/ds-topic-guides/ai-ml.html)
- [Imagining library futures using AI and machine learning](https://hangingtogether.org/imagining-library-futures-using-ai-and-machine-learning/)
- [Underfitting and Overfitting in ML](https://www.geeksforgeeks.org/machine-learning/underfitting-and-overfitting-in-machine-learning/)
- 3Blue1Brown: But what is a neural network?
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
    <iframe
        src="https://www.youtube-nocookie.com/embed/aircAruvnKk"
        title="But what is a neural network?"
        style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe>
    </div>    
- [Google Machine Learning Education](https://developers.google.com/machine-learning):
    
    - [What is Machine Learning?](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml)
    - [Supervised Learning](https://developers.google.com/machine-learning/intro-to-ml/supervised)
    - [Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks)

- [Neuro-symbolic approaches in artificial intelligence](https://doi.org/10.1093/nsr/nwac035)

