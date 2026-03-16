# Communicating with AI

Generative AI systems are often used through natural language interaction. Users type instructions, questions, or requests, and the system produces a response based on the text it receives.

Learning how to communicate with AI is important for AI literacy. When people use generative AI, the wording of the prompt, the context provided, and the structure of the request can all affect the result.

This week focuses on how users communicate with AI, how prompts shape outputs, and why careful prompting does not remove the need for evaluation and verification.

## How LLMs interpret prompts

Large language models respond to text based on patterns learned from training data. They do not understand instructions in the same way humans do. Instead, they generate responses by predicting what text is likely to come next based on the input they receive.

For this reason, prompts matter. A prompt is not just a question. It also provides instructions, context, constraints, and expectations about what kind of response should be generated.

Small changes in wording can lead to different outputs. For example, a prompt that asks for a short summary may produce a very different answer from a prompt that asks for a summary in bullet points for a specific audience.

Compare the following examples.

```
Explain what metadata is.
```

```
Explain what metadata is in three bullet points for undergraduate students.
```

The second prompt gives the model more guidance. It specifies the task, the format, and the audience.

This does not mean that longer prompts are always better. It means that clearer prompts often give the model a better basis for producing a useful answer.

!!! example "Hands-on: Comparing simple prompts"

    **Goal:** Observe how changing the wording of a prompt changes the response.

    **Step 1: Open a large language model**

    Open any large language model you have access to, such as ChatGPT, Claude, Gemini, or Copilot.

    **Step 2: Paste a short paragraph**

    Use any short paragraph from a reading, article, or course material.

    **Step 3: Try two prompts**

    First, enter:

    ```
    Summarize this text.
    ```

    Then enter:

    ```
    Summarize this text in three bullet points for graduate students in LIS.
    ```

    **Step 4: Compare the results**

    Consider the following questions:

    - Which response was more useful
    - How did the second prompt shape the answer
    - What did the model do differently when the audience and format were specified

## Components of an effective prompt

Although prompts can take many forms, many effective prompts include several common components.

### Task

The task tells the model what you want it to do.

Examples include:

* summarize a document
* explain a concept
* generate keywords
* compare two ideas
* draft a short paragraph

For example:

```
Explain what metadata is.
```

### Role

Some prompts ask the model to respond from a particular perspective or for a particular purpose.

For example:

```
You are a librarian helping a patron understand generative AI.
```

This does not mean the model actually becomes a librarian. It means the prompt is guiding the style, level, and perspective of the response.

### Context

Context provides background information that helps the model understand the situation in which a task occurs.

Without context, the model may give a general answer that is not well suited to the specific situation. When context is provided, the model has more information about the problem, the setting, and the intended audience.

Compare the following examples.

**Prompt without context**

```
Explain whether AI-generated summaries are reliable.

```

**Prompt with context**

```
A public library patron is asking whether they should trust an AI-generated summary of a health article. Explain whether AI-generated summaries are reliable and what the patron should be careful about.
```

The first prompt may produce a broad explanation about AI reliability.  
The second prompt gives the model a clearer situation and audience, which may lead to a more practical and relevant response.

In many real-world situations, providing context helps the model produce answers that better match the user's needs.


### Output format

The output format tells the model how to present its answer.

Examples include:

* a paragraph
* bullet points
* a table
* a list of steps
* JSON or other structured forms

For example:

```
Explain what metadata is in four bullet points.
```

Together, these components often make prompts more precise and easier to interpret.

!!! example "Hands-on: Building a prompt step by step"


	**Goal:** Observe how adding task, role, context, and output format changes the response.
	
	**Step 1: Start with a very simple prompt**
	
	```
	Explain AI hallucination.
	```
	
	**Step 2: Add a role**
	
	```
	You are a librarian. Explain AI hallucination.
	```
	
	**Step 3: Add context**
	
	```
	You are a librarian helping a patron who is confused about whether ChatGPT always gives correct answers. Explain AI hallucination.
	```
	
	**Step 4: Add an output format**
	
	```
	You are a librarian helping a patron who is confused about whether ChatGPT always gives correct answers. Explain AI hallucination in three short bullet points.
	```
	
	**Step 5: Compare the responses**
	
	Consider the following questions:
	
	- Which version was clearest
	- Which version seemed most appropriate for the situation
	- Which added component changed the answer the most

