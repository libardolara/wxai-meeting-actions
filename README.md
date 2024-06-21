# GenAI Meeting Actions

This repository is a Proof of Concept on how to use GenAI to create a Meeting Actions AI to take your meetings transcript into actions. Meeting Actions could be sending and email, modifying a document, reseaching a topic, among others. Using Generative AI we would like to use a meeting recording to make these actions possible. In this project we will use IBM's [watsonx.ai](https://www.ibm.com/products/watsonx-ai) platform to access the LLMs needed. It is worth noting that this is not an MVP, the objective of this repository is to proof that the technology has the ability to achieve the desired use case.

## Prerequistes

* Jupyter Notebook Environment
* IBM Cloud account
* Access to IBM Speech-to-Text (Plus), and Watstonx.ai.

## Use case

This PoC addresses the use case of using the a meeting to modify a document. The AI system would take a meeting recording and use it to extract the modifications to a discussed document. The business pain point addressed is the long and tedious tasks of manually transcribing, extracting the modifications discussed and then actually modifying the document. The **WOW** factor is the speed in which we can generate a new version of the document.

