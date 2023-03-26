import pandas as pd

def load_and_process(url):
    data = pd.read_csv(url)
    df = (
        pd.DataFrame(data=data)
        .assign(spi1_spi2=lambda x: x['spi1'] - x['spi2'])
        .assign(score1_score2=lambda x: x['score1'] - x['score2'])
        .assign(ratio=lambda x: x['spi1_spi2'] / x['score1_score2'])
        .loc[:, ['date','team1','team2','spi1','spi2','score1','score2','spi1_spi2','score1_score2','ratio']]
        .reset_index(drop=True)
    )
    return df