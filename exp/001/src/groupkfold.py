from sklearn.model_selection import KFold


class GroupKFoldWithSeed(KFold):
    """sklearnに用意されているGroupKFoldでseed固定ができないので, seed固定できるようにしたクラス"""

    def __init__(self, n_splits=5, shuffle=False, random_state=None):
        super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
        self.kf = KFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)

    def split(self, X, y, groups):
        unique_groups = groups.unique()
        for tr_group_idx, va_group_idx in self.kf.split(unique_groups):
            tr_groups, va_groups = unique_groups[tr_group_idx], unique_groups[va_group_idx]
            is_tr = groups.isin(tr_groups)
            is_va = groups.isin(va_groups)
            yield is_tr[is_tr].index.values, is_va[is_va].index.values
