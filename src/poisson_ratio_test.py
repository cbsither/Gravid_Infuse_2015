import numpy as np
import scipy.stats as stats

"""
The following code is from: https://stackoverflow.com/questions/33944914/implementation-of-e-test-for-poisson-in-python

These functions are implemented in the statsmodel package now but I'd rather not change the original analysis script
"""

def _zstat_generic2(value, std_diff, alternative):
    '''generic (normal) z-test to save typing

    can be used as ztest based on summary statistics
    '''
    zstat = value / std_diff
    if alternative in ['two-sided', '2-sided', '2s']:
        pvalue = stats.norm.sf(np.abs(zstat))*2
    elif alternative in ['larger', 'l']:
        pvalue = stats.norm.sf(zstat)
    elif alternative in ['smaller', 's']:
        pvalue = stats.norm.cdf(zstat)
    else:
        raise ValueError('invalid alternative')
    return zstat, pvalue

def poisson_twosample(count1, exposure1, count2, exposure2, ratio_null=1,
                      method='score', alternative='2-sided'):
    '''test for ratio of two sample Poisson intensities

    If the two Poisson rates are g1 and g2, then the Null hypothesis is

    H0: g1 / g2 = ratio_null

    against one of the following alternatives

    H1_2-sided: g1 / g2 != ratio_null
    H1_larger: g1 / g2 > ratio_null
    H1_smaller: g1 / g2 < ratio_null

    Parameters
    ----------
    count1: int
        Number of events in first sample
    exposure1: float
        Total exposure (time * subjects) in first sample
    count2: int
        Number of events in first sample
    exposure2: float
        Total exposure (time * subjects) in first sample
    ratio: float
        ratio of the two Poisson rates under the Null hypothesis. Default is 1.
    method: string
        Method for the test statistic and the p-value. Defaults to `'score'`.
        Current Methods are based on Gu et. al 2008
        Implemented are 'wald', 'score' and 'sqrt' based asymptotic normal
        distribution, and the exact conditional test 'exact-cond', and its mid-point
        version 'cond-midp', see Notes
    alternative : string
        The alternative hypothesis, H1, has to be one of the following

           'two-sided': H1: ratio of rates is not equal to ratio_null (default)
           'larger' :   H1: ratio of rates is larger than ratio_null
           'smaller' :  H1: ratio of rates is smaller than ratio_null

    Returns
    -------
    stat, pvalue two-sided

    not yet
    #results : Results instance
    #    The resulting test statistics and p-values are available as attributes.


    Notes
    -----
    'wald': method W1A, wald test, variance based on separate estimates
    'score': method W2A, score test, variance based on estimate under Null
    'wald-log': W3A
    'score-log' W4A
    'sqrt': W5A, based on variance stabilizing square root transformation
    'exact-cond': exact conditional test based on binomial distribution
    'cond-midp': midpoint-pvalue of exact conditional test

    The latter two are only verified for one-sided example.

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008

    '''

    # shortcut names
    y1, n1, y2, n2 = count1, exposure1, count2, exposure2
    d = n2 / n1
    r = ratio_null
    r_d = r / d

    if method in ['score']:
        stat = (y1 - y2 * r_d) / np.sqrt((y1 + y2) * r_d)
        dist = 'normal'
    elif method in ['wald']:
        stat = (y1 - y2 * r_d) / np.sqrt(y1 + y2 * r_d**2)
        dist = 'normal'
    elif method in ['sqrt']:
        stat = 2 * (np.sqrt(y1 + 3 / 8.) - np.sqrt((y2 + 3 / 8.) * r_d))
        stat /= np.sqrt(1 + r_d)
        dist = 'normal'
    elif method in ['exact-cond', 'cond-midp']:
        from statsmodels.stats import proportion
        bp = r_d / (1 + r_d)
        y_total = y1 + y2
        stat = None
        pvalue = proportion.binom_test(y1, y_total, prop=bp, alternative=alternative)
        if method in ['cond-midp']:
            # not inplace in case we still want binom pvalue
            pvalue = pvalue - 0.5 * stats.binom.pmf(y1, y_total, bp)

        dist = 'binomial'

    if dist == 'normal':
        return _zstat_generic2(stat, 1, alternative)
    else:
        return stat, pvalue


def power_analysis(count1, exposure1, count2, exposure2,
                   beta_, alpha_, ratio_null, ratio_null_exp, t_units, method='score'):
    """
    Power analysis from Gu, K., Ng, H. K. T., Tang, M. L., & Schucany, W. R. (2008). Testing the ratio of two poisson
	rates. Biometrical Journal: Journal of Mathematical Methods in Biosciences, 50(2), 283-298.

    :param count1: int
        Number of events in first sample
    :param exposure1: float
        Total exposure (time * subjects) in first sample
    :param count2: int
        Number of events in first sample
    :param exposure2: float
        Total exposure (time * subjects) in first sample
    :param ratio_null: the null hypothesis defined by the expected lambda ratios given no effect
    :param _beta: type 2 error
    :param _alpha: type I error
    :param t0: first sample interval
    :param t1: maximum sample interval
    :return:
    """
    d = count1 / count2
    z_beta = 1 - beta_
    z_alpha = 1 - alpha_
    rho = ratio_null / d
    c_ = ratio_null / ratio_null_exp

    if method in ['score']:
        lambda_1 = (((c_ / rho) + c_**2)*((z_alpha + z_beta)**2)) / ((1 - c_)**2)
    elif method in ['wald']:
        lambda_1 = (((c_ / rho) + c_**2) *
                    (z_alpha * np.sqrt((c_ + rho)/(1 + (c_ * rho))) + z_beta)**2) / ((1 - c_)**2)
    elif method in ['sqrt']:
        lambda_1 = (((c_ / rho) + 1)*((z_alpha + z_beta)**2)) / (np.log(c_)**2)
    elif method in ['exact-cond']:
        lambda_1 = (((c_ / rho) + 1) *
                    (z_alpha * (np.sqrt(c_ * (rho**2 + 2*rho + 1)) / (c_ + rho)) + z_beta)**2) / (np.log(c_)**2)
    elif method in ['cond-midp']:
        lambda_1 = ((z_alpha*np.sqrt((c_/rho)+c_)+z_beta*np.sqrt(1 + (c_/rho))) / (2*(1-np.sqrt(c_))))**2 - (3/8)

    #t_units = np.arange(1, 100)

    exp_lambda_1 = lambda_1

    lambda_1_est = count1 / exposure1
    lambda_2_est = count2 / exposure2

    return exp_lambda_1

