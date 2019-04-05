#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pystan


# In[3]:


main = pd.read_csv('trend2.csv')
main = main[main['church2'].isna()==False]
main = main[main['gini_net'].isna()==False]
main = main[main['rgdpl'].isna()==False]

main.country = main.country.str.strip()

countries = main.country.unique()
country_lookup = dict(zip(countries, range(len(countries))))
country = main['country_code'] = main.country.replace(country_lookup).values

main.reset_index(inplace=True)
main['idnum']=main.index
n_country = main.groupby('country')['idnum'].count()

u = np.log(main.rgdpl)


# In[4]:


# PART 1
hierarchical_intercept = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] u;
  vector[N] x;
  vector[N] y;
} 
parameters {
  vector[J] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {
  vector[N] y_hat;
  vector[N] m;

  for (i in 1:N) {
    m[i] = a[country[i]] + u[i] * b[1];
    y_hat[i] = m[i] + x[i] * b[2];
  }
}
model {
  mu_a ~ normal(0, 1);
  a ~ normal(mu_a, sigma_a);
  b ~ normal(0, 1);
  y ~ normal(y_hat, sigma_y);
}
"""


# In[5]:


hierarchical_intercept_data = {'N': len(main.index),
                          'J': len(n_country),
                          'country': country+1,
                          'u': u,
                          'x': main.gini_net.values,
                          'y': main.church2.values}

hierarchical_intercept_fit = pystan.stan(model_code=hierarchical_intercept, data=hierarchical_intercept_data, 
                                         iter=1000, chains=2)


# In[11]:


m_means = hierarchical_intercept_fit['m'].mean(axis=0)
plt.scatter(u, m_means)
g0 = hierarchical_intercept_fit['mu_a'].mean()
g1 = hierarchical_intercept_fit['b'][:, 0].mean()
xvals = np.linspace(0, 5)
plt.plot(xvals, g0+g1*xvals, 'k--')
plt.xlim(u.min(), u.max())

m_se = hierarchical_intercept_fit['m'].std(axis=0)
for ui, m, se in zip(u, m_means, m_se):
    plt.plot([ui,ui], [m-se, m+se], 'b-')
plt.xlabel('church'); plt.ylabel('Intercept estimate')


# In[12]:


# PART 2
hierarchical_intercept_2 = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] u;
  vector[N] x;
  vector[N] y;
} 
parameters {
  vector[J] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {
  vector[N] y_hat;
  vector[N] m;

  for (i in 1:N) {
    m[i] = a[country[i]] + u[i] * b[1];
    y_hat[i] = m[i] + x[i] * b[2];
  }
}
model {
  mu_a ~ normal(0, 10);
  a ~ normal(mu_a, sigma_a);
  b ~ normal(0, 1);
  y ~ normal(y_hat, sigma_y);
}
"""


# In[13]:


hierarchical_intercept_fit_2 = pystan.stan(model_code=hierarchical_intercept_2, data=hierarchical_intercept_data, 
                                         iter=1000, chains=2)


# In[15]:


m_means = hierarchical_intercept_fit_2['m'].mean(axis=0)
plt.scatter(u, m_means)
g0 = hierarchical_intercept_fit_2['mu_a'].mean()
g1 = hierarchical_intercept_fit_2['b'][:, 0].mean()
xvals = np.linspace(u.min(), u.max())
plt.plot(xvals, g0+g1*xvals, 'k--')
plt.xlim(u.min(), u.max())

m_se = hierarchical_intercept_fit_2['m'].std(axis=0)
for ui, m, se in zip(u, m_means, m_se):
    plt.plot([ui,ui], [m-se, m+se], 'b-')
plt.xlabel('church'); plt.ylabel('Intercept estimate')


# In[ ]:


# The standard error in the first model is less than the second one, though the second one is now more non-collinear

