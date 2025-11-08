# ContentGen

## Overview
ContentGen is a JupyterLab extension available on [PyPI](https://pypi.org/project/contentgen/) that generates context-aware practice questions and summaries directly within notebooks. Developed at the Data Science Teaching & Learning Lab at UC San Diego, it supports instructors by embedding dynamic, AI-generated content into the notebook workflow.

The extension includes a pip-installable Python backend and a TypeScript frontend connected through custom HTTP handlers.

Contributors: Ylesia Wu, Ayush Shah, Gabriel Cha, and Jiaen Yu, under the guidance of Professor Sam Lau.


## Quick Start

By the way, our extension package is called `server-extension` for now.

1. Clone the ContentGen-demo repo: `git clone https://github.com/dstl-lab/ContentGen-demo.git`
2. `cd ContentGen-demo`
3. `conda env create -f environment.yml`
4. `conda activate contentgen-demo`
5. `pip show server-extension`
6. Identify from the displayed message `Location: <your_own_path>/site-packages`
7. `cd <your_own_path>/site-packages/server_extension`
8. `vim .env`
9. Type in GEMINI_API_KEY=<your-api-key>, no spaces
10. Type in `:wq`, then hit enter
11. Navigate back to the cloned ContentGen-demo repo
12. `jupyter lab`


### Get a Gemini Api Key
1. Go to https://aistudio.google.com/u/1/apikey and create an API key, copy/store it
2. navigate to repo root folder
3. navigate to server-extension/server_extenion
4. create a `.env` file
5. type in GEMINI_API_KEY=\<your-key\>, don't leave any space, and save

## Resources

## Acknowledgments
