# Text-Mining Part 1

Please note that you don't need to use this code to submit to the competition! You can use any language you want (R?), and submit a csv to Kaggle without needing anything else.

However, if you want to use this noteboko, you can either run a Jupyter notebook on your own computer, run a docker container on your own computer(recommended), or run an aws instance (also recommended). Instructions for each:


#### Jupyter on your own

In the repo you will find the Jupyter Notebook you can run. In addition to the usual stuff, you will need to install spacy, nltk, & langdetect. You will also need to download a spacy model (at least 'en'). Instructions for loading spacy models can be found at [spacy.io](https://spacy.io). Just keep 'pip install'-ing until you get everything!

Start by cloning the repo:

```{sh}
git clone https://github.com/nandanrao/text-mining
```

Then run your jupyter from inside that folder!


#### Docker on your own

You can run this on your own machine, or a cloud instance. First, install docker if you don't already have it, following these instructions:

* [For Mac OSX](https://docs.docker.com/docker-for-mac/install/)
* [For Windows](https://docs.docker.com/docker-for-windows/install/)
* [For Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

Clone the repo and run docker from your shell:

```{sh}
git clone https://github.com/nandanrao/text-mining
cd text-mining
docker run -d --name text-mining -v $PWD:/home/jovyan -p 8888:8888 nandanrao/text-mining start.sh jupyter lab --NotebookApp.password='sha1:ed21921c94d1:2af52eda4765ea12514f45468fac48418c6c8ec5'
```

Once this is all downloaded and running, navigate to [localhost:8888](http://localhost:8888) and enter the password we used in class!

Note, this will download the nandanrao/text-mining docker image, which is quite large (~3gb). So make sure you have a connection. This is because I've included, in addition to all the usualy libraries, several of the larger spacy models as well.

#### AWS (w/ Docker)

Launch an instance from the following AMI:

```
ami-50062329
```

Then add the following under "Configure Instance Details" > "Advanced Details" > "User Data" > "As text":

``` shell
#! bin/sh

docker rm notebook && docker run --name notebook -d -p 80:8888 -v /home/ubuntu:/home/jovyan  nandanrao/text-mining start.sh jupyter lab --NotebookApp.password='sha1:ed21921c94d1:2af52eda4765ea12514f45468fac48418c6c8ec5'
```

Then navigate to the public DNS of the instance, and enter the password we used in class, and you should be up and running!
