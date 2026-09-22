def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    # Write code here
    smoothed_list = []
    
    b0 = series[1]-series[0]
    l0 = series[0]

    b_list = [b0]
    smoothed_list.append(l0)
    
    for i, s in enumerate(series[1::]):
        l = (alpha*s) + (1 - alpha)*(smoothed_list[i]+b_list[i])
        b = beta*(l-smoothed_list[i])+(1-beta)*(b_list[i])
        
        smoothed_list.append(l)
        b_list.append(b)

    return smoothed_list