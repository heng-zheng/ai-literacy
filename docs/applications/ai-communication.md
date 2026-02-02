# AI, Communication, and Information Exposure

## How AI Shapes Information Exposure

Online communication is mediated by systems that rank, recommend, and remove content at scale. AI shapes what becomes visible and what remains unseen by determining which items appear first, which are shown repeatedly, and which are shown less often or not at all.

These decisions are based on signals such as past interactions, popularity, and relevance as defined by the platform. Over time, this influences what feels familiar, important, or worth attention, even when users do not actively choose to avoid other information.

As a result, AI mediated visibility can affect how people form their opinions, what they treat as common knowledge, and what they trust.

A practical way to analyze this is to follow the pathway from content to attention. Ask what signals the system uses, what it rewards, and what it pushes out of view. In practice, this means starting from what appears first on a feed or results page and asking why it is there, what user actions seem to be encouraged, and what kinds of content rarely appear.

!!! example "Hands on: When past views shape what you see next"
    **Goal:** Observe how recent activity can influence what is shown by default.

    **Steps:**

    1. Open Amazon in a regular browser.
       You may stay logged in or use a private window.

    2. Search for one common product.
       Examples include headphones, backpack, or water bottle.

    3. Click into two or three product pages and spend a short time viewing them.

    4. Close the page or return to the Amazon homepage.

    5. Look at the homepage recommendations.
       Note whether any products related to what you viewed appear.

    **Think about**

    1. What kinds of items are now easier to notice.
    2. Whether the homepage reflects your recent activity.
    3. How this might shape what feels relevant before you actively search again.


**Further information:**

