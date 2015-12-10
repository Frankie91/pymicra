from scipy import integrate
import pandas as pd
import numpy as np

def integrate_series(self, how='trapz', dateindex=False, **kwargs):
    '''
    Numerically a given series.

    @param how: the method to use (trapz by default)
    @return 

    Available methods:
     * trapz - trapezoidal
     * cumtrapz - cumulative trapezoidal
     * simps - Simpson's rule
     * romb - Romberger's rule

    See http://docs.scipy.org/doc/scipy/reference/integrate.html for the method details.
    or the source code
    https://github.com/scipy/scipy/blob/master/scipy/integrate/quadrature.py
    '''
    available_rules = set(['trapz', 'cumtrapz', 'simps', 'romb'])
    if how in available_rules:
        rule = integrate.__getattribute__(how)
    else:
        print('Unsupported integration rule: %s' % (how))
        print('Expecting one of these sample-based integration rules: %s' % (str(list(available_rules))))
        raise AttributeError
    if dateindex:
        result = rule(self.values, self.index.astype(np.int64), **kwargs)
    else:
        result = rule(self.values, self.index.astype(np.float64), **kwargs)
    return result


def integrate_df(self, how='trapz', dateindex=False, **kwargs):
    '''
    Numerically integrate a given dataframe

    @param how: the method to use (trapz by default)
    @return 

    Available methods:
     * trapz - trapezoidal
     * cumtrapz - cumulative trapezoidal
     * simps - Simpson's rule
     * romb - Romberger's rule

    See http://docs.scipy.org/doc/scipy/reference/integrate.html for the method details.
    or the source code
    https://github.com/scipy/scipy/blob/master/scipy/integrate/quadrature.py
    '''
    df=self.copy()
    available_rules = set(['trapz', 'cumtrapz', 'simps', 'romb'])
    if how in available_rules:
        rule = integrate.__getattribute__(how)
    else:
        print('Unsupported integration rule: %s' % (how))
        print('Expecting one of these sample-based integration rules: %s' % (str(list(available_rules))))
        raise AttributeError
    if dateindex:
        xaxis=df.index.astype(np.int64)
    else:
        xaxis=df.index.astype(np.float64)
    for c in df.columns:
        df[c] = rule(df[c].values, xaxis, **kwargs)
    if how in ['trapz', 'simps']:
        return df.iloc[0]
    else:
        return df
pd.Series.integrate = integrate_series
pd.DataFrame.integrate = integrate_df
