import csv


def export_as_csv(file_path, results):
    columns = [
        "gain_vlf",
        "gain_lf",
        "gain_hf",
        "phase_vlf",
        "phase_lf",
        "phase_hf",
        "coherence_vlf",
        "coherence_lf",
        "coherence_hf",
        "gain_vlf_norm",
        "gain_lf_norm",
        "gain_hf_norm",
        "coherence_threshold_applied",
        "n_windows",
        "avg_abp",
        "avg_cbfv",
        "std_abp",
        "std_cbfv",
        "coherence_threshold",
    ]
    with open(file_path, "w") as fobj:
        w = csv.DictWriter(fobj, columns)
        w.writeheader()
        w.writerow({c: results[c] for c in columns})

