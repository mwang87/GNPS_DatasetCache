run-local:
	nextflow run calculate_spectra_detail.nf

run-conda-cluster-test:
	nextflow run -with-conda '/Users/miw023/miniconda3/envs/ming_research' calculate_spectra_detail.nf -resume --files "/data/massive/MSV000084286/**/*.mzML"

run-conda-cluster-test-grid:
	nextflow run -c cluster.config calculate_spectra_detail.nf '/Users/miw023/miniconda3/envs/ming_research' calculate_spectra_detail.nf -resume --files "/data/massive/MSV000084286/**/*.mzML"

run-conda-cluster-full-mzml:
	nextflow run -with-conda '/Users/miw023/miniconda3/envs/ming_research' calculate_spectra_detail.nf -with-report "nf_report.html" -with-trace "nf_trace.html" -resume --files "/data/massive/public/**/*.mzML"

run-conda-cluster-full-mzml-grid:
	nextflow run -c cluster.config calculate_spectra_detail.nf -with-report "nf_report.html" -with-trace "nf_trace.html" -resume --files "/data/massive/public/**/*.mzML"

run-conda-cluster-full-mzxml:
	nextflow run -with-conda '/Users/miw023/miniconda3/envs/ming_research' calculate_spectra_detail.nf -with-report "nf_report.html" -with-trace "nf_trace.html" -resume --files "/data/massive/public/**/*.mzXML"

run-conda-cluster-full-mzxml-grid:
	nextflow run -c cluster.config calculate_spectra_detail.nf -with-report "nf_report.html" -with-trace "nf_trace.html" -resume --files "/data/massive/public/**/*.mzXML"