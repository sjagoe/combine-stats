import argparse
import glob
import os
import pstats


def combine(directory, pattern, output):
    pattern_directory = os.path.join(directory, pattern)
    files = glob.glob(pattern_directory)
    if len(files) == 0:
        raise RuntimeError('No files found matching {!r}'.format(
            pattern_directory))
    stats = pstats.Stats(files[0])
    for filename in files[1:]:
        stats.add(filename)
    stats.dump_stats(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=unicode)
    parser.add_argument('--pattern', default='*.pstats')
    parser.add_argument('--output', default='combined.pstats')
    args = parser.parse_args()

    combine(args.directory, args.pattern, args.output)


if __name__ == '__main__':
    main()
