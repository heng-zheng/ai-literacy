(Under Construction)

# AI for Information Organization and Systems

## AI in Digital Archives and Preservation 

In large digitization programs, a major challenge is **scale**. When archives convert millions of pages and images into digital form, staff rarely have the capacity to create detailed item-level records from scratch. In practice, AI is used to make collections **searchable earlier** and to help professionals prioritize where their limited time and expertise are most needed.


Building on OCR and basic text understanding introduced in the previous week, AI is used in digital archives primarily to address **scale**, not to produce complete or authoritative descriptions. Once text becomes machine-readable, AI systems can suggest draft descriptive elements and group large volumes of material into broad categories that support early access.

At this stage, AI outputs should be understood as **provisional structure**. Suggested titles, dates, names, or topical labels reflect patterns learned from existing data rather than interpretive understanding. Their value lies in making large collections searchable and navigable sooner, not in replacing professional description.

In this context, **triage** refers to how AI reshapes attention rather than how archives operate. Instead of aiming for completeness upfront, AI helps surface basic organization across a collection and highlights where human expertise is most needed. Professional judgment remains essential for evaluation, correction, and decisions that carry interpretive or institutional responsibility.

This framing is reflected in the way the **National Archives and Records Administration** documents its AI use through a [public inventory of AI use cases](https://www.archives.gov/ai). Rather than presenting AI as a single system or solution, NARA describes a range of narrowly scoped applications that support access, discovery, privacy protection, and internal knowledge work.

Across these examples, AI is consistently positioned as an assistive layer. Systems are used to generate draft descriptive metadata, flag potentially sensitive information, support search and retrieval, or help staff navigate large internal knowledge bases. These applications aim to reduce routine effort, manage scale, and improve responsiveness, especially in areas such as catalog access, FOIA processing, and privacy review.

Importantly, NARA does not frame AI outputs as authoritative archival decisions. Many projects are explicitly labeled as pilots, with quality evaluation and human review built into the workflow. Responsibility for interpretation, validation, and final description remains with professionals, reinforcing the idea that AI supports archival access without replacing institutional judgment or accountability.

!!! example "Hands on: From Raw Document to a Searchable Object"
    **Goal:** Observe how automated extraction can support access at scale while still requiring human judgment.
    **Steps:**
    1. Open a scanned PDF or an image based document provided by the instructor.  
    2. Use one tool that can extract text or descriptions, such as Google Drive OCR, Adobe Scan, or an LLM with image input.  
    3. Identify five elements that could function as metadata. Examples include title, date, creator, place, and subject keywords.  
    4. Copy your five fields into a short note, one line per field.

    **Discuss:**
    1. Which fields look plausible but may still be unreliable, and why  
    2. Which decisions would you not delegate to an automated tool without expert review  
    3. What additional context you would need to confirm the correctness of your draft metadata

    **Key takeaway:**
    Automated extraction can create usable structure quickly and at scale, but accuracy, context, and accountability still depend on professional review and decision making.

[1]: https://www.archives.gov/ai?utm_source=chatgpt.com "Inventory of NARA Artificial Intelligence (AI) Use Cases"

## Cataloging and Classification Automation

Automated cataloging tools support description by suggesting metadata based on patterns in existing records. They can propose subject terms, classification candidates, and other descriptive fields by comparing a resource to similar items that have already been cataloged. This can reduce routine effort and speed up early record creation, especially when processing large volumes of materials.

These suggestions are not the same as authoritative cataloging. The system does not interpret context, resolve ambiguity, or apply local standards on its own. Outputs can reflect the conventions and limits of the records the system learned from, so results require review and correction.

Classification remains a professional and institutional responsibility. Staff decide what to accept, what to revise, and what to reject, based on local policy and cataloging practice. This includes decisions about controlled vocabularies, local consistency, and how description serves community and institutional priorities.

Example: [OCLC cataloging with AI](https://www.oclc.org/en/connexion.html#catalog-with-ai). Watch the [presentation in the final session](https://www.oclc.org/go/en/events/cataloging-community-meeting/june-2025.html#final-session) (starting from 3:48 to 10:10) and review the [slides](https://www.oclc.org/content/dam/oclc/cataloging-subscription/cataloging-events/OCCM-2025-06-final-session.pdf#page=7.00).

!!! example "Hands-on: Assisted Description with a Fixed Prompt"

    **Goal**  
    Experience AI as a drafting assistant for description, not as an authority.

    **Instructions**

    1. Choose one generative AI tool you have access to  
       Examples include ChatGPT, Gemini, or Claude.

    2. Copy and paste the following prompt into the tool.

    **Prompt**

    You are assisting with preliminary cataloging work.  
    Based only on the text provided below, do the following.

    1. Write one clear, neutral sentence describing the item.  
    2. Suggest up to five subject terms that reflect the main topics.  
    3. Do not invent information that is not supported by the text.

    **Text A**

    This report examines how small public libraries in rural areas have adopted digital services over the past decade. It discusses challenges related to funding, staffing, and broadband access, as well as strategies used to expand community engagement through online programs, digital collections, and remote reference services. The report is based on survey responses from library directors and includes several short case examples.

    **Text B**

    This handbook introduces basic data management practices for non-technical staff working in cultural institutions. Topics include file naming, storage, backups, and documentation. The handbook is intended as a practical guide for daily work and does not address advanced data analysis or programming.

    **Student review task**

    For each text:
    - Mark each suggested subject term as **Keep**, **Revise**, or **Reject**.  
    - For any term marked **Revise** or **Reject**, briefly explain why, using evidence from the text.

    **Discussion**

    - Which text produced more consistent subject terms.  
    - Which led to broader or more ambiguous suggestions.  
    - What information would be needed to make confident cataloging decisions.

## Integrating AI into Library and Enterprise Information Systems

AI in information organizations is rarely used as a standalone tool. Instead, it is embedded within larger systems such as library platforms, enterprise knowledge bases, document management systems, or customer support environments. Users often interact with AI indirectly, through interfaces that appear familiar and routine.

In this embedded form, AI supports specific functions rather than replacing entire workflows. It may assist with search ranking, metadata suggestion, content routing, or access control, while human staff remain responsible for oversight, interpretation, and decision-making. This design reflects organizational needs for consistency, accountability, and risk management.

Understanding AI at the system level shifts attention away from individual tools and toward how AI reshapes workflows. The key questions are where AI assistance is appropriate, where human review is required, and how institutional context determines responsible use.

!!! example "In-class activity: Mapping AI in an Information System"

    **Purpose**  
    Recognize how AI fits into organizational workflows rather than operating as a standalone tool.

    **Steps**

    1. Choose one familiar environment.  
       A library system.  
       A university office or administrative unit.  
       A workplace or enterprise information system.

    2. Sketch or outline the information workflow.  
       Where information is created, stored, searched, or shared.

    3. Mark where AI might be integrated.  
       Places where AI could support organization or access.  
       Places where human review or approval would still be required.

    4. Optional.  
       Ask an AI tool to describe a similar workflow and compare it with your own outline.

    **Think about**

    - Where AI support seems helpful or efficient.  
    - Where AI use could create confusion, risk, or accountability issues.  
    - How organizational context shapes what responsible AI use looks like.

    **Key takeaway**

    AI in information systems works as embedded support within workflows. Authority and responsibility remain organizational and human.

## AI-Driven Reference and Information Services

AI-driven reference services are often used as a first point of contact. They can answer routine questions quickly, support navigation, and help users clarify what they are looking for. In many systems, the AI layer is embedded in chat interfaces, help centers, or knowledge bases, so users may experience it as part of normal service rather than as a separate tool.

The key issue is scope boundaries. AI assistants can be useful for questions with clear intent, stable answers, and low stakes. They are less reliable when questions are ambiguous, require local policy interpretation, or involve sensitive situations. In those cases, the appropriate outcome may not be an answer, but a handoff to a human professional.

A practical way to evaluate AI reference is to focus on three aspects. Whether the response matches the user’s intent. Whether it stays within available evidence and does not invent details. Whether it signals limits and routes the user to human help when needed.

!!! example "In-class activity: Defining the Role of a Virtual Assistant"

    **Purpose**  
    Clarify what AI reference services are suited for and where human support is necessary.

    **Steps**

    1. Write three reference style questions.
       One routine.
       One ambiguous.
       One complex or sensitive.

    2. Ask an AI assistant to respond to each question.

    3. Read the responses carefully.

    **Think about**

    - Where the AI response feels appropriate for first contact.  
    - Where the response feels incomplete, overly confident, or risky.  
    - When a human professional would need to step in.  
    - What the assistant should do instead of answering, such as asking a clarifying question or directing the user to the right office or policy.

    **Key takeaway**

    AI reference works best for routine first contact. Clear boundaries and human handoff are part of responsible service design.
