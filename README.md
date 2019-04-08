
---
title: Text Mining for Social Sciences
author: Nandan Rao
date: April, 2019
...


## Outline

  * Informatiion Retrieval
  * NLP
  * Preprocessing Preprocessing Preprocessing

---

## Social Sciences meets ML?

>> When solving a problem of interest, do not solve a more general problem as an intermediate step. Try to get the answer that you really need, but not a more general one. \hfill (Vladimir Vapnik)

&nbsp;
&nbsp;

Statistical Modelling: The Two Cultures

[https://projecteuclid.org/download/pdf_1/euclid.ss/1009213726](https://projecteuclid.org/download/pdf_1/euclid.ss/1009213726)

---

## What is Information Retrieval?

  * Information retrieval $\approx$ search.
  * One of the basic, early problems of internet engineering and information organization.
  * Many of the tools we use in NLP were created for this problem.
  * You have a corpus of documents (for example: the internet). You have a user who wants a few of these documents. How do you design this system?


---

## Information Retrieval - Naive Search

  Let's say you are inventing search. Imagine someone searching for the term "People who see ghosts". How could you pick between the following?

  * This is a document about people who see ghosts. Those people end up on TV shows.
  * This is a document about seeing goats. Those people work on farms.


---

## Information Retrieval - Naive Search

Let's try again with the term: "People who see ghosts"

"I don't believe people who see ghosts", said Mannie, before spitting into the wind and riding his bike down the street at top speed. He then went home and ate peanut-butter and jelly sandwiches all day. Mannie really liked peanut-butter and jelly sandwiches. He ate them so much that his poor mother had to purchase a new jar of peanut butter every afternoon.

We have collected a report of every resident in our community that has seen a ghost. Each resident was asked "how many ghosts have you seen?", "describe the last ghost you saw", and "tell us about your mother." Afterwards, we compared the ghost reports between the different individuals, and assessed whether or not they had actually seen these apparitions.


---

## Information Retrieval - Naive Search

Let's try again with the term: "People who see ghosts"

"I don't believe **people who see ghosts**", said Mannie, before spitting into the wind and riding his bike down the street at top speed. He then went home and ate peanut-butter and jelly sandwiches all day. Mannie really liked peanut-butter and jelly sandwiches. He ate them so much that his poor mother had to purchase a new jar of peanut butter every afternoon.

We have collected a report of every **resident** in our community that has **seen** a **ghost**. Each **resident** was asked "how many **ghosts** have you **seen**?", "describe the last **ghost** you **saw**", and "tell us about your mother." Afterwards, we compared the ghost reports between the different **individuals**, and assessed whether or not they had actually **seen** these **apparitions**.

---

## Information Retrieval - Term Frequency


  * Frequency matters!
  * Let's try and count the frequency of each word

---

## Information Retrieval - Linguistic Tricks
  \textbf{Stop words} "seen a ghost" $\rightarrow$ "seen ghost"

  \textbf{Stemming} "seen a ghost" $\rightarrow$ "see ghost"

  \textbf{Lemmatization} "saw ghosts" $\rightarrow$ "see ghost"

  \textbf{Tokenization} "see ghost" $\rightarrow$ ["see", "ghost"]

---

## Information Retrieval - Synonyms

We might need some concept of synonyms.

* ghost, apparitions, spook $\rightarrow$ ghost
* people, individuals, residents, folk $\rightarrow$ people

Are these actually synonyms?

---


## Information Retrieval - TF Fail

Now let's try our tools on the following text:

&nbsp;

> People see incredible things. One time I saw some people talking about things they had seen, and those people were so much fun. They saw clouds and they saw airplanes. Can you believe the amount of seeing done by these people? People are the best.


---

## Information Retrieval - IDF

Let $df_v$ be the number of documents that contain the term $v$.

The _inverse document frequency_ is

$$
    \textrm{idf}_v = \log\left( \frac{D}{df_v} \right),
$$

where $D$ is the number of documents.

Properties:

1. Higher weight for words in fewer documents.
2. Log dampens effect of weighting.

---


## Information Retrieval - IDF

For words which are more common, we lower their weights.

(example)

---


## Information Retrieval - IDF

  Words which appear in \textit{many} of the documents are not going to help us pick \textit{one} document.

---


## Natural Language Processing

  What is Natural Language Processing?

  * [https://en.wikipedia.org/wiki/Natural-language_processing\#History](https://en.wikipedia.org/wiki/Natural-language_processing\#History)
  * [https://www.cl.cam.ac.uk/archive/ksj21/histdw4.pdf](\url{https://www.cl.cam.ac.uk/archive/ksj21/histdw4.pdf})


---


## Natural Language Processing

  Two large challenges of Natural Language Processing:

  * Put language into a metric space.
  * Deal with the complex correlations between words in a sentence, and sentences in a document.


---

## Metric Space

A metric space consists of a set (we'll call them **documents** in this context) and a distance metric between items in the set.

* What are some possible measures of "distance" between two documents?

---

## Space

(word count example)

---

## Distances

Now that we have our data into a numeric form, how can we determine a distance?

---

## Distances

What about the distance between these two documents?

* We have collected a report of every resident in our community that has seen a ghost. Each resident was asked "how many ghosts have you seen?", "describe the last ghost you saw", and "tell us about your mother." Afterwards, we compared the ghost reports between the different individuals, and assessed whether or not they had actually seen these apparitions.


* We ask each resident how many ghosts they've seen.

---

## Distances

We _might_ want a distance that ignores the "size" of the document.

One option is to normalize our vectors to unit length, this has the advantage of keeping the "direction" while removing the size element. Once we normalize our vectors, the euclidian distance becomes proportional to:

$$
|| A - B ||^2 \propto 1 - A^TB = 1 - \cos \theta
$$

Where $1 - \cos \theta$ is referred to as the **cosine distance** and $1 - \cos \theta$ is referred to as the **cosine similarity**.

---

## Space

What about the similarity of these two documents:

People who see ghosts are full of crap. I don't believe a word they say. They didn't actually see any ghosts. No way! They are just seeing things.

We talked to lots of people who have seen ghosts. Each person was asked "how many ghosts have you seen?" They had a lot of interesting and disturbing stories about the ghosts in their lives.

---

## NGrams

With the previous example, stemming/lemmatization + NGrams + TF-IDF would yield a feature:

"see ghost"

which would most likely be very highly weighted (depending on the corpus). This would help these two documents to be very similar, even though they are not in the simple BOW space.

---

## NGrams

Similarly, in a 2-gram space these two documents separate:

Sometimes, at my job, I use text mining.

Sometimes, at my mining job, I text.

---

## NGrams

"at my job, I use text mining"

```
["at my", "my job", "job I",
"I use", "use text", "text mining"]
```

&nbsp;

"at my mining job, I text"

```
["at my", "my mining", "mining job",
"I text"]
```

---

## Distances

What about a continuous metric space?

---

## Distances

Co-occurences can be used as a proxy for semantic similarity.

---

## Distances

(embedding example)

---

## Distances

Other ways to think about semantic structure of a sentence?

Grammar???

---


## Natural Language Processing

  * In an attempt to create conversations, computer scientists brought in linguists.
  * There was a need to understand the semantic content of sentences.

---


## Natural Language Processing

  How can we differentiate between these documents?


  * France: Migrant stabbed to death in Calais
  * Afghan asylum seeker stabbed to death in London park
  * Clashes in Istanbul after angry mourners of a Turkish man is stabbed to death by an Afghani refugee
  * German woman stabbed to death by Syrian refugee on her doorstep
  * In memory to Bangladeshi migrant \#Manan stabbed to death 6y ago during pogrom orchestrated by Nona's
  * great people? the people that kicked over jugs of water to let migrants die in the desert? those are not great people.

---

## Machine Learning with Language

[https://github.com/nandanrao/text-mining/blob/master/dependency-tree-example.ipynb](https://github.com/nandanrao/text-mining/blob/master/dependency-tree-example.ipynb)

---
---
title: Classifying Text
author: Nandan Rao
date: April, 2019
...


## Outline

* Emprical risk minimization and $p(y,x)$
* $p(x)$ when $X$ is language
* Generative vs discriminative classifiers
* Hyperparameters in BOW framework
* Towards supervising the embedded space

---

## Emprical Risk Minimization

Consider an input space $X$, a discrete output space $Y$ and a function, $g: X \rightarrow Y$ which predicts a value for $y$ given an input $x$. Consider also a _loss function_ $\ell: Y,Y \rightarrow \mathbb{R}$.

The _risk_ of the classifier $g$ is defined as:

$$
R(g) = \mathbb{E}_{X,Y} [ {\ell(g(x), y)} ]
$$
$$
R(g) = \sum_{y \in Y} \int_X \ell(g(x), y) \  p(x,y) \ dx
$$

---

## Emprical Risk Minimization

We estimate the risk with its finite-sample approximation, the _empirical risk_:

$$
R(g) = \frac{1}{n} \sum_{i=1}^n \ell(g(x_i), y_i)
$$

Note, that this is only an approximation of $\mathbb{E}_{X,Y}$ if all the pairs:

$$
x_i, y_i \in p(X,Y)
$$

---

## Emprical Risk Minimization

$$
x_i, y_i \in p(X,Y)
$$

Implies that $p(Y|X)$ and $p(X)$ are the same in our validation distributions as they are in our target distribution.

Ways to deal with changes in any of the component parts of the joint distribution are covered in the literature of _domain adaptation_.

---

## Language

What is $p(X)$ when we are dealing with language?

Again, we will consider that each $x_i$ is a document.

Is the document space continuous?

Hopefully you see why for most tasks related to NLP, we want the space to be continuous.

Thus, in order to classify, we need to embed the documents into a continous space, with a continuous distance metric.


---


## Generative classifiers

Generative classifiers seek to model the join probability $p(X,Y)$ directly.

With a model built of the joint probability, the classification simply consists of applying bayes rule to the joint probability and picking the class $y \in Y$ with the highest $p(y|x)$

---

## Discriminative classifiers

Discriminative classifiers either:

* Directly model the posterior, $p(Y|X)$
* Learn a direct mapping $g: X \rightarrow Y$

---


## Logistic Regression

Logistic regression models the posterior probability as:

$$
p(y|x; \beta) = \sigma(\beta^Tx)
$$

where the logistic function $\sigma$ is given by:

$$
\sigma(n) = \frac{1}{1 + \exp^{-n}}
$$

This can be fit via maximum likelihood ($\ell := -p(y|x; \beta)$) or by any other convex surragote of the 0-1 error ($\ell := 1\{ g(x) \neq y \}$)

---


## Naive Bayes

As mentioned, Naive Bayes predicts based on the posterior calculated from the modelled joint distribution:

$$
p(y|x) = \frac{p(x|y)p(y)}{p(x)}
$$

It's called "naive" because we make the (extreme) simplifying assumption that all the $p(x_i|y)$ are independent and thus $p(x|y) = \prod_i p(x_i|y)$.

---

## Naive Bayes


What does this independence assumption amount to saying about language?

---

## Naive Bayes

Let's see how a multinomial naive Bayes can be related to logistic regression:

$$
p(y = 1 | x) = \frac{p(x,y=1)}{\sum_y p(x, y=y_i)}
$$
$$
p(y = 1 | x) = \sigma \bigg(  \log \frac{p(x,y_1)}{p(x,y_0)} \bigg)
$$
$$
p(y = 1 | x) = \sigma \bigg(  (\pi_1 -\pi_0)^Tx + \log \frac{p(y_1)}{p(y_0)} \bigg)
$$

Where $\pi_i$ denotes the log probability parameters of the multinomial distribution representing $p(X|y_i)$

---

## Naive Bayes

Thus the binary multinomial naive Bayes is a linear classifier and, in particular, one in which the coefficients are equal to the log difference in probabilities that a particular feature shows up in each class.

---

## Asymptotic Properties

Logistic regression searches the space of linear classifiers in the feature space, finding the linear classifier with the lowest empirical risk in the training set.

Naive Bayes is a specific linear classifier that makes distributional assumptions over the data generating process $p(X|Y)$.

It should be clear that, asymptotically, logistic regression will converge to the optimal linear classifier. It's not clear that Naive Bayes will do the same, if the distributional assumptions do not hold. Thus:
$$
R(g_{LR, \infty}) \leq R(g_{NB, \infty})
$$

---

## Asymptotic Properties

However, making more assumptions allows Naive Bayes to reach it's asymptotic risk quicker, as shown by Andrew Ng and Michael Jordan:

[https://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf](https://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf)

Let's try this on our data.

---

## Hyperparameter Optimization

A hyperparameter is any parameter that the optimization process of the our learning algorithm does not optimize over.

Thus in logistic regression, the regularization term, $\lambda$, is a hyperparameter.

Our training algorithm will pick the parameters that minimize the in-sample empirical risk.

We pick hyperparameters to minimize the out-of-sample empirical risk.

This usually is done either by changing the class of models searched by the algorithm or by changing the loss function to reduce the generalization error.

---

## Hyperparameter Optimization

In our simple language models, however, it should be clear that we have hyperparameters that we want to tune that seem to have nothing to do with our model.

For example, all the parameters in the vectorizing step.

These parameters guide the way that our documents are embedded in the metric space.

We want this embedding to be the best that it can be, such that it minimizes our expected risk.


---

## Hyperparameter Tuning

How can we pick good hyperparameters?

---

## Hyperparameter Tuning

The simplest way to tune hyperparameters is to make no assumptions about them and just search the entire space, hoping to find ones that are relatively good.

This is, interestingly enough, very common!

It's called grid search.

---

## Tuning an embedding

It should be clear, however, that this is not ideal.

Is it possible to jointly optimize the way that we embed language into a metric space AND the classification function at the same time?

---

---
title: Text Mining for Social Sciences
author: Nandan Rao
date: April, 2019
...

## Social Sciences and Text Mining

This is hot stuff.

Some examples:

---

## Social Sciences - Missing Migrants

  \includegraphics[width=\textwidth]{assets/missingmigrants}

---

## Social Sciences - Missing Migrants


* The Missing Migrants project is essentially one of dataset creation.
* These statistics are not available from any single state.
* News agencies report the events. In plain text!

---

## Social Sciences - Missing Migrants

\includegraphics[width=\textwidth]{assets/newsfilter}

---

## Social Sciences - OECD \& Freelance Labor Markets

What is the effect of the explosion of freelancing websites on the labor market? Demand side:

* "I need an experienced Business Strategist who can write content explaining all the important moving parts and pieces of building a business plan and/or business model. You'll be explaining to first time entrepreneurs and small business owners and diving into the importance"

* "We are Ricardo Steak House Restaurant located in Harlem, New York. We are looking for an expert opinion and training on how to manage our accounting department"

* "We are an 8Mil per year trucking company based out of NJ. Due to negative loss-runs, we lost ideal market coverage for insurance and forced to use Progressive Commercial. We need someone with both an accounting background and deep knowledge of commercial insurance..."

---

## Social Sciences - OECD \& AI

How can we measure the growing share of artificial intelligence in worldwide innovation?

Corpora: Github, Patents.

One-class classification

Keep classification fixed, improve embedding.

---

## Social Sciences - Warwick \& Online Labor Markets

How can we use online labor markets as a realtime view on shifts in jobs and skills demanded?

---

## Social Sciences - Warwick \& Wages + Tasks

How do the returns to tasks change over time?

What are tasks? Created manually? Extract from text?

---
