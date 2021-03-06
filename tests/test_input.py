from graditudelib import normalize
from graditudelib import visualizing_kinetics
from graditudelib import elbow_curve
from graditudelib import silhouette
from graditudelib import Nearest_Neighbors
from graditudelib import PCA_analysis
from graditudelib import scaling
from graditudelib import robust_regression
from graditudelib import histograms_of_fractions
from graditudelib import Clustering
from graditudelib import min_row_sum
from graditudelib import t_sne_colored_list_clustering_features
from graditudelib import correlation_between_genes
from graditudelib import modify_input
from graditudelib import selecting_ncRNAs
from graditudelib import plot_network_graph
from graditudelib import clustering_proteins
from graditudelib import t_sne_proteins_data
from graditudelib import interactive_tsne_plot


def test_run_modify_input():
    modify_input.filtering_input(
        '/home/silvia/work/GRADitude/data/gene_wise_quantifications_combined_extended.csv',
        'Locus_tag',
        '/home/silvia/work/GRADitude/data/read_alignment_stats.csv',
        100,
        'filtered_gene_wise_quantifications_combined_extended.csv',
        'filtered_alignment_stats.csv',
        'Grad_47_Fraction_00L_Rep_3')


def test_run_normalize():
    normalize.normalized_count_table(
        "../data/filtered_gene_wise_quantifications_combined_extended.csv",
        11,
        32,
        "../data/filtered_alignment_stats_with_correlated_ERCC.csv",
        1,
        22,
        "normalized_table_with_pellet.csv",
        "size_factor_table.csv",
    )


def test_run_visualizing_kinetics():
    visualizing_kinetics.plot_kinetics(
        "../data/k-means_Norm_MIN_ROW_SUM_100.csv_max_6cl.csv",
        'chiX',
        11)


def test_run_k_means_clustering():
    k_means.generate_k_means_clustering(
        "/home/silvia/work/GRADitude/tests/filtered_gene_wise_quantifications_combined_extended.csv",
        12,
        7,
        'normalized_by_log10_with_clusters.csv',
        'log10',
        1)


def test_run_elbow_method():
    elbow_curve.k_means_clustering_elbow(
        "../data/gene_wise_quantifications_combined_extended.csv",
        11,
        32,
        2,
        10,
        "output_1",
        "output_2")


def test_run_silhouette_analysis():
    silhouette.silhouette_analysis(
        "../data/gene_wise_quantifications_combined_extended.csv",
        11,
        2,
        10)


def test_run_hierarchical_clustering():
    hierarchical_clustering.generate_hierarchical_clustering(
        "../data/gene_wise_quantifications_combined_extended_test.csv",
        12,
        7,
        'normalized_by_log10_with_clusters_hierarchical.csv',
        'log10',
        1)


def test_run_db_scan_clustering():
    DBSCAN_clustering.generate_dbscan_clustering("../data/gene_wise_quantifications_combined_extended_test.csv",
                                                 12,
                                                 'no_normalized_DBSCAN.csv',
                                                 'no_normalization',
                                                 1)


def test_run_nearest_neighbors():
    Nearest_Neighbors.generate_nearest_neighbors("../data/gene_wise_quantifications_combined_extended_test.csv",
                                                 12)


def test_run_pca():
    PCA_analysis.pca('../data/gene_wise_quantifications_combined_extended_test.csv',
                     12,
                     'test.csv',
                     'output_plot')


def test_run_t_sne_analysis():
    tSNE.t_sne_analysis("../data/normalized_by_log10_with_clusters_DBSCAN.csv",
                        12,
                        'with_cluster',
                        'test')


def test_run_scaling():
    scaling.scaling_('../data/gene_wise_quantifications_combined_extended.csv',
                     12,
                     1,
                     'normalized_to_max',
                     'test.csv')


def test_run_robust_regression():
    robust_regression.robust_regression("../data/filtered_alignment_stats_MIN_ROW_SUM_100.csv",
                                        "../data/cms_095046.txt",
                                        20, 18,
                                        4,
                                        'filtered_alignment_stats_with_correlated_ERCC.csv')


def test_run_histograms_of_fractions():
    histograms_of_fractions.plot_histograms('../output/filtered_gene_wise_quantifications_combined_extended.csv',
                                            11)


def test_clustering():
    Clustering.clustering('../data/gene_wise_quantifications_combined_extended.csv',
                          12,
                          6,
                          1,
                          'K-means',
                          "normalized_to_range",
                          "test.csv")


def test_run_min_row_sum():
    min_row_sum.exclude_the_min_row_sum("../data/filtered_gene_wise_quantifications_combined_extended.csv", 10,
                                        0,
                                        'gene_wise_combined_0_min_row_sum.csv')


def test_run_t_sne_colored_list_clustering_features():
    t_sne_colored_list_clustering_features.t_sne(
        "/home/silvia/work/GRADitude/data/k-meansNorm_MIN_ROW_SUM_100_ncRNA.csv_max_3_cl.csv",
        11, 30,
        'output1.html',
        'output2.html')


def test_run_umap_analysis():
    UMAP_analysis.umap_("../data/k-meansNorm_MIN_ROW_SUM_100_ncRNA.csv_max_3_cl.csv",
                        11,
                        'output1_test',
                        'output2_test')


def test_run_correlation():
    correlation_between_genes.correlation("../tests/normalized_by_log10_with_clusters.csv", 11,
                                          'hist.png')


def test_run_selecting_ncRNAs():
    selecting_ncRNAs.selecting_specific_features("../data/gene_wise_quantifications_combined_extended.csv",
                                                 11, 'ncRNA', 'test.csv')


def test_run_ploth_graph():
    plot_network_graph.plot_network_graph_rna_protein("../output/correlated_table_test.csv", float(0.4), 10,
                                                      'test.html')


def test_clustering_protein():
    clustering_proteins.clustering("../data/modified_proteinGroups_No612_20180119.0755_pgFilt4.csv", 24, 43,
                                   6, 'k-means', 'test.csv')


def test_t_sne_proteins():
    t_sne_proteins_data.t_sne_pr("../tests/test.csv", 24, 30, 'test.html')


def test_interactive_plot():
    interactive_tsne_plot.interactive_plot("../data/k-meansNorm_MIN_ROW_SUM_100_ncRNA.csv_max_3_cl.csv", 11,
                                           "output.html")


# test_run_modify_input()
# test_run_normalize()
# test_run_visualizing_kinetics()
# test_run_k_means_clustering()
test_run_elbow_method()
# test_run_silhouette_analysis()
# test_run_hierarchical_clustering()
# test_run_db_scan_clustering()
# test_run_nearest_neighbors()
# test_run_pca()
# test_run_t_sne_analysis()
# test_run_scaling()
# test_run_robust_regression()
# test_run_histograms_of_fractions()
# test_clustering()
# test_run_min_row_sum()
# test_run_t_sne_colored_list_clustering_features()
# test_run_correlation()
# test_run_umap_analysis()
# test_run_selecting_ncRNAs()
# test_run_ploth_graph()
# test_clustering_protein()
# test_t_sne_proteins()
# test_t_sne_list()
# test_interactive_plot()
