#!/usr/bin/env python
# coding: utf-8

# Reading Data 

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import os
tt = pd.read_csv('immSurvey.csv')

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

tt[['stanMeansNewSysPooled','textToSend']].head()


#------------### FORMER GP WITH TfidVectorizer ###------------#

from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X = vec.fit_transform(sample)
X

pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
X = vec.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

# FORMER GP
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

# Compute posterior predictive mean and covariance
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

#test correlation between test and mus
np.corrcoef(ytest, mu_s)


#------------### HOMEWORK GP WITH Bi-gram Vectorizer ###------------#

from sklearn.feature_extraction.text import CountVectorizer


bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

X = bigram_vectorizer.fit_transform(sample)
X

pd.DataFrame(X.toarray(), columns=bigram_vectorizer.get_feature_names()).head()

analyze = bigram_vectorizer.build_analyzer()


# HOMEWORK GP 
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

# Compute posterior predictive mean and covariance
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

#test correlation between test and mus
np.corrcoef(ytest, mu_s)


# As we saw in the lecture, the correlation between estimates and the truth was ~.68 with TfidVectorizer, and with bigram vectorizer it has become ~.61

