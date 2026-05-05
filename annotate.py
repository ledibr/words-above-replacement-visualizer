import pandas as pd


def annotate_metadata(size: str = '10k'):
    with open('metadata/player_list.txt', 'r', encoding='utf-8') as f:
        players = [line.strip() for line in f]

    if size != '10k' or size != '12k':
        size = '10k'
    metadata_path = f'oss_data/war_word2vec_{size}_metadata.tsv'
    metadata_df = pd.read_csv(metadata_path, encoding='utf-8', sep='\t', names=['word'])
    wordcount_df = pd.read_csv(f'metadata/word_counts_{size}.csv', encoding='utf-8')
    batter_df = pd.read_csv(f'metadata/batter_stats_calc.csv', encoding='utf-8', header=0, names=['word', 'position', 'team'], usecols=[0, 1, 3])
    pitcher_df = pd.read_csv(f'metadata/pitcher_stats_calc.csv', encoding='utf-8', header=0, names=['word', 'position', 'team'], usecols=[0, 1, 3])
    player_df = pd.concat([batter_df, pitcher_df])

    metadata_df['type'] = ['player' if w in players else 'word' for w in metadata_df['word']]
    metadata_df = pd.merge(metadata_df, wordcount_df, how='left', on='word')
    metadata_df = pd.merge(metadata_df, player_df, how='left', on='word')

    metadata_df.to_csv(metadata_path, sep='\t', index=False, mode='w', encoding='utf-8')


if __name__ == '__main__':
    annotate_metadata('10k')