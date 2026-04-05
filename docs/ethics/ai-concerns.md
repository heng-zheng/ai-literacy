# Concerns of AI

In previous sections, we introduced what AI systems are and how they work, along with basic ways of interacting with them in practice. This section shifts attention to their limitations and risks. As AI becomes more common in everyday contexts, it is necessary to examine not only what these systems can do, but also the constraints and tradeoffs they bring.

Some concerns are visible in the output itself, such as hallucinated facts or misleading summaries. Other concerns are less visible, such as privacy, copyright, data collection, or environmental cost.

AI literacy therefore requires critical evaluation. Users need to consider what data a system relies on, what risks may arise from its use, and what must be verified before trusting or reusing its output.

The concerns introduced here are not a complete list. They are examples of major issues that appear across many current AI systems. 

## Environmental cost

AI systems require physical infrastructure. They depend on data centers, computing hardware, electricity, cooling, and networked services. For this reason, AI is not only a digital software. It also has material and environmental costs.

These costs are not limited to building a model. Running AI systems at scale also consumes resources. A tool may feel quick and convenient to an individual user while still relying on large amounts of energy in the background.

At the same time, views on this issue are not one-sided. Some people are concerned that AI systems consume too much energy and place additional strain on existing infrastructure. Others argue that AI may help address energy challenges by improving efficiency, optimizing resource use, or supporting research in areas such as energy systems and climate modeling.

**Further information**

- Business Insider: 
Exposing The Dark Side of America's AI Data Center Explosion
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
    <iframe
        src="https://www.youtube-nocookie.com/embed/t-8TDOFqkQA"
        title="Exposing The Dark Side of America's AI Data Center Explosion | View From Above | Business Insider"
        style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe>
</div>

- Sims Witherspoon: Can AI Help Solve the Climate Crisis?
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
    <iframe
        src="https://www.youtube-nocookie.com/embed/RNhbqQefPSg"
        title="
Can AI Help Solve the Climate Crisis? | Sims Witherspoon | TED"
        style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe>
</div>

- [Pew Research: What we know about energy use at U.S. data centers amid the AI boom](https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/)


## Privacy and data security

Many AI systems collect and process user input, including prompts, uploaded files, and metadata. Users may not know what is stored, how long it is retained, or whether it is reviewed or used for model improvement.

Privacy therefore becomes a core concern in AI literacy. Ease of use does not imply appropriateness. Sensitive personal, academic, workplace, legal, or health-related data require caution.

Privacy is closely tied to security. A tool’s interface may appear trustworthy while its underlying processes remain unclear. In professional contexts, the key question is not only whether a task can be done, but whether the data should be entered into the system at all.

For information organizations, this issue is critical. Libraries, universities, and archives often handle confidential or protected records. A convenient AI tool is not always an appropriate one.

!!! example "Hands-on: Do you know AI is collecting your data?"
	
	Think about how you usually use tools like ChatGPT, Gemini, Claude, or Copilot.
	
	Consider:
	
	* What kinds of information have you entered into these tools?
	* When you type something, what do you think happens to that data?
	* Do you assume:
	
	  * it is stored?
	  * it is used to improve the system?
	  * it disappears after the session?
	
	Now think more concretely:
	
	* Have you ever entered anything that could be:
	
	  * personal
	  * student-related
	  * workplace or institutional
	  * sensitive or confidential
	
	**Reflection:**
	
	* Before this, did you actively think about where your data goes?
	* What assumptions were you making?
	* Do you feel comfortable with those assumptions now?

