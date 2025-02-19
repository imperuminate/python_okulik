# 1. `Git`
- научиться создавать репозитории, управляти ими и решать конфликты случай чего.

---
---
---
## git setup on local mashine

`git config --global user.name "yurAndreiko"`

`git config --global user.email "imperuminate@gmail.com"`

`git config --list --show-origin`

## repositoty creation and operation

`git init`

`git add .`

`git commit -m "comment"` or `git commit -am "comment"`

`git log`

`git checkout 0ff7ece7263203ebda06d63233a22f2a53e67e47` - вернуться к прошлому коммиту

`git switch -` отменить возврат, и вернуться к последнему коммиту

`git checkout PLANME.md` - отменить докомитные изменения (все изменения которые были до индексации - сбросятся). no changes added to commit

`git reset HEAD PLANME.md` - отменит последний git add . и вернут но не уберет изменения, нужно будет еще git checkout PLANME.md

`git checkout -b me` - создаст и перейдет на новую ветку, подтянув все актуальные изменения с предыдущей

`git checkout -b main` - перейдет или вернется на ветку

`git branch` - покажет все ветки

`git push`

`git clone git@github.com:imperuminate/python_okulik.git` - to downloan github project localy. You'll nean to setup SSH key

Setup [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

