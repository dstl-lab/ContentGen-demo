# ContentGen-demo Set Up Instructions

Here are the set up instructions :)

By the way, our extension package is called `server-extension` for now.

1. Clone the ContentGen-demo repo: `git clone https://github.com/dstl-lab/ContentGen-demo.git`
2. `cd ContentGen-demo`
3. `conda env create -f environment.yml`
4. `conda activate contentgen-demo`
5. `pip show server-extension`
6. Identify from the displayed message `Location: <your_own_path>/site-packages/server_extension/`
7. `cd <your_own_path>/site-packages/server_extension`
8. `vim .env`
9. Type in GEMINI_API_KEY=<your-api-key>, no spaces
10. Type in `:wq`, then hit enter
11. Navigate back to the cloned ContentGen-demo repo
12. `jupyter lab`
