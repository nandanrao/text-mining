# Text-Mining Part 1

Please note that you don't need to use this code to submit to the competition! You can use any language you want (R?), and submit a csv to Kaggle without needing anything else.

However, if you want to use this noteboko, you can either run a Jupyter notebook on your own computer or run a docker container (recommended). Instructions for each:


#### Jupyter on your own

In the repo you will find the Jupyter Notebook you can run. In addition to the usual stuff, you will need to install spacy, nltk, & langdetect. You will also need to download a spacy model (at least 'en'). Instructions for loading spacy models can be found at [spacy.io](https://spacy.io). Just keep 'pip install'-ing until you get everything!

Start by cloning the repo:

```{sh}
git clone https://github.com/nandanrao/text-mining
```

Then run your jupyter from inside that folder!


#### Docker

Install docker on your machine, following these instructions:

* [For Mac OSX](https://docs.docker.com/docker-for-mac/install/)
* [For Windows](https://docs.docker.com/docker-for-windows/install/)
* [For Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

Clone the repo and run docker from your shell:

```{sh}
git clone https://github.com/nandanrao/text-mining
cd text-mining
docker run -d --name text-mining -v $PWD:/home/hovyan -p 8888:8888 nandanrao/text-mining start.sh jupyter lab
```

Once this is all downloaded and running, you will see a link in your shell from jupyter. Copy and past that link into your browser, and you have your jupyter lab/notebook!

Note, this will download the nandanrao/text-mining docker image, which is quite large (~3gb). So make sure you have a connection. This is because I've included, in addition to all the usualy libraries, several of the larger spacy models as well.
