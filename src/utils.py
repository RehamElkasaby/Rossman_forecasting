import matplotlib.pyplot as plt
def plot_time_series(time, values, title="Time Series Plot", labels="Values", xlabel="Time", ylabel="Values", grid=True, figsize=(10, 6), legend=False, ylim=None):
    """A function to plot single or multiple time series

    Args:
        time (_type_): time series data
        values (_type_): the variable to be tracked
        title (str, optional): title of the plot. Defaults to "Time Series Plot".
        labels (str, optional): _description_. Defaults to "Values".
        xlabel (str, optional): _description_. Defaults to "Time".
        ylabel (str, optional): _description_. Defaults to "Values".
        grid (bool, optional): _description_. Defaults to True.
        figsize (tuple, optional): _description_. Defaults to (10, 6).
        legend (bool, optional): _description_. Defaults to False.
        ylim (_type_, optional): _description_. Defaults to None.
    """
    plt.figure(figsize=figsize)

    if not isinstance(values, list): # Single time series
        
        if isinstance(labels, list):
            label = labels[0] if labels else None
        else:
            label = labels

        plt.plot(time, values, label=label)
        
        if label and legend:
            plt.legend()
    else:
        # Multiple time series
        num_series = len(values)
        if isinstance(labels, str):
            labels = [f"{labels} {i+1}" for i in range(num_series)]
        for i in range(num_series):
            plt.plot(time, values[i], label=labels[i])

        if legend:
            plt.legend()

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if grid:
        plt.grid(True)
    if ylim:
        if len(ylim) == 2:
            plt.ylim(ylim)
        else:
            print("Warning: 'ylim' should be a list or tuple of two numbers (min, max). Ignoring ylim.")
    plt.tight_layout()
    plt.show()