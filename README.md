# ContentGen

## Overview
ContentGen is a JupyterLab extension available on [PyPI](https://pypi.org/project/contentgen/) that generates context-aware practice questions and summaries directly within notebooks. Developed at the Data Science Teaching & Learning Lab at UC San Diego, it supports instructors by embedding dynamic, AI-generated content into the notebook workflow.

The extension includes a pip-installable Python backend and a TypeScript frontend connected through custom HTTP handlers.

Contributors: Ylesia Wu, Ayush Shah, Gabriel Cha, and Jiaen Yu, under the guidance of Professor Sam Lau.


## Quick Start

### Install the Extension
To install the latest release from PyPI:

```bash
pip install contentgen
```

Then launch JupyterLab:

```bash
jupyter lab
```

Open the **ContentGen** sidebar and enter your API key to start generating content.

### Get a Gemini Api Key
1. Go to [Google AI Studio](https://aistudio.google.com/apikey) and create an API key.
2. Copy and store your key securely.
3. Launch JupyterLab, open the **ContentGen** sidebar, and paste the key when prompted.


## Resources

- [**ContentGen** on PyPI](https://pypi.org/project/contentgen/): official Python package for installing the ContentGen extension.  
- [**Public GitHub Repository**](link): clean public version of the extension’s source code.
- [**Prompt Templates**](link): backend prompts used for content generation.  
- [**Example Notebook**](link): demonstration notebook showing typical usage; dependencies listed in [requirements.txt](link-to-requirements).  
- [**Evaluation Dataset**](link): anonymized dataset used in our study for evaluating generated content quality.

## Acknowledgments
