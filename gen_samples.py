import click
import pandas as pd
import random

@click.command()
@click.option("--num-samples", default=10000, help="Number of Samples")
@click.argument('file')
def generate_samples(num_samples, file):
    """ Make dem samples """
    data = pd.read_csv(file, sep='\t', error_bad_lines=False)
    new_data = data.copy()

    col = None
    for x in range(len(data.columns), num_samples + 1):
        rand_header = random.choice(data.columns.values.tolist()[1:])
        col = data.loc[:, rand_header]
        col.name = "sample" + str(x)
        new_data[col.name] = col
        print("Made: " + col.name)

    new_data.to_csv(file + "_" + str(num_samples) + ".txt", sep='\t')

if __name__ == '__main__':
    generate_samples()