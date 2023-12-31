# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['isna', 'isya', 'n_in_cols', 'n_in_rows', 'counts_sorted']

# %% ../nbs/00_core.ipynb 10
def isna(df): return df.isna()
def isya(df): return df.isna() == False
def n_in_cols(df): return df.sum()
def n_in_rows(df): return df.sum(axis=1)
def counts_sorted(s): return s.value_counts(sort=False).sort_index()

n_in_cols(isna(df))

