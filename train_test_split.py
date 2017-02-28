import argparse
import random
from draw_multiple_characters import get_chars_set

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chars_file', type=str, default='characters/top_3000_simplified.txt', help='the char files to split')
    parser.add_argument('--output_dir', type=str, default='characters', help='output directory')
    FLAGS = parser.parse_args()
    chars_file = FLAGS.chars_file
    output_dir = FLAGS.output_dir
    chars = get_chars_set(chars_file)

    random.shuffle(chars)
    size = len(chars)
    train_portion = 0.7
    test_portion = 0.3

    train = chars[0:round(size * train_portion)]
    test = chars[round(size * train_portion):]
    train_file = f'{output_dir}/train.txt'
    test_file = f'{output_dir}/test.txt'
    with open(train_file, 'w') as f:
        f.writelines([f'{line}\n' for line in train])

    with open(test_file, 'w') as f:
        f.writelines(f'{line}\n' for line in test)


