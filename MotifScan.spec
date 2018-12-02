/*
A KBase module: MotifScan
*/

module MotifScan {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport

    funcdef run_MotifScan(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    */

    typedef structure{
      string genome_ref;
      string ws_name;
      string motifset_ref;
    } ScanGenomeIn;

    typedef structure{
      string report_name;
      string report_ref;
    } ScanGenomeOut;

    typedef structure{
      string ss_ref;
      string ws_name;
      string motifset_ref;
    } ScanSequenceSetIn;

    typedef structure{
      string report_name;
      string report_ref;
    } ScanSequenceSetOut;

    typedef structure{
      string fasta_path;
      string motifset_ref;
      string ws_name;
    } ScanMotifsIn;

    typedef structure{
      string out_motifset_ref;
    } ScanMotifsOut;


    funcdef ScanFastaForMotifs(ScanMotifsIn params)
      returns (ScanMotifsOut out) authentication required;

    funcdef ScanGenomeForMotifs(ScanGenomeIn params)
      returns (ScanGenomeOut out) authentication required;

    funcdef ScanSequenceSetForMotifs(ScanSequenceSetIn params)
      returns (ScanSequenceSetOut out) authentication required;




    /*
    functions we need here -
    subset MSO -> need this to get individual motifs

    */

};
