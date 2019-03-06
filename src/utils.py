import pandas as pd
import numpy as np
import re


class WikiMoviePlots():
    
    DATA_DIR = "../data/"
    DATA_FILENAME = "wiki_movie_plots_deduped.csv"
    
    def _read_data(self):
        self.data = pd.read_csv(self.DATA_DIR + self.DATA_FILENAME)
        self.data.reset_index(inplace=True, drop=False)
        self.data.rename(columns={'index': 'movie_id', 
                                  'Genre':'genre', 'Plot':'plot'}, 
                         inplace=True)
        self.data['movie_id'] = 'M_' + self.data.movie_id.astype(str)
        return
    
    def __init__(self):
        self._read_data()
        return

    
    def _split_it(self, x):
        return re.findall(r"[\w']+", x)
    
    def _split_genres(self):
        self.plot_data['genres'] = self.plot_data['genre'].apply(self._split_it)
        del self.plot_data['genre']
        return
    
    def _drop_rows(self, drop_at):
        ## Dropping all the rows for now, to clean the data.
        ## In future, can work on making this function more complicated
        ## Proposed logic: Drop only uncommon words from the genre list
        self.plot_data['genre_len'] = self.plot_data['genres'].apply(len)
        self.plot_data = self.plot_data[self.plot_data['genre_len'] < drop_at]
        del self.plot_data['genre_len']
        return
    
    def get_plot_data(self, genre_split=True, drop_at=5):
        plot_cols = ['movie_id', 'genre', 'plot']
        self.plot_data = self.data[plot_cols]
        
        if genre_split:
            self._split_genres()
            
            if drop_at is None:
                return self.plot_data
            else:
                self._drop_rows(drop_at)
        
        return self.plot_data
    
