import click
import pandas as pd
import random

from fancyimpute import KNN
from sklearn import preprocessing

@click.command()
@click.option("--k", default=10, help="The K in KNN")
@click.argument('file')
def impute(k, file):
    """  
    transpose (such that samples are rows)
    standard scale
    KNN impute (k=10)
    inverse transform
    untranspose
    """

    try:
        # Load data
        print("Loading data..")
        data = pd.read_csv(file, sep='\t', header=0, index_col=0, error_bad_lines=False)
        data.set_index('Gene', inplace=True)
        new_data = data.copy()

        # Transpose
        print("Transposing..")
        transposed = new_data.transpose()

        # Scale
        print("Scaling..")
        scaler = preprocessing.StandardScaler(copy=True)
        scaler.fit(transposed)
        scaled = pd.DataFrame(  scaler.transform(transposed),
                                index=transposed.index,
                                columns=transposed.columns
                            )
        # Impute
        print("Imputing..")
        imputed = KNN(k=k, print_interval=1).fit_transform(scaled)

        # Inverse Transform
        print("Inverse Transforming..")
        inverse = scaler.inverse_transform(imputed)

        # Untranspose
        print("Untransposing..")
        untransposed = inverse.transpose()

        # Back to a Dataframe
        imputed_df = pd.DataFrame(untransposed)

        # Return indexes
        imputed_df.index = data.index
        imputed_df.columns = data.columns.values

        # Write file
        imputed_df.to_csv(file + "_KNN_" + str(k) + '.txt', sep='\t')

    except Exception as e:
        import pdb
        pdb.set_trace()


if __name__ == '__main__':
    impute()