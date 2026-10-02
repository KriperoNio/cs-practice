git diff HEAD~2 HEAD -- lab03/calc.py
Показывает разницу в изменениях. При этом промежуточное состояние смешивается.

git show HEAD~1 
Отдельный КОНКРЕТНЫЙ коммит.

git log -S"def" --oneline -- lab03/calc.py
Поиск def в файле. Я не писал def (исправлю по необходимости)

git blame lab03/calc.py
Построчная информация изменения файла.

git restore lab03/calc.py
Возвращает файл в состояние пследнего коммита.

git restore --source=HEAD~2 lab03/calc.py
Возвращает файл в состояние коммита c меткой HEAD~2 (у меня HEAD~3).


