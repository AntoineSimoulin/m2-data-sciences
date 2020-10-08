import os


def load_cls_file(file_path):
    reviews, labels = [], []
    with open(file_path) as f:
        line = f.readline()
        while line:
            review, label = line.strip().split('\t')
            reviews.append(review.strip("\""))
            labels.append(int(label))
            line = f.readline()
    return reviews, labels

def load_cls_dataset(file_path, section='books'):
    X_books, y_books = {}, {} # books
    for split in ['train', 'valid']:  # test
        X_books[split], y_books[split] = load_cls_file(os.path.join(file_path, section, '{}_0.tsv'.format(split)))
    return X_books, y_books