#!/usr/bin/env python

# Performs inflection of Czech nouns (specialized to out-of-vocabulary words)
#
# Dependency: OpenNMT-py==3.0.4
#
# Example run: python3 inflect.py
# jablko
# jablko	jablka	jablku	jablko	jablko	jablku	jablkem	jablka	jablek	jablkům	jablka	jablka	jablkách	jablky
# 
# Example of incorrect prediction:
# pes
# pes	pesu	psi	pes	pese	psi	psem	psi	psů	psům	pse	psi	pesech	psi


from argparse import Namespace
from onmt.bin.translate import translate

import sys
import os
import datetime
import random


#| Directory structure
#|
#|- requirements.txt
#|- inflect.py
#|- models
#|   |- model_released.pt
#|- tmp 
#|   |- tmp_datetime.src
#|   |- tmp_datetime.tgt


model_path = "models/lstm_v0.44.pt"
inp=["jablko", "bagr", "altruista", "internetíř", "lingebra"]

def __get_true_path_to_base():
    def removesuffix(x, suf):
        return x[:-len(suf)]
    
    suffix = "inflect.py"

    # Get full path to this `inflect.py` script
    file_path = os.path.realpath(__file__)

    base_dir = removesuffix(file_path, suffix)

    return base_dir

def rand():
    return str(random.randint(100_000, 999_999))

def get_curtime_str():
    return str(datetime.datetime.utcnow()).replace(" ", "_")

def get_tmpfilenames():
    base = __get_true_path_to_base()
    tmpdir = os.path.join(base, "tmp")

    os.makedirs(tmpdir, exist_ok=True)

    fn = f"{get_curtime_str()}_{rand()}.tmp"
    srcfn = fn + ".src"
    tgtfn = fn + ".tgt"

    src = os.path.join(tmpdir, srcfn)
    tgt = os.path.join(tmpdir, tgtfn)
    

    return src, tgt
    


def writelines(lines,filename):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")
            
def readlines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]
    
def convert2neural(lemmata):
    """Convert list of lemmata to list of inputs for NN for prediction
    """
    lines = []

    for lemma in lemmata:
        # Convert to specific neural format
        
        line = " ".join(lemma) #.replace("   ", " <SPACE> ")
        
        lines += [line + f" # S {i}" for i in range(1,7+1)] + [line + f" # P {i}" for i in range(1,7+1)]
    
    return lines
def convertFromNeural(predictions, original_lemmata):
    count = 14

    if len(predictions) != count * len(original_lemmata):
        raise Exception("Prediction failed, produced insufficient number of predictions.")
    
    allforms = ["".join(p.split(" ")) for p in predictions]
    
    
    
    inflected_lemmata = [allforms[count*i : count*(i+1)] for i in range(len(original_lemmata))]

    return inflected_lemmata



def inflect(lemmata):
    """
    `lemmata` can be either string (one lemma) or list of strings (list of lemmata)
    """

    if type(lemmata) == str:
        ONLY_ONE_LEMMA = True
        lemmata = [lemmata]
    else:
        ONLY_ONE_LEMMA = False
    
    lines = convert2neural(lemmata)

    # generate tmp filenames
    filename_in, filename_out = get_tmpfilenames()
    
    writelines(lines, filename_in)
    _inflect_file(filename_in, filename_out, model_path)
    predictions = readlines(filename_out)

    #try:
    os.remove(filename_in)
    os.remove(filename_out)
    #except OSError as e:
    # If it fails, inform the user.
    # #print("Warning: Failed to remove the tmp files in folder tmp/")
    #print("Please, remove them manually")
    
    # Convert from neural format back to normal text 
    inflected_lemmata = convertFromNeural(predictions,lemmata)
    
    if ONLY_ONE_LEMMA:
        return inflected_lemmata[0]
    else:
        return inflected_lemmata

def _inflect_file(fnin, fnout, model_path):
    """Run inflection on the specified input file content and write the
    predictions to the specified output file."""
    opt = Namespace(align_debug=False, alpha=1.0, attn_debug=False, avg_raw_probs=False, ban_unk_token=False, batch_size=30, batch_type='sents', beam_size=5, beta=-0.0, block_ngram_repeat=0, config=None, coverage_penalty='none', data_type='text', decoder_start_token='<s>', dump_beam='', fp32=False, fuzzy_corpus_ratio=0.1, fuzzy_threshold=70, fuzzy_token='｟fuzzy｠', fuzzymatch_max_length=70, fuzzymatch_min_length=4, gpu=-1, ignore_when_blocking=[], insert_ratio=0.0, int8=False, length_penalty='avg', log_file='', log_file_level='0', mask_length='subword', mask_ratio=0.0, max_length=250, min_length=0, models=[model_path], n_best=1, norm_numbers=True, norm_quote_commas=True, output=fnout, penn=True, permute_sent_ratio=0.0, phrase_table='', poisson_lambda=3.0, post_remove_control_chars=False, pre_replace_unicode_punct=False, prior_tokenization=False, random_ratio=0.0, random_sampling_temp=1.0, random_sampling_topk=0, random_sampling_topp=0.0, ratio=-0.0, replace_length=-1, replace_unk=False, report_align=False, report_time=False, reversible_tokenization='joiner', rotate_ratio=0.0, save_config=None, seed=-1, src=fnin, src_feats=None, src_lang='', src_onmttok_kwargs="{'mode': 'none'}", src_prefix='', src_seq_length=192, src_subword_alpha=0, src_subword_model=None, src_subword_nbest=1, src_subword_type='none', src_subword_vocab='', src_suffix='', src_vocab_threshold=0, stepwise_penalty=False, switchout_temperature=1.0, tgt=None, tgt_file_prefix=False, tgt_lang='', tgt_onmttok_kwargs="{'mode': 'none'}", tgt_prefix='', tgt_seq_length=192, tgt_subword_alpha=0, tgt_subword_model=None, tgt_subword_nbest=1, tgt_subword_type='none', tgt_subword_vocab='', tgt_suffix='', tgt_vocab_threshold=0, tm_delimiter='\t', tm_path=None, tokendrop_temperature=1.0, tokenmask_temperature=1.0, transforms=[], upper_corpus_ratio=0.01, verbose=False, with_score=False)
    
    # Suppress stderr for translation    
    save_stdout = sys.stderr
    sys.stderr = open(os.devnull, "w")
    
    translate(opt)
    
    sys.stderr = save_stdout
    

if __name__ == "__main__":
    print("Enter a lemma to be inflected:", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if line !="":
            print("\t".join(inflect(line)))
            print("", file=sys.stderr)
            print("Enter a lemma to be inflected:", file=sys.stderr)