!!! example "Hands-on: How do AI tools actually handle your data?"

    **Goal:**  
    Understand how AI tools you actually use handle your data, and what control you have over that process.

    Choose one AI tool that you personally use or are likely to use. Go to its privacy, data, or settings page and explore how it handles user data (e.g., [ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq), [Gemini](https://support.google.com/gemini/answer/13594961), [Claude](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training), or others).  

    As you explore, focus on the following questions:

    - Can you turn off the use of your data for model training?
    - If you turn it off, does anything else change (e.g., chat history, features, integrations)?
    - Can you delete past conversations or activity?
    - Is any data still temporarily stored even after settings are turned off?

    After exploring your chosen tool, briefly reflect on:

    - How much control does this tool actually give you over your data?
    - Are the settings easy to find and understand?
    - Are there any tradeoffs (e.g., losing features vs. protecting privacy)?

    **Note:** These settings and policies can change over time. Always rely on the current official documentation rather than screenshots or summaries.

**Further information**

- [Your Personal Information Is Probably Being Used to Train Generative AI Models](https://www.scientificamerican.com/article/your-personal-information-is-probably-being-used-to-train-generative-ai-models/)

- [Be Careful What You Tell Your AI Chatbot](https://hai.stanford.edu/news/be-careful-what-you-tell-your-ai-chatbot)

- [University of Kentucky: What to know about AI safety and Microsoft Copilot at UK](https://its.uky.edu/news/what-know-about-ai-safety-and-microsoft-copilot-uk)

## Hallucinations and confabulations

Generative AI can produce fluent and convincing text even when it is wrong.

Some errors are easy to spot, such as invented sources or incorrect facts. Others are subtle, such as summaries that distort meaning or citations with small but critical mistakes. Outputs may also mix correct and incorrect information.

Fluency can mislead. Clear and confident language may be trusted too quickly, especially in academic or professional contexts.

Reliability is therefore a literacy issue. Users need to verify claims, check sources, compare outputs, and recognize uncertainty.

**Further information**

- [Anthropic: Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)
- [OpenAI: Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate/)
- [The Promethean Dilemma of AI at the Intersection of Hallucination and Creativity](https://cacm.acm.org/opinion/the-promethean-dilemma-of-ai-at-the-intersection-of-hallucination-and-creativity/)
- [New study warns of risks in AI chatbots giving medical advice](https://www.ox.ac.uk/news/2026-02-10-new-study-warns-risks-ai-chatbots-giving-medical-advice)

## Copyright, ownership, and training data

AI systems raise questions about copyright, licensing, and ownership, both for training data and for generated output.

Training data is often drawn from large collections of text, images, audio, or code. Users usually do not know what was included, whether permission was obtained, or how materials were licensed.


In academic publishing, this issue is already reflected in policy. Many publishers, such as [Springer](https://link.springer.com/brands/springer/journal-policies#Artificial%20intelligence%20(AI)), do not allow AI systems to be listed as authors. AI tools may be used in the research or writing process, but responsibility for the content must remain with human authors. Also see [COPE's position](https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools). 

**Further information**

- [Anthropic Wins on Fair Use for Training its LLMs; Loses on Building a “Central Library” of Pirated Books](https://www.authorsalliance.org/2025/06/24/anthropic-wins-on-fair-use-for-training-its-llms-loses-on-building-a-central-library-of-pirated-books/)
- [Authors Guild on AI](https://authorsguild.org/advocacy/artificial-intelligence/)

## Bias, fairness, transparency, and explainability

AI systems can reflect bias in the data they are trained on and in the ways they are designed or evaluated. As a result, a system may appear neutral while still producing uneven outcomes.

This matters for fairness, transparency, and explainability. If users are affected by a system without understanding how it works, trust and accountability become harder. In information organizations, this is especially relevant in areas such as search, ranking, recommendation, and decision support.

**Further information**

- [Transparency in AI is on the Decline](https://hai.stanford.edu/news/transparency-in-ai-is-on-the-decline)

- [Artificial intelligence algorithm bias in information retrieval systems and its implication for library and information science professionals: A scoping review](https://doi.org/10.1080/07317131.2025.2512282)

- [How We Analyzed the COMPAS Recidivism Algorithm](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm), also see the [dataset](https://www.kaggle.com/datasets/danofer/compass)

## AI and labor

AI can affect how work is done. It is often used to increase speed or reduce routine effort, but it can also reshape jobs in uneven ways.

One concern is deskilling. If workers rely heavily on AI for tasks such as writing, coding, searching, or analysis, they may practice these skills less often. Over time, this can reduce their ability to perform tasks independently or to evaluate AI output.

AI can also influence hiring, expectations, and workload. In some settings, workers may be expected to do more in less time because AI tools are available.

**Further information**

- [AI deskilling is a structural problem](https://doi.org/10.1007/s00146-025-02686-z)
- [The AI Deskilling Paradox](https://cacm.acm.org/news/the-ai-deskilling-paradox/)
- [AI's impacts on early career software engineers](https://spectrum.ieee.org/ai-effect-entry-level-jobs)
- [AI is Coming for Your Job. Now What? | Vlad Tenev | TED](https://www.youtube.com/watch?v=cJfKqKEyw1o)

- [Harvard Business School: Displacement or Complementarity? The Labor Market Impact of Generative AI](https://www.hbs.edu/faculty/Pages/download.aspx?name=25-039.pdf)
- [National Bureau of Economic Research: Artificial Intelligence and the Labor Market](http://doi.org/10.3386/w33509)
- [Anthropic: Labor market impacts of AI: A new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts)


## Other concerns

The concerns discussed above are not the only ones. AI systems can also raise other issues that deserve attention, especially when they are adopted broadly across education, workplaces, and public communication.

One concern is overreliance. Students or workers may begin using AI not only as a support tool, but as a default way of completing tasks, such as reading and writing. Excessive reliance on AI may lead to [psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis).

Another concern is unequal language support. Many AI systems perform much better in high-resource languages such as English than in low-resource languages. For example, translation quality may be noticeably weaker, or search results may be less reliable. This can limit access and reduce the usefulness of AI tools for some users. As a result, AI may expand access in some settings while reinforcing inequality in others.

**Further information**

- [Uncovering inequalities in new knowledge learning by large language models across different languages](https://doi.org/10.1073/pnas.2514626122)
- [Nearly all Seoul students use generative AI](https://www.koreaherald.com/article/10652914)
- [Mind the (Language) Gap: Mapping the Challenges of LLM Development in Low-Resource Language Contexts](https://hai.stanford.edu/policy/mind-the-language-gap-mapping-the-challenges-of-llm-development-in-low-resource-language-contexts)

- [Rise of Concerns About AI: Reflections and Directions](https://cacm.acm.org/opinion/rise-of-concerns-about-ai/)