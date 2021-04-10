import numpy

idcg = lambda l: sum((1.0 / np.log(i + 2) for i in range(l)))

def _ndcg(gt, rec):
    dcg = 0.0
    for i, r in enumerate(rec):
        if r in gt:
            dcg += 1.0 / np.log(i + 2)

    return dcg / _idcgs[len(gt)]