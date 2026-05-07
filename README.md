# Words Above Replacement Visualizer

This repository contains the files used to build the TensorBoard Projector
visualization of the embeddings presented in [Words Above Replacement](https://github.com/ledibr/words-above-replacement).
The projector can be accessed at https://ledibr.github.io/words-above-replacement-visualizer/.

The following information is presented for documentation purposes; no code in this
repository is intended to be run by users, as it is primarily backend
for the projector site.

## Repository Contents

- `annotate.py`: Script used to annotate metadata files with fields described in [Metadata](#metadata) below.
- `oss_data`: Contains projector config file, tensor files, and metadata files (unannotated and annotated).
- `metadata`: Contains files with info for metadata fields, used to annotate metadata files.

## Tensors

- **WAR Word2Vec 10K:** Embeddings of 10k most frequent words in the model vocabulary.
- **WAR Word2Vec 12K:** Embeddings of 12k most frequent words in the model vocabulary.
- **WAR Word2Vec Players + Target Words:** Embeddings of studied player set (141 players)
  as well as all "interest words" (256 words).

## Metadata

Each embedding is associated with several metadata fields that can be used as labels
or color categories in the projector.
- **word:** The token corresponding to the embedding.
- **type:** Whether the token is an entity (player) or a non-entity word.
- **count:** The count of the token in the corpus.

  The following two fields are exclusive to entities; non-entities have a value of 'N/A'.
  (Coloring by these fields is most useful when using the "WAR Word2Vec Players + Target Words" tensors 
  or isolating all entity embeddings using 'Search by type' → 'player'.)

- **position:** The primary position of the player.
- **team:** The primary team of the player.