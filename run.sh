#!/usr/bin/env bash
# pyenv shell 3.6.0

# generate train test split
python train_test_split.py --chars_file characters/top_3000_simplified.txt --output_dir characters

# generate train images
python draw_multiple_characters.py --font font/simkai.ttf --ch_lists characters/train.txt --gray --output_dir output/top_3000/train/simkai
python draw_multiple_characters.py --font font/simsun.ttf --ch_lists characters/train.txt --gray --output_dir output/top_3000/train/simsun

# generate test images
python draw_multiple_characters.py --font font/simkai.ttf --ch_lists characters/test.txt --gray --output_dir output/top_3000/test/simkai
python draw_multiple_characters.py --font font/simsun.ttf --ch_lists characters/test.txt --gray --output_dir output/top_3000/test/simsun
