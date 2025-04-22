# ContentGen-demo

Here are the set up instructions :)

By the way, our extension package is called `server-extension` for now.

1. Clone the ContentGen-demo repo: `git clone https://github.com/dstl-lab/ContentGen-demo.git`
2. `cd ContentGen-demo`
3. `conda env create -f environment.yml` OR `conda env create -f environment-dsc80.yml`
4. `conda activate contentgen-demo` OR `conda activate contentgen-dsc80`
5. `pip show server-extension`
6. Identify from the displayed message `Location: <your_own_path>/site-packages/server_extension/`
7. `cd <your_own_path>/site-packages/server_extension`
8. `vim .env`
9. Type in GEMINI_API_KEY=<your-api-key>, no spaces
10. Type in `:wq`, then hit enter
11. Navigate back to the cloned ContentGen-demo repo
12. `jupyter lab`


## Get a Gemini Api Key
1. Go to https://aistudio.google.com/u/1/apikey and create an API key, copy/store it
2. navigate to repo root folder
3. navigate to server-extension/server_extenion
4. create a `.env` file
5. type in GEMINI_API_KEY=\<your-key\>, don't leave any space, and save
