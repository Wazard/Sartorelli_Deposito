import numpy as np

mat = np.random.randint(1,101, size=(6,6))
print(mat)

sub_mat = mat[1:5, 1:5]
print(sub_mat)

inverted_sub_mat = sub_mat[[3, 1, 2, 0]]
print(inverted_sub_mat)

diag = np.diag(inverted_sub_mat)
print(diag)

modified_inverted_sub_mat = np.where(inverted_sub_mat%3==0, -1, inverted_sub_mat)
print(modified_inverted_sub_mat)

print(f"OG:\n{mat}\nSUB:\n{sub_mat}\nINV_SUB:\n{inverted_sub_mat}\nDIAG:\n{diag}\nINV_MOD:\n{modified_inverted_sub_mat}")