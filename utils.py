import re
from re import sub, split, findall
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.metrics import recall_score, precision_score, f1_score, average_precision_score, roc_auc_score
from sklearn.feature_extraction.text import VectorizerMixin

def scorer(y_test, p):
    d = {'precision': precision_score(y_test, p),
         'recall': recall_score(y_test, p),
         'f1-weighted': f1_score(y_test, p, average='weighted'),
         'ap': average_precision_score(y_test, p),
         'auc': roc_auc_score(y_test, p)}
    return pd.DataFrame(d, index=['score'])

def ngrammer(tokens, ngram_range):
    mix = VectorizerMixin()
    mix.ngram_range = ngram_range
    return mix._word_ngrams(tokens)

def clean_html(s):
    """ Converts all HTML elements to Unicode and removes links"""
    try:
        s = sub(r'https?://[^\s]+', '', s)
        return BeautifulSoup(s, 'html5lib').get_text() if s else ''
    except UserWarning:
        return ''
    except Exception as e:
        print(e)
        return ''

def get_errors(X_test, y_test, preds):
    """ Creates a DataFrame with false negatives and false positives """
    df = pd.DataFrame({'text': X_test, 'prediction': preds, 'label': y_test})
    problems = df[df.label != df.prediction]
    return (problems[problems.label == False]
            , problems[problems.label == True])


def get_top_features(v, model, accepted = True, start = 1, end = 10):
    """ Get the most probable n-grams for a naive bayes model.

    >>> V_train, V_test, vectorizer = create_vectors(X_train, X_test)
    >>> model = MultinomialNB()
    >>> model.fit(V_train, y_train)
    >>> get_top_features(vectorizer, model)
    """
    i = 1 if accepted else 0
    probs = zip(v.get_feature_names(), model.feature_log_prob_[i])
    return sorted(probs, key = lambda x: -x[1])[start:end]

def write_submission_csv(preds, ids, file_name):
    d = {'id': ids, 'label': preds}
    pd.DataFrame(d).to_csv(file_name, index = False)
