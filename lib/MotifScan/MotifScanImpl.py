# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from installed_clients.KBaseReportClient import KBaseReport
from MotifFinderMEME.MotifFinderMEMEClient import MotifFinderMEME
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from MotifUtils.MotifUtilsClient import MotifUtils

#END_HEADER


class MotifScan:
    '''
    Module Name:
    MotifScan

    Module Description:
    A KBase module: MotifScan
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/arwyer/MotifScan.git"
    GIT_COMMIT_HASH = "ca00ed79535ad4751166dc52c8882395f36f68ef"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR
        pass


    def ScanGenomeForMotifs(self, ctx, params):
        """
        :param params: instance of type "ScanGenomeIn" (This example function
           accepts any number of parameters and returns results in a
           KBaseReport funcdef
           run_MotifScan(mapping<string,UnspecifiedObject> params) returns
           (ReportResults output) authentication required;) -> structure:
           parameter "genome_ref" of String, parameter "ws_name" of String,
           parameter "motifset_ref" of String
        :returns: instance of type "ScanGenomeOut" -> structure:
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN ScanGenomeForMotifs
        ws = Workspace('https://appdev.kbase.us/services/ws')
        ws_name = params['workspace_name']
        subset = ws.get_object_subset([{
                                     'included':['/assembly_ref'],
'ref':params['genome_ref']}])
        aref = subset[0]['data']['assembly_ref']
        assembly_ref = {'ref': aref}
        print('Downloading Assembly data as a Fasta file.')
        assemblyUtil = AssemblyUtil(self.callback_url)
        fasta_file = assemblyUtil.get_assembly_as_fasta(assembly_ref)
        scanFastaParams = {'fasta_path' : fasta_file['path'], 'motifset_ref' : params['motifset_ref'],'ws_name' : params['ws_name']}

        #build mast command with this -> fasta_file['path']
        #no way we can use this fasta to build report, too big

        #END ScanGenomeForMotifs

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method ScanGenomeForMotifs return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def ScanSequenceSetForMotifs(self, ctx, params):
        """
        :param params: instance of type "ScanSequenceSetIn" -> structure:
           parameter "ss_ref" of String, parameter "ws_name" of String,
           parameter "motifset_ref" of String
        :returns: instance of type "ScanSequenceSetOut" -> structure:
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN ScanSequenceSetForMotifs
        fastapath = '/kb/module/work/tmp/ToScan.fasta'
        MFM = MotifFinderMEME(self.callback_url)
        buildFastaParams = {'workspace_name' : params['ws_name'], 'SequenceSetRef' : params['ss_ref'], 'fasta_outpath' : fastapath  }
        MFM.BuildFastaFromSequenceSet(buildFastaParams)
        scanFastaParams = {'fasta_path' : fastapath, 'motifset_ref' : params['motifset_ref'],'ws_name' : params['ws_name']}
        self.ScanFastaForMotifs(scanFastaParams)

        #TODO: Make report
        #END ScanSequenceSetForMotifs

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method ScanSequenceSetForMotifs return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def ScanFastaForMotifs(self, ctx, params):
        """
        :param params: instance of type "ScanMotifsIn" -> structure:
           parameter "fasta_path" of String, parameter "motifset_ref" of
           String
        :returns: instance of type "ScanMotifsOut" -> structure: parameter
           "something" of String
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN ScanFastaForMotifs
        #use motifutils to download MSO as MEME
        MOU = MotifUtils(self.callback_url)
        MastFileName = 'MastTemp.txt'
        downloadMotifParams = {'source_ref' : params['motifset_ref'], 'format' : 'MEME', 'outname' : MastFileName,'ws_name' : params['ws_name']}
        memeMotifPath = MOU.DownloadMotifSet(downloadMotifParams)['destination_path']

        #use mast on meme + fasta
        #parse and report
        #create new MSO and add locations?
        #END ScanFastaForMotifs

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method ScanFastaForMotifs return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