## Common prompting strategies

Users often develop prompting strategies to guide model behavior more effectively. These strategies do not guarantee correctness, but they can help shape the response.

### Role prompting

[Role prompting](https://www.geeksforgeeks.org/artificial-intelligence/role-based-prompting/) asks the model to respond from a particular role or perspective.

For example:

```
You are an academic librarian helping a student begin a literature review.
```

This can help the model produce a response with a more relevant tone and focus.

### Step-by-step prompting

For more complex tasks, users sometimes ask the model to work through a problem step by step.

This is related to what researchers call [chain-of-thought prompting](https://www.promptingguide.ai/techniques/cot), or CoT. In practice, it means asking the model to break its response into intermediate steps rather than giving only a short final answer.

For example:

```
Explain step by step how a student should verify whether a cited article is real.
```

This can sometimes produce a more organized response. However, a step-by-step answer is not automatically correct.


### Example-based prompting

A model can also be guided by examples. This is sometimes called few-shot prompting.

In few-shot prompting, the user gives the model one or more examples of the kind of response they want. The model then uses that pattern to continue.

For example:

```
Question: What is metadata?
Answer: Metadata is information that describes other data.

Question: What is a controlled vocabulary?
Answer:
```

Here the prompt provides a pattern that the model is likely to continue.

A related approach is zero-shot prompting. In zero-shot prompting, the user does not provide examples. Instead, they simply ask the model to perform the task directly.

For example:

```
What is a controlled vocabulary?
```

Zero-shot prompting is often enough for simple tasks. Few-shot prompting can be useful when the user wants the model to follow a particular pattern, style, or type of answer more closely.

!!! example "Hands-on: Comparing zero-shot and few-shot prompting"

    **Goal:** Observe how examples can shape the response.

    **Step 1: Open a large language model**

    Open any large language model you have access to, such as ChatGPT, Claude, Gemini, or Copilot.

    **Step 2: Try a zero-shot prompt**

    Enter:

    ```
    What is a controlled vocabulary?
    ```

    **Step 3: Try a few-shot prompt**

    Then enter:

    ```
    Question: What is metadata?
    Answer: Metadata is information that describes other data.

    Question: What is a controlled vocabulary?
    Answer:
    ```

    **Step 4: Compare the results**

    Consider the following questions:

    - Did the two responses differ in length, tone, or structure
    - Did the example in the few-shot prompt influence the wording of the answer
    - Which version seemed more useful for learning
    - In what kinds of situations might examples help guide the model

### Structured output prompting

Sometimes users want information in a specific structure.

For example:

```
List three benefits and three risks of generative AI in a table.
```

This can be useful in research, information organization, and data-related tasks.

!!! example "Hands-on: Trying different prompting strategies"

	**Goal:** Compare how different prompting strategies shape the response.
	
	Choose one question, such as:
	
	```
	What are the risks of using generative AI in academic writing?
	```
	
	Then ask the same question using the following different prompts.
	
	**Version 1: Basic prompt**
	
	```
	What are the risks of using generative AI in academic writing?
	```
	
	**Version 2: Role prompt**
	
	```
	You are a university instructor. What are the risks of using generative AI in academic writing?
	```
	
	**Version 3: Step-by-step prompt**
	
	```
	Explain step by step what the main risks of using generative AI in academic writing are.
	```
	
	**Version 4: Structured output prompt**
	
	```
	List the main risks of using generative AI in academic writing in a table with two columns: risk and explanation.
	```
	
	After comparing the outputs, consider:
	
	- Which response was easiest to understand
	- Which response was most useful
	- Did different strategies change the substance of the answer, or mainly its structure and tone

## Iterative prompting

In practice, people often do not get the result they want from the first prompt. Prompting is usually an iterative process.

A user may start with a broad request, examine the result, notice problems, and then revise the prompt.

This process often involves:

1. writing an initial prompt
2. reviewing the output
3. identifying what is missing or unclear
4. revising the prompt
5. generating a new answer

For example, consider the following progression.

```
Write about AI.
```

```
Write a short explanation of generative AI.
```

```
Write a 150-word explanation of generative AI for first-year LIS graduate students.
```

Each revision narrows the task and gives the model more guidance.

Iterative prompting can improve usefulness, but it also requires judgment. The user must decide what the response is missing and how the prompt should change.

!!! example "Hands-on: Revising a weak prompt"

	**Goal:** Practice improving a prompt through revision.
	
	**Step 1: Begin with a weak prompt**
	
	```
	Write about prompt engineering.
	```
	
	**Step 2: Read the response**
	
	Notice what is vague, too broad, or not useful.
	
	**Step 3: Revise the prompt**
	
	Try a more specific version such as:
	
	```
	Write a 200-word explanation of prompt engineering for LIS graduate students. Focus on why prompt wording affects the quality of LLM responses.
	```
	
	**Step 4: Revise again**
	
	Try a third version such as:
	
	```
	Write a 200-word explanation of how prompt wording affects LLM responses for LIS graduate students. Include one example and end with two practical tips.
	```
	
	**Step 5: Reflect**
	
	Consider the following questions:
	
	- What problems did the first prompt create
	- Which revision improved the answer the most
	- What does this exercise suggest about how users should interact with AI systems

## Prompting helps, but verification is still necessary

Prompting can shape outputs, but it does not remove the limits of large language models.

A better prompt may improve clarity, structure, or relevance. However, even a carefully written prompt cannot fully prevent problems such as:

* hallucinated information
* fabricated citations
* outdated knowledge
* weak reasoning
* overconfident answers

For example, a user may write:

```
Only provide real peer-reviewed sources published after 2020.
```

This instruction may help, but it does not guarantee that every source returned by the model is real or correctly cited.

For this reason, better prompting can improve an answer, but it cannot make the model fully reliable. In research, teaching, and professional settings, users still need to verify important claims and references.

!!! example "Hands-on: Checking whether AI-provided links point to the right source"

    **Goal:** Practice verifying whether AI-provided academic links or DOIs actually point to the correct sources.

    **Step 1: Ask for academic articles**

    Enter a prompt such as:

    ```
    Identify three peer-reviewed academic articles about AI applications in libraries. For each one, provide the article title, author(s), journal name, publication year, and a direct link or DOI.
    ```

    **Step 2: Review the response**

    Ask yourself:

    - Do the article titles look plausible for an academic publication
    - Do the journal names look credible
    - Do the links or DOIs look like they belong to the claimed article

    **Step 3: Check the links or DOIs**

    Use Google Scholar, library databases, or the links/DOIs provided to check:

    - Does the link or DOI lead to the article the model described
    - Does the bibliographic information (such as the title, author names, journal name, and publication year) match what the model gave you

    **Step 4: Reflect**

    Consider the following questions:

    - Did the links or DOIs point to the correct articles
    - Were any titles, authors, journals, or years inaccurate
    - Did the AI provide correct bibliographic information
    - What does this suggest about the need to check AI-provided sources before using them


## Practice: Applying Prompting Strategies

The following hands-on activity uses one shared scenario: preparing a short AI literacy article about **AI hallucination** for **first-year university students**. In this activity, you will experiment with multiple prompt versions, apply different prompting strategies, evaluate the responses, and work toward a small final artifact.

The goal is not to find one perfect prompt immediately. Instead, the goal is to observe how prompt design shapes explanation, structure, usefulness, and reliability.

!!! example "Hands-on: Creating a short AI literacy article about AI hallucination"

    **Goal:** Use multiple prompting strategies to develop a short article that explains AI hallucination to first-year university students.

    **Scenario**

    Imagine that you are preparing a short AI literacy article for **first-year university students** who are beginning to use generative AI tools in their academic work. Your goal is to create a short, clear, and usable explanation of **AI hallucination** that helps them understand the concept and why it matters.

    Your final artifact for this activity will be a **short article** of about **200–250 words**.

    **Step 1: Start with a baseline prompt**

    Begin with a very simple prompt so you can see what the model does without much guidance.

    For example:

    ```
    Explain AI hallucination.
    ```

    Read the response and note what seems too broad, too technical, too vague, or not well suited to first-year students.

    **Step 2: Add audience and purpose**

    You can then revise the prompt by specifying who the explanation is for.

    For example:

    ```
    Explain AI hallucination for first-year university students.
    ```

    Compare this version with the first one.

    Ask yourself:

    - Did the tone or vocabulary change
    - Was the explanation easier to understand
    - Did the response seem more appropriate for beginning students

    **Step 3: Add constraints and content requirements**

    You can make the prompt more useful by adding constraints about length and what the response should include.

    For example:

    ```
    Explain AI hallucination for first-year university students in about 150 words and include one simple example.
    ```

    You may also try a more structured version, such as:

    ```
    Define AI hallucination in plain language for first-year university students, then provide one simple example.
    ```

    Compare the responses and consider:

    - Which version was clearer
    - Whether the example improved understanding
    - Whether the added constraints made the response more useful

    **Step 4: Try different prompting strategies**

    Next, experiment with strategies introduced earlier in this section.

    You can try a **role prompt**, such as:

    ```
    You are a university instructor introducing generative AI concepts to first-year university students. Explain AI hallucination.
    ```

    You can try a **structured output prompt**, such as:

    ```
    Explain AI hallucination using one short paragraph followed by three bullet points.
    ```

    You can try a **step-by-step prompt**, such as:

    ```
    Explain step by step what AI hallucination is and why it matters for students using generative AI tools.
    ```

    Compare these responses and consider:

    - Which strategy produced the clearest explanation
    - Which strategy produced the most useful structure
    - Did the strategies mainly change the format, or also the substance of the explanation

    **Step 5: Check the reliability of the content**

    Even if one version seems strong, do not assume it is fully reliable. Review the explanation and identify claims, examples, or wording that you would want to verify. You can also ask the model for sources, such as:

    ```
    Suggest three academic or credible sources that explain AI hallucination.
    ```

    Then verify all three sources using a library database, Google Scholar, or another credible source.

    Consider:

    - Were the suggested sources real and relevant
    - Did the sources actually support the explanation the model gave
    - Were the sources the kinds of sources you wanted for this task
    - Were the sources current enough for your purpose
    - Might there be useful sources that a generative AI system cannot easily access or retrieve
    - What still required human checking

    **Step 6: Generate a short final article**

    After experimenting with multiple prompt versions, write one improved prompt that asks the model to generate a short final article.

    Your prompt should ask for a short article of about **200–250 words** for **first-year university students**.

    You can ask the model to include:

    - a short title
    - a clear explanation of AI hallucination
    - one simple example
    - one sentence explaining why students should verify AI-generated information
    - two citations to credible sources

    For example:

    ```
    Write a short article of about 200–250 words for first-year university students explaining AI hallucination.
    Include a short title, a clear explanation, one simple example, one sentence explaining why students should verify AI-generated information, and two citations to credible sources.
    ```

    **Step 7: Reflect on the process**

    After generating the final version, reflect on the following questions:

    - Which prompt changes improved the article the most
    - Which prompting strategy was most useful for this task
    - Where was human judgment still necessary
    - Would you use the final article without revision, or would you still change something before sharing it


## Further information

- [Google: Prompt engineering: overview and guide](https://cloud.google.com/discover/what-is-prompt-engineering)
- [Wharton Generative AI Labs Prompt Library](https://www.notion.so/1b3dc3333315802a9e99cafedb321048?pvs=21)
- [Prompt Engineering Guide](https://www.promptingguide.ai/). See the [introduction](https://www.promptingguide.ai/introduction) part and the [Prompting Techniques](https://www.promptingguide.ai/techniques) part. 
- [GeeksforGeeks: Prompt Engineering Best Practices for AI Models](https://www.geeksforgeeks.org/blogs/prompt-engineering-best-practices/)
- You can try [Microsoft Copilot's Prompt Coach](https://marketplace.microsoft.com/en-us/product/office/WA200007578?tab=Overview) to improve your prompts