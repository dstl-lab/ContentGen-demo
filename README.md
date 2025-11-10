# ContentGen

## Overview
**ContentGen** is a JupyterLab extension available on [PyPI](https://pypi.org/project/contentgen/) that generates context-aware practice questions and summaries directly within notebooks. Developed at the Data Science Teaching & Learning Lab at UC San Diego, it supports instructors by embedding dynamic, AI-generated content into the notebook workflow. The extension includes a pip-installable Python backend and a TypeScript frontend connected through custom HTTP handlers.

This project accompanies the paper *“Improving LLM-Generated Educational Content: A Case Study on Prototyping, Prompt Engineering, and Evaluating a Tool for Generating Programming Problems for Data Science.”*


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

### Get a Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/apikey) and create an API key.
2. Copy and store your key securely.
3. Launch JupyterLab, open the **ContentGen** sidebar, and paste the key when prompted.


## Resources

- [**ContentGen** on PyPI](https://pypi.org/project/contentgen/): official Python package for installing the ContentGen extension.  
- [**Public GitHub Repository**](https://github.com/dstl-lab/ContentGen-public): open-source version of the extension’s codebase.
- [**Prompt Templates**](https://github.com/dstl-lab/ContentGen-public/blob/main/contentgen/handlers.py): backend prompts used for content generation.  
- [**Example Notebooks**](example_notebooks): demonstration notebooks showing typical usage; dependencies listed in [requirements.txt](requirements.txt).  
- [**Evaluation Dataset**](evaluation_dataset): anonymized dataset used in our study for evaluating generated content quality.


### Running the Example Notebook

To run the example notebooks locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/dstl-lab/ContentGen-demo.git
   cd ContentGen-demo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch JupyterLab:
   ```bash
   jupyter lab
   ```
4. Open the notebooks in `example_notebooks`.

You can then explore the notebooks interactively and utilize the **ContentGen** extension within JupyterLab to generate AI-assisted teaching content.


## Acknowledgments

This project was developed as part of the Data Science Teaching & Learning Lab at UC San Diego, led by Professor Sam Lau.  

Contributors: Ylesia Wu, Ayush Shah, Gabriel Cha, and Jiaen Yu.  

We thank the lab members for their feedback during development of the tool.


## Contact Information

**Sam Lau**  
GitHub: [@SamLau95](https://github.com/SamLau95)  
Email: sel011@ucsd.edu

**Jiaen Yu**  
GitHub: [@yujiaen1999](https://github.com/yujiaen1999)  
Email: jiy037@ucsd.edu

**Ylesia Wu**  
GitHub: [@ylesia-wu](https://github.com/ylesia-wu)  
Email: xw001@ucsd.edu

**Ayush Shah**  
GitHub: [@Ayush1124](https://github.com/Ayush1124)  
Email: ajshah@ucsd.edu

**Gabriel Cha**  
GitHub: [@gabrielchasukjin](https://github.com/gabrielchasukjin)  
Email: gcha@ucsd.edu
