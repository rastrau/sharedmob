git checkout --orphan temp ee1d5286fcf72d008f19aae60c27bfeefa2ca671 # create a new branch without parent history from commit git checkout --orphan temp ee1d5286fcf72d008f19aae60c27bfeefa2ca671 (adjust this commit ID)
git commit -m "Truncated history" # create a first commit on this branch
git rebase --onto temp ee1d5286fcf72d008f19aae60c27bfeefa2ca671 main # now rebase the part of master branch that we want to keep onto this branch
git branch -D temp # delete the temp branch
git prune --progress # delete all the objects w/o references
git gc --aggressive # aggressively collect garbage; may take a lot of time on large repos
git push origin --force
