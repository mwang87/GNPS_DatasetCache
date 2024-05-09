#!/usr/bin/env nextflow
nextflow.enable.dsl=2

params.mtblstoken = ""

TOOL_FOLDER = "$baseDir/bin"

process mwbFiles {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    val x

    output:
    file 'MWBFilePaths_ALL.tsv'

    """
    python $TOOL_FOLDER/getAllWorkbench_file_paths.py \
    --study_id ALL \
    --output_path MWBFilePaths_ALL.tsv
    """
}

process mtblsFiles {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    val x

    output:
    file 'MetabolightsFilePaths_ALL.tsv'

    """
    python $TOOL_FOLDER/getAllMetabolights_file_paths.py \
    --output_filename "MetabolightsFilePaths_ALL.tsv" \
    --user_token $params.mtblstoken
    """
}

workflow {
    mwbFiles(1)
    mtblsFiles(1)
}
