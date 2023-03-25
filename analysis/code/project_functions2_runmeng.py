{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64769f12-2a61-4f65-92ef-e99f7e4dbbd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def process_soccer_data(url):\n",
    "    data = pd.read_csv(url)\n",
    "    df = (\n",
    "        pd.DataFrame(data=data)\n",
    "        .assign(spi1_spi2=lambda x: x['spi1'] - x['spi2'])\n",
    "        .assign(score1_score2=lambda x: x['score1'] - x['score2'])\n",
    "        .assign(ratio=lambda x: x['spi1_spi2'] / x['score1_score2'])\n",
    "        .loc[:, ['date','team1','team2','spi1','spi2','score1','score2','spi1_spi2','score1_score2','ratio']]\n",
    "        .reset_index(drop=True)\n",
    "    )\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7e4b382-5741-4a14-9d9f-607178f54a6f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
