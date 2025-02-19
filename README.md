# 1. `Git`
- научиться создавать репозитории, управляти ими и решать конфликты случай чего.

---
---
---
### git setup on local mashine

`git config --global user.name "yurAndreiko"`

`git config --global user.email "imperuminate@gmail.com"`

`git config --list --show-origin`

### repositoty creation

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


# 2. `Python`
- выучить основы языка пайтона
- после завершения, прорешивать задачи на пайтон каждый день
# 3. `Pytest`
- научиться использовать для написания и организации тестов
# 4. `Playwright`
- научиться использовать для написания и организации тестов
# 5. `SQL`
- выучить команды и синтаксис
- решать задачи и практиковать sql  
# 6. `API`
- научиться использовать, понять как работать с либами
# 7. tools: 
`dotenv`, `defaultdict`, `faker`, `csv`
# 8. `CI/CD`:
- научиться настраивать свой проект в CI/CD

8.1 `GitHub Actions`\
8.2 `Jenkins`
# 9 `Docker`
# 10 `Selenium` 
- понять основы, попробовать по работать, для того чтобы было что сказать на собесе. Понять разницу между Selenium и Playwright