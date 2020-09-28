import sys
from toolkit.core.trajdataset import TrajDataset
from toolkit.core.trajlet import split_trajectories
from toolkit.benchmarking.load_all_datasets import get_datasets, all_dataset_names


# TODO: to be added later
def grouping(dataset: TrajDataset):
    return


def main():
    opentraj_root = sys.argv[1]
    output_dir = sys.argv[2]

    datasets = get_datasets(opentraj_root, all_dataset_names)
    for ds in datasets:
        grouping(ds)


if __name__ == "__main__":
    main()



