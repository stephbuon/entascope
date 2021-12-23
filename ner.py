import pickle
import sys
import os
import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'lemmatizer', 'tagger'])

def extract_named_entity(sentence):
    return [str(entity.text) for entity in sentence.ents]   
    # return [(entity.text, entity.label_) for entity in sentence.ents]   
    
def extract_named_entity_category(sentence):
    return [str(entity.label_) for entity in sentence.ents]

def export_named_entities(data, extraction_col, arg1):

    data[extraction_col] = data[extraction_col].astype(str)
    data['parsed_text'] = list(nlp.pipe(data[extraction_col]))
    data['named_entities'] = data['parsed_text'].apply(extract_named_entity)
    data['named_entity_category'] = data['parsed_text'].apply(extract_named_entity_category)

    #data = data[data['named_entities'].map(bool)]

    print(data)

    #if not data.empty:
    #    handle = open(os.path.basename(arg1) + '.pickle', 'wb')
    #    pickle.dump(data, handle)
    #    print('Finished and saved pickle')
    #else:
    #    print('Finish and no pickled data produced')
    #    exit()

#arg1 = sys.argv[1]
arg1 = '/home/stephbuon/projects/a.csv'
data = pd.read_csv(arg1)
export_named_entities(data, 'sentence', arg1)