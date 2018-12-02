#import stuff....
from copy import deepcopy

def subset_MSO(MSO,Iupac_sequence):
    subMSO = {}
    found = False
    for motif in MSO['Motifs']:
        if motif['Iupac_sequence'] == Iupac_sequence:
            subMSO['Condition'] = MSO['Condition']
            subMSO['SequenceSet_ref'] = MSO['SequenceSet_ref']
            subMSO['Alphabet'] = deepcopy(MSO['Alphabet'])
            subMSO['Background'] = deepcopy(MSO['Background'])
            subMSO['Motifs'] = []
            subMSO.append(deepcopy(motif))
            found = True
            break
    if found:
        return subMSO
    return None
