import numpy as np

def pseudoinv_regression(design, obs):
    pseudoinv = np.linalg.inv(design.transpose() @ design)
    weights = pseudoinv @ design.transpose() @ obs
    predictions = design @ weights

    rss = sum((obs - predictions) ** 2)

    return (weights, predictions, rss)

def cross_validate_model(design, obs):
    rss = 0
    for i in range(len(design)):
        loo_design = np.delete(design, i, axis=0)
        loo_obs = np.delete(obs, i)
        weights, _ = pseudoinv_regression(loo_design, loo_obs)
        left_out_prediction = design[i] @ weights
        actual = obs[i]
        residual_sq = (left_out_prediction - actual) ** 2
        rss += residual_sq

    return rss

if __name__ == "__main__":
    data = [(0, 0),(1, 10),(2, 20),(3, 50),(4, 35),(5, 100),
    (6, 110),(7, 190),(8, 150),(9, 260),(10, 270)]

    x_values = list(map(lambda p: p[0], data))
    y_values = list(map(lambda p: p[1], data))
    obs = np.array(y_values)

    #linear regression
    x = np.array(x_values)
    ones = np.array([1] * x.size)
    design = np.vstack((ones, x)).transpose()
    predictions = pseudoinv_regression(design, obs)
    rss = cross_validate_model(design, obs)
    print(rss)

    #quadratic polynomial
    squares = x ** 2
    design = np.vstack((ones, x, squares)).transpose()
    rss = cross_validate_model(design, obs)
    print(rss)

    #8th-degree polynomial
    design = np.array([(x ** i) for i in range(9)]).transpose()
    rss = cross_validate_model(design, obs)
    print(rss)