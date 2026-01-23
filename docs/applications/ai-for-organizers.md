# AI for Information Organization and Systems

## AI in Digital Archives and Preservation 

In large digitization programs, a major challenge is **scale**. When archives convert millions of pages and images into digital form, staff rarely have the capacity or the mandate to create detailed item-level records for every object from scratch. In practice, AI is used to improve search capabilities and to help professionals prioritize where their limited time and expertise are most needed.


Building on OCR (Optical Character Recognition) and basic text understanding, AI is used in digital archives primarily to address **scale**, not to produce complete or authoritative descriptions. Once text becomes machine-readable, AI systems can suggest draft descriptive elements and group large volumes of material into broad categories that support early access.

At this stage, AI outputs should be understood as **provisional structure**. Suggested titles, dates, names, or topical labels reflect patterns learned from existing data rather than interpretive understanding. Their value lies in making large collections searchable and navigable sooner, not in replacing professional descriptions.

**National Archives and Records Administration** documents its AI use through a [public inventory of AI use cases](https://www.archives.gov/ai). Rather than presenting AI as a single system, NARA’s public inventory describes multiple AI use cases, including both in-progress pilots and planned pilots. These range from task-focused applications that support access and discovery, such as semantic search and automated descriptive metadata, to internal productivity and knowledge tools, as well as higher-level planned initiatives. In many of the in-progress pilots, NARA frames AI as a support layer that generates candidate outputs or improves retrieval, while staff remain responsible for evaluating quality, verifying results, and making decisions that carry institutional responsibility.

**Further information:**

- [Combining AI tools with human validation to enrich cultural heritage metadata](https://pro.europeana.eu/post/combining-ai-tools-with-human-validation-to-enrich-cultural-heritage-metadata)
- [Inventory of NARA Artificial Intelligence (AI) Use Cases](https://www.archives.gov/ai)

!!! example "Hands on: From Raw Document to a Searchable Object"
    **Goal:** Observe how automated extraction can support access at scale while still requiring human judgment.
    
    **Steps:**

    1. Open a scanned PDF or an image-based document.  
    2. Use one tool that can extract text or descriptions, such as [Google Drive OCR](https://support.google.com/drive/answer/176692?hl=en&co=GENIE.Platform%3DDesktop), [Microsoft's PDF-to-Word](https://www.microsoft.com/en-us/microsoft-365/word/convert-pdf-to-word#Convert-to-Word), or an LLM with image input.  
    3. Identify elements in the extracted text that could potentially be used as metadata. Examples include title, date, creator, place, and subject keywords.  

    **Think about**

    1. Which extracted elements seem plausible but uncertain, and what might make them unreliable?  
    2. Which descriptive decisions would you not delegate to an automated tool without expert review?  
    3. What additional context or documentation would be needed to confirm or correct the draft metadata?


## Cataloging and Classification Automation

Automated cataloging tools support description by suggesting metadata based on patterns in existing records. They can propose subject terms, classification candidates, and other descriptive fields by comparing a resource to similar items that have already been cataloged. This can reduce routine effort and speed up early record creation, especially when processing large volumes of materials.

These suggestions are not the same as authoritative cataloging. The system does not interpret context, resolve ambiguity, or apply local standards on its own. Outputs can reflect the conventions and limits of the records the system learned from, so results require review and correction.

Classification remains a professional and institutional responsibility. Staff decide what to accept, revise, and reject based on local policy and cataloging practice. This includes decisions about controlled vocabularies, local consistency, and how description serves community and institutional priorities.


**Further information:**

- [OCLC cataloging with AI](https://www.oclc.org/en/connexion.html#catalog-with-ai). Watch the [presentation in the final session](https://www.oclc.org/go/en/events/cataloging-community-meeting/june-2025.html#final-session) (starting from 3:48 to 10:10) and review the [slides](https://www.oclc.org/content/dam/oclc/cataloging-subscription/cataloging-events/OCCM-2025-06-final-session.pdf#page=7.00).

!!! example "Hands-on: Assisted Description with a Fixed Prompt"

    **Goal**  
    Experience AI as a drafting assistant for description, not as an authority.

    **Instructions**

    1. Choose one generative AI tool you have access to. Examples include ChatGPT, Gemini, or Claude.

    2. Copy and paste the following prompt into the tool.

    **Prompt**
    
    ``` { .text .copy }
      You are assisting with preliminary cataloging.

      Use only the text provided. Do not infer details that are not stated.

      For each text:
      1. Write one clear, neutral descriptive sentence suitable for a brief note field.
      2. Suggest up to five subject terms as short noun phrases that reflect the main topics. Prefer terms that could plausibly map to a controlled vocabulary.
      3. If the text does not support a specific detail (e.g., author, date, place), leave it out rather than guessing.

      Return your output in this format for each text:

      Text A
      Description:
      Subject terms:

      Text B
      Description:
      Subject terms:
      
      Text A: This report examines how small public libraries in rural areas have adopted digital services over the past decade. It describes recent shifts toward online programs, remote reference services, and expanded e-book and streaming collections, often introduced in response to community demand and public health disruptions. The report discusses common constraints, including limited staffing, unstable funding, and gaps in broadband availability that affect both library operations and patron access. It summarizes strategies used by library directors to build capacity, such as partnerships with schools and local agencies, staff cross-training, and phased technology upgrades. The report draws on survey responses from library directors and includes several brief case examples that illustrate how libraries selected platforms, promoted services, and evaluated usage. It also notes equity considerations, including differences in access among older adults, low-income households, and residents in remote areas.

      Text B: This handbook introduces practical data management practices for non-technical staff working in cultural institutions such as libraries, museums, and archives. It explains how everyday decisions about file naming, folder structure, and version control affect long-term access and reduce the risk of accidental loss. The handbook covers basic storage planning, including the use of shared drives, cloud storage, and external media, and it outlines simple backup routines using the “3-2-1” approach. It emphasizes documentation practices that support continuity when staff roles change, such as maintaining readme files, recording data sources, and keeping a simple change log. The handbook includes short checklists and examples intended for daily work, but it does not address advanced data analysis, programming, or database design. It concludes with guidance on common pitfalls, including duplicate files, unclear ownership, and inconsistent naming conventions that make retrieval difficult over time.
    ```
    

    **For each text:**

    - Look through the subject terms suggested by the AI and consider how you would respond to them.
    - Identify which terms you would likely keep as-is, which you would want to revise, and which you would not use.

    **Think about**

    - Which text produced more consistent subject terms?
    - Which led to broader or more ambiguous suggestions?  
    - What information would be needed to make confident cataloging decisions?

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

         *Library example:*  
         A library discovery system such as the University of Kentucky’s [InfoKat Discovery](https://saalck-uky.primo.exlibrisgroup.com/discovery/search?vid=01SAA_UKY:UKY), with an AI-enabled research assistant.

         *Enterprise example:*  
         A campus-wide document management environment using [Microsoft Copilot](https://uky.service-now.com/techhelp?id=kb_article&sysparm_article=KB0015470&sys_kb_id=73f8af751b1a72500c850d00604bcb58). Copilot can retrieve, summarize, and synthesize content from shared OneDrive or SharePoint files.

      2. Mark where AI might be integrated.  
         Places where AI could support organization or access.  
         Places where human review or approval would still be required.

         *Library example:*  
         AI-assisted query interpretation, result ranking, topic suggestions, or summary views, versus cataloging decisions, access policies, and user guidance handled by library staff.

         *Enterprise example:*  
         AI-assisted document retrieval, summarization, or cross-file synthesis, versus decisions about records status, sharing, retention, and appropriate use governed by institutional policy and human oversight.

      **Think about**

      - Where AI support seems helpful or efficient in each environment?  
      - Where AI use could create confusion, risk, or accountability issues?
      - How library and enterprise contexts differ in terms of access control, responsibility, and acceptable AI use?

**Further information:**

- [Integrating AI into Library Systems: A Perspective on Applications and Challenges](https://doi.org/10.1145/3677389.3702568)
- [The State of AI in the Enterprise: Deloitte's 2026 AI report tracking adoption and impact](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)

## AI-Driven Reference and Information Services

AI-driven reference services are often used as a first point of contact. They can quickly answer routine questions, support navigation, and help users clarify what they are looking for. In many systems, the AI layer is embedded in chat interfaces, help centers, or knowledge bases, so users may experience it as part of normal service rather than as a separate tool.

The key issue is scope boundaries. AI assistants can be useful for questions with clear intent, stable answers, and low stakes. They are less reliable when questions are ambiguous, require interpretation of local policy, or involve sensitive situations. In those cases, the appropriate outcome may not be an answer, but a handoff to a human professional.

A practical way to evaluate an AI reference is to focus on three aspects. Whether the response matches the user’s intent. Whether it stays within available evidence and does not invent details. Whether it signals limits and routes the user to human help when needed.

!!! example "In-class activity: Defining the Role of a Virtual Assistant"

    **Purpose**  
    Clarify what AI reference services are suited for and where human support is necessary.

    **Steps**

      1. Write three reference-style questions.
         One routine.
         One ambiguous.
         One complex or sensitive.

         You are welcome to choose the library or the organization you are familiar with.
         The examples below use the William T. Young Library and the University of Kentucky
         as reference contexts.

         *Library example: William T. Young Library*

         - Routine  
         What are the William T. Young Library’s hours during finals week?

         - Ambiguous  
         I need help finding sources on artificial intelligence in education at the William T. Young Library.

         - Complex or sensitive  
         I am working with interview data that includes personal information. What are the William T. Young Library’s expectations for storing and sharing this data?

         *Enterprise example: University of Kentucky*

         - Routine  
         Where can I find the University of Kentucky’s academic calendar for this semester?

         - Ambiguous  
         What are the University of Kentucky’s rules about using AI tools for work or coursework?

         - Complex or sensitive  
         I am unsure whether certain documents should be retained or deleted under the University of Kentucky records policy. What should I do?


    2. Ask an AI assistant to respond to each question.

    3. Read the responses carefully.

    **Think about**

    - Where does the AI response feel appropriate for first contact?  
    - Where the response feels incomplete, overly confident, or risky?
    - When would a human professional need to step in?  
    - What the assistant should do instead of answering, such as asking a clarifying question or directing the user to the right office or policy?

**Further information:**

- A discussion group to explore the implications of Generative AI programs like ChatGPT on reference, instruction, and other user services: [Generative Artificial Intelligence, Reference, & Instruction Discussion Group (GAIR&I)](https://connect.ala.org/rusa/communities/community-home?communitykey=46466ca8-f965-4314-87e5-018955ba4c35)
