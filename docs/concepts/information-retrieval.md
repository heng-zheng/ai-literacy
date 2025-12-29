# AI for Search, Discovery, and Recommendation

## Why Information Retrieval Matters?
- What problems IR tries to solve
- Where IR appears in everyday systems

## How Information Retrieval Works
- Indexing
- Querying
- Ranking

## How AI Enhances Information Retrieval

### AI for Understanding Content

- **OCR + text understanding**: OCR (Optical Character Recognition) is a form of image recognition that detects and recognizes text in visual files such as scanned documents, photographs of pages, and image-based PDFs. By identifying text regions and converting visual characters into machine-readable text, OCR makes the contents of non–digital-born materials searchable and accessible to information systems.

    Basic text understanding then operates on the extracted text to identify document structure and basic elements, such as paragraphs, headings, dates, or layout boundaries. Rather than interpreting full meaning or assigning topics, this step prepares the text for downstream tasks like indexing, metadata enrichment, and search

    A practical example of OCR and basic text understanding is [Adobe PDF Extract API](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/), which converts scanned documents and other image-based PDF files into structured, machine-readable text.

- **AI for Indexing**: AI-based indexing works by having computers read large numbers of documents and look for patterns in the text, such as frequently discussed ideas, important terms, and how words are used together. From this, the system can automatically create summaries, topics, or labels that describe what each document is about.

    Unlike traditional indexing that depends on exact keywords or fixed rules, AI learns from examples and improves as it processes more documents. This makes it especially useful for large and changing collections, where new topics and terminology appear over time.

    One common example of AI-based indexing is *topic modeling*. Topic modeling helps the system discover main themes across a collection of documents by grouping texts that discuss similar ideas. For instance, in a large set of news articles or research papers, topic modeling can automatically identify topics such as healthcare, education, or technology and use them as index terms to support browsing and discovery.

- **AI for Enriching Metadata**: AI-based metadata enrichment focuses on adding or enhancing descriptive information for individual items, such as subject terms, keywords, named entities, or short summaries, based on document content. Rather than determining how documents are indexed at the system level, metadata enrichment improves how each item is described in catalogs, archives, or discovery systems.

    This is valuable for large-scale digitization projects or legacy collections, where records may contain minimal or inconsistent metadata. By automatically analyzing text, images, or audiovisual materials, AI can help fill in missing fields, standardize descriptions, and make materials easier to find and understand.

    A common example of AI-based metadata enrichment is *named entity recognition*. For instance, when processing a digitized historical letter or newspaper article, an AI system can identify people, organizations, and places mentioned in the text. These enriched metadata fields improve search, filtering, and user exploration without requiring manual cataloging of every item.

### AI for Understanding Queries
- Natural language queries
- Intent detection
- Query expansion

### AI for Ranking & Relevance
- Learning to rank
- Context-aware relevance

### AI for Interaction
- Conversational search
- Retrieval-Augmented Generation (RAG)
- Explanatory vs. black-box results

### Examples of AI-Enhanced Search and Discovery
- Web search (e.g., Google)
- Library discovery systems (e.g., Primo)
[Add a demo video using infokat research assistant]

## What algorithms show and hide