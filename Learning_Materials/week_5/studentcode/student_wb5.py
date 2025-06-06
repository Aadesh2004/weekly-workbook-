# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
    ----------
    datafile_name: str
        path to data file

    K: int
        number of clusters to use

    feature_names: list
        list of feature_names

    Returns
    ---------
    fig: matplotlib.figure.Figure
        the figure object for the plot

    axs: matplotlib.axes.Axes
        the axes object for the plot
    """
    # ====> insert your code below here
    # Load data
    data_array = np.genfromtxt(datafile_name, delimiter=',')



    # Main clustering
    main_cluster_model = KMeans(n_clusters=K, n_init=10)
    main_cluster_model.fit(data_array)
    cluster_labels = main_cluster_model.predict(data_array)



    # Create plot grid
    num_features = data_array.shape[1]
    fig, ax = plt.subplots(num_features, num_features, figsize=(12, 12))
    plt.set_cmap('viridis')

    # Colors for histograms
    hist_colors = plt.get_cmap('viridis', K).colors

    # Loop through feature pairs
    feat1 = 0
    while feat1 < num_features:
        ax[feat1, 0].set_ylabel(feature_names[feat1])
        ax[0, feat1].set_xlabel(feature_names[feat1])
        ax[0, feat1].xaxis.set_label_position('top')

        feat2 = 0
        while feat2 < num_features:
            plot_data_x = data_array[:, feat1].copy()
            plot_data_y = data_array[:, feat2].copy()

            # Sort data
            order_idx = np.argsort(cluster_labels)
            ordered_x = plot_data_x[order_idx]
            ordered_y = plot_data_y[order_idx]

            if feat1 != feat2:
                ax[feat1, feat2].scatter(ordered_x, ordered_y, c=cluster_labels, s=50, marker='^', edgecolor='black', alpha=0.7)
            else:
                hist_idx = np.argsort(cluster_labels)
                hist_data = plot_data_x[hist_idx]
                hist_labels = cluster_labels[hist_idx]

                split_indices = np.unique(hist_labels, return_index=True)[1][1:]
                data_splits = np.split(hist_data, split_indices)

                k = 0
                while k < K:
                    ax[feat1, feat2].hist(data_splits[k], bins=20, color=hist_colors[k], edgecolor='black', alpha=0.7)
                    k += 1

            feat2 += 1
        feat1 += 1

    # Set title
    user_name = "a8-bhandari (Aadesh Bhandari)" # Replace with your UWE username
    fig.suptitle(f'Visualisation of {K} clusters by {user_name}', fontsize=16, y=0.925)

    # Save plot
    fig.savefig('myVisualisation.jpg')

    return fig, ax
    # <==== insert your code above here