- [Algorithmic people-pleasers: Are AI chatbots telling you what you want to hear?](https://www.article19.org/resources/algorithmic-people-pleasers-are-ai-chatbots-telling-you-what-you-want-to-hear/)

## Social Media Recommendation and Personalization

Recommendation systems personalize feeds by learning from behavior such as clicks, watch time, and interactions. Personalization can support discovery by helping users find relevant content, but it also shapes what is prioritized and repeated. This is why concepts such as filter bubbles and echo chambers are often used to describe their effects.

Over time, repeated patterns of visibility can narrow what users encounter. When systems consistently prioritize content aligned with prior behavior, certain topics, sources, or perspectives become easier to see, while others gradually fade from view. This process is often described as a **filter bubble**.

A filter bubble does not mean users are intentionally avoiding other viewpoints. It reflects how personalization and ranking shape information exposure by reinforcing existing patterns of interest and interaction.

These effects do not require a platform to target ideology directly. They can emerge from optimization goals that reward content likely to hold attention.

Many users notice this in everyday use. After clicking on or interacting with a particular topic, similar posts often appear more frequently in their feed. A single action can influence what the system learns to prioritize, making related content easier to encounter and less related content harder to find.

!!! example "Hands on: Tracing visibility in your own feed"
    **Goal:** Notice how small actions can change what appears first.

    **Steps:**

    1. Choose one or more social media platforms you use.
       Examples include YouTube, TikTok, Instagram, or X.
    2. On the first platform, scroll for about one minute and note the first five items you see.
    3. Search for a topic you do not usually interact with.
       Open two or three results.
       While viewing them, try one or two interactions such as liking, saving, or watching for a longer time.
    4. Return to the main feed and refresh or reopen the app.
    5. Scroll again and note the first five items you now see.
    6. If possible, repeat the same steps on a second platform and compare the results.

    **Think about**

    1. What changed between the two sets of items.
    2. Whether different types of interaction led to different changes.
    3. How quickly the feed responded on each platform.
    4. What signals the system may have used to adjust visibility.

**Further information:**

- [Generative Echo Chamber? Effect of LLM-Powered Search Systems on Diverse Information Seeking](https://doi.org/10.1145/3613904.3642459). You can also check the authors' presentation:
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/s2A0YVr4vP8"
    title="Generative Echo Chamber? Effect of LLM-Powered Search Systems on Diverse Information Seeking"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

## Automated Content Moderation

Platforms use automated moderation to handle scale. Systems can flag hate speech, harassment, graphic content, and misinformation patterns. They can also reduce distribution or route content to human review.

Moderation is difficult because many cases depend on context. Humor, sarcasm, reclaimed language, and health related discussion are hard to judge from text alone. Automated systems may perform well on average, but their errors often become most visible in high impact situations. During the COVID-19 pandemic, [Meta](https://thehill.com/policy/technology/5020242-meta-admits-content-moderation-errors/) acknowledged that expanded automated moderation sometimes limited legitimate discussion.

!!! example "Hands on: How platforms explain moderation"
    **Goal:** Understand how content moderation is defined and experienced on real platforms.

    **Steps:**

    1. Choose one or more platforms you are familiar with.
       Examples include Facebook, TikTok, or X.

    2. Visit the platform’s public moderation or safety page.
       You may use the links below or find a similar page on another platform.

         - [How Facebook uses artificial intelligence to moderate content](https://www.facebook.com/help/1584908458516247)  
         - [TikTok content moderation](https://www.tiktok.com/euonlinesafety/en/content-moderation/)  
         - [X safety and sensitive content policies](https://help.x.com/en/safety-and-security#sensitive-content)  

    3. Skim the page and note two or three types of content the platform says it moderates.
       Examples include hate speech, misinformation, graphic content, or harassment.

    4. Note how the platform describes its process.
       Look for references to automated systems, human review, or user reporting.

    5. Reflect on your own experience using the platform.
       Think about whether you have seen content labeled, removed, downranked, or hidden.

    **Think about**

    1. How clearly the platform explains what will be moderated.
    2. Whether the rules seem easy or difficult to apply in real situations.
    3. How moderation decisions might look different to users than to the system enforcing them.

**Further information**

- [Using AI to detect COVID-19 misinformation and exploitative content](https://ai.meta.com/blog/using-ai-to-detect-covid-19-misinformation-and-exploitative-content/), also see [IEEE's report](https://spectrum.ieee.org/how-facebook-is-using-ai-to-fight-covid19-misinformation)

## Misinformation and Disinformation Detection

Misinformation and disinformation are often discussed together, but they describe different dynamics. Drawing on [Claire Wardle’s definitions](https://issues.org/misunderstanding-misinformation-wardle/), misinformation refers to false or misleading information shared without the intent to cause harm, while disinformation involves the deliberate creation or distribution of such content for strategic purposes. Much misleading content is not entirely fabricated, but consists of genuine material shared out of context.

Detection tools typically focus on identifying patterns associated with problematic content, such as repeated claims, reuse across platforms, or unusual distribution behavior. These tools can help flag likely cases, but they often operate after content has already begun to circulate and gain attention.

In practice, intervention matters as much as detection. Labeling, downranking, removal, and account actions shape how information is encountered and interpreted, each carrying tradeoffs for transparency, trust, and public understanding. For example, YouTube may display information panels alongside videos on topics prone to misinformation, linking to independent third-party sources to provide additional context while leaving the video itself visible. Focusing only on whether a claim is true or false risks overlooking how information is framed and used in everyday contexts.

!!! example "Hands on: Seeing detection and intervention in practice"
    **Goal:** Observe how misinformation is identified and handled after it circulates.

    **Steps:**

    1. Choose one trending or widely shared claim you have seen online.
       This may relate to health, science, or everyday life.

    2. Look up the claim using a fact-checking tool, such as [Google Fact Check Tools](https://toolbox.google.com/factcheck/explorer)  

    3. Note how the claim is described.
       Pay attention to wording, sources, and the level of certainty.

    4. If possible, check how the claim appears on the original platform.
       Look for labels, notes, or reduced visibility.

    **Think about**

    1. Whether detection happened before or after the claim spread.
    2. What kind of intervention was used.
    3. How the approach balances correction, transparency, and trust.

**Further information**

- Social media and the age of AI misinformation | Aishwarya Reganti | TEDxJacksonville
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/lVkJsTY_n8Q"
    title="Social media and the age of AI misinformation | Aishwarya Reganti | TEDxJacksonville"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

## Deepfakes and Synthetic Media

Deepfakes and synthetic media can convincingly imitate real people. They are used in entertainment, accessibility, and creative production, but they also enable deception, harassment, and the rapid spread of misleading content. Detection remains challenging because generation tools improve quickly and even low quality synthetic media can circulate widely before being questioned.

Recent reporting has shown how AI generated images and videos can create confusion during fast moving news events, particularly when visual material spreads faster than verification. In these situations, synthetic media does not need to be highly realistic to be effective, as ambiguity alone can mislead audiences.

In response, platforms and regulators increasingly emphasize labeling and disclosure rather than relying solely on detection. These approaches aim to provide context to viewers while allowing content to remain visible, reflecting broader efforts to balance transparency, trust, and accountability.

!!! example "Hands on: Seeing synthetic media in everyday platforms"
    **Goal:** Recognize how synthetic media appears in common platforms and how labeling shapes interpretation.

    **Steps:**

    1. Open YouTube and search for a comparison video using a query such as “real vs AI generated” or “AI generated faces vs real”. Choose one video that compares real and AI generated images or videos.
       ([example video 1](https://youtu.be/oWLHAuUoYqQ?si=U1R0Ge06phboLEHx), [example video 2](https://www.youtube.com/watch?v=IkwWEEZXjPw))

    2. Watch a short segment and take notes.
       Focus on moments where it is difficult to tell whether the content is real or synthetic.

    3. Write down two observations.
       One feature that made the content seem realistic.
       One feature that raised doubt or uncertainty.

    4. Next, visit one platform’s policy page on AI generated content labeling.
       For example:  
       https://www.tiktok.com/tns-inapp/pages/ai-generated-content

    5. Think back to your own use of social media.
       Consider whether you have noticed labels such as “AI generated” or similar disclosures while browsing.

    **Think about**

    1. Whether current AI generated media is convincing enough to be mistaken for real content.
    2. How labels affect your trust or interpretation of the content.
    3. Whether you actively notice these labels during everyday browsing.

**Further information**

- AI news videos blur line between real and fake reports
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/SRA4brHXBBQ"
    title="AI news videos blur line between real and fake reports"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

- Is Sienna Rose AI-generated? New music artist divides listeners
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/qLIosCiA4jA"
    title="Is Sienna Rose AI-generated? New music artist divides listeners"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

- [Seeing is no longer believing: Artificial Intelligence’s impact on photojournalism](https://jsk.stanford.edu/news/seeing-no-longer-believing-artificial-intelligences-impact-photojournalism)

- [People are more susceptible to misinformation with realistic AI-synthesized images that provide strong evidence to headlines](https://doi.org/10.37016/mr-2020-189)

- [Deepfakes Aren't the Disinformation Threat They're Made Out to Be](https://www.rand.org/pubs/commentary/2023/12/deepfakes-arent-the-disinformation-threat-theyre-made.html)

## Generative AI in Scholarly Publishing

Generative AI is increasingly used in scholarly work for writing assistance, translation, summarization, and drafting support. These tools can reduce routine effort, but they also introduce risks, such as summaries that sound confident while omitting limitations, or citations that are incomplete or inaccurate.

In scholarly communication, accountability is important. AI can support writing and review-related tasks, but it does not replace the author’s responsibility for accuracy, attribution, and verification. Authors remain responsible for how AI tools are used and for the integrity of the final work.

AI is also being explored as a support tool in peer review. Some systems assist editors or reviewers by flagging issues such as possible text reuse. These tools are designed to supplement human judgment, not to function as independent peer reviewers.

!!! example "Hands on: Finding AI use policies in scholarly publishing"
    **Goal:** Understand how publishers and professional organizations define acceptable uses of AI in publishing.

    **Steps:**

    1. Choose one field you are familiar with.
       This may relate to libraries, information science, education, health, technology, or another area.

    2. Identify one publisher, journal, or professional organization in that field.
       Examples include an academic publisher, a major journal, or a professional association.

    3. Search for that organization’s policy on the use of AI in publishing.
       Look for guidance on writing assistance, authorship, disclosure, peer review, or editorial use.

    4. Read the policy and note three points.
       One activity that is clearly allowed.
       One activity that is restricted or discouraged.
       One area where the policy is vague or open to interpretation.

    **Think about**

    1. What assumptions the policy makes about how AI is used.
    2. Whether the policy focuses more on transparency, authorship, or research integrity.
    3. How this policy would affect your own use of AI in academic or professional writing.

**Further information**

- [GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers](https://gptzero.me/news/neurips/)
- [As Springer Nature journal clears AI papers, one university’s retractions rise drastically](https://retractionwatch.com/2025/02/10/as-springer-nature-journal-clears-ai-papers-one-universitys-retractions-rise-drastically/)
- [Researchers who are using generative AI to write scientific papers are publishing a significantly higher number of studies](https://cen.acs.org/policy/publishing/Researchers-use-generative-AI-write/103/web/2025/12)
- [More than half of researchers now use AI for peer review — often against guidance](https://doi.org/10.1038/d41586-025-04066-5)
- [AAAI Launches AI-Powered Peer Review Assessment System](https://aaai.org/aaai-launches-ai-powered-peer-review-assessment-system/)
- [How AI is transforming research: More papers, less quality, and a strained review system](https://newsroom.haas.berkeley.edu/how-ai-is-transforming-research-more-papers-less-quality-and-a-strained-review-system/)

## Negative Impacts and Risks

Communication systems shape how people feel, what they trust, and how they make decisions. Some risks are direct, such as emotional reliance on AI companions. Others are indirect, including repeated reassurance seeking that increases anxiety rather than reducing it.

AI and mental health is not a simple good or bad story. Recent reporting and research have raised concerns about young people using AI companions to meet emotional needs or simulate relationships, highlighting questions about dependency, boundaries, and long-term effects.

Another emerging concern is AI-mediated cyberchondria. When language models lower the cost of seeking information and reassurance, they can unintentionally reinforce anxiety-driven repeated querying instead of resolving uncertainty.

In online shopping, users have reported experiences where returning customers or frequent browsers are shown higher prices or fewer discounts than new users. This practice is often described as differential or personalized pricing. 

From a user perspective, the concern is not personalization itself but opacity. When people cannot tell whether prices, recommendations, or responses are shaped by their past behavior, trust in the system can erode, even when the underlying goal is revenue optimization rather than intentional deception.

As AI chatbots and conversational systems begin to incorporate advertising or sponsored content, these concerns extend to how commercial incentives may shape responses, visibility, and user trust.

**Further information**

- [1 in 5 high schoolers has had a romantic AI relationship or knows someone who has](https://www.npr.org/2025/10/08/nx-s1-5561981/ai-students-schools-teachers)
- [Why AI companions and young people can make for a dangerous mix](https://news.stanford.edu/stories/2025/08/ai-companions-chatbots-teens-young-people-risks-dangers-study)
- [Snap settles social media addiction lawsuit ahead of trial](https://www.bbc.com/news/articles/c62ndl2ydzxo)
- [Ads Are Coming to ChatGPT. Here’s How They’ll Work](https://www.wired.com/story/openai-testing-ads-us/)
- [How online retailers are using AI to adjust prices by mining your personal data](https://www.pbs.org/newshour/show/how-online-retailers-are-using-ai-to-adjust-prices-by-mining-your-personal-data)