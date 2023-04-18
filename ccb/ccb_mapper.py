import text2term
import pandas as pd
import string


print("Starting caching the ontology")
#cache the ontology
text2term.cache_ontology("http://purl.obolibrary.org/obo/cl.owl", "CL")
print("Cache geladen")

print("preprocessing the csv file")

#opening the csv file
df_csv = pd.read_csv('cell_annotations_in_sc_heart_atlases - cell_annotations.csv')

#drop nans
df_csv = df_csv.dropna(subset=['celltypes'])

#getting celltypes, removing the punctuation and convert it to a list
celltypes = df_csv['celltypes'].str.replace('[{}]'.format(string.punctuation), '').tolist()


print("preprocessing ended")
print("List: ", celltypes)


print("")
print("start mapping")
#map the two terms
df = text2term.map_terms(celltypes, "CL", output_file="ccb/mapping.txt", save_mappings=True, use_cache=True)

print("mapping complete")

#df.info()

#clear the cache
text2term.clear_cache("CL")